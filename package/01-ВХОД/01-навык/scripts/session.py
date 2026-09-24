#!/usr/bin/env python3
"""session.py — оркестратор 90-минутной сессии Spine Core для корпоративного архитектора.

Все проверки выполняет Spine Core (бинарь arch-be); скрипт только готовит входы,
вызывает arch-be и собирает результаты в markdown-отчёты для показа на встрече.

Команды (запуск из корня рабочей папки сессии):
  init <dir> [--demo SPINE_REPO]
                      создать рабочую папку сессии из шаблонов (или для репетиции)
  preflight           проверить окружение, контекст и «настройку» числа находок
  check               прогнать корпоративные правила по репозиториям архитектора
  fleet init|check|bump|repin|report
                      демо «стандарт как продукт»: версии, наследование, отчёт ДКА
  bypass              демо лазеек (удаление extends, затенение, фиктивный ADR) и их закрытия
  effective           собрать эффективный файл ДКА: правила ДКА + исключения из реестра ДКА
  selftest [--scaffold]
                      проверка надёжности правил на примерах bad/good/bypass
  pack                собрать раздаточный пакет для архитектора

Общий параметр: --session PATH (по умолчанию context/session.yaml).
Бинарь: переменная ARCH_BE или spine.arch_be в session.yaml (иначе arch-be из PATH).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Нужен PyYAML: pip install pyyaml")

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATES = SKILL_DIR / "assets" / "templates"
MAX_EXCEPTION_DAYS = 180


# ----------------------------------------------------------------- контекст
def load_ctx(path: str) -> dict:
    p = Path(path).resolve()
    if not p.exists():
        sys.exit(f"Не найден {p}. Сначала: session.py init <папка> и заполните context/session.yaml")
    cfg = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    cfg["_root"] = p.parent.parent  # <workspace>/context/session.yaml
    return cfg


def rp(ctx: dict, value) -> Path:
    s = os.path.expanduser(str(value))
    pth = Path(s)
    return pth if pth.is_absolute() else (ctx["_root"] / pth)


def arch_be(ctx: dict) -> str:
    return os.environ.get("ARCH_BE") or (ctx.get("spine") or {}).get("arch_be") or "arch-be"


def run_be(ctx: dict, args: list[str], timeout: int = 900) -> tuple[int, str, str]:
    cmd = [arch_be(ctx)] + args
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError:
        sys.exit(f"Не найден бинарь Spine Core: {cmd[0]}. Задайте ARCH_BE или spine.arch_be")
    except subprocess.TimeoutExpired:
        return 124, "", f"таймаут {timeout} с: {' '.join(cmd)}"
    return r.returncode, r.stdout, r.stderr


def repos(ctx: dict) -> list[dict]:
    out = []
    for r in ctx.get("repos") or []:
        out.append({"name": r["name"], "path": rp(ctx, r["path"])})
    if not out:
        sys.exit("В session.yaml не указаны repos")
    return out


def corp_rules_path(ctx: dict) -> Path:
    return rp(ctx, (ctx.get("spine") or {}).get("corp_rules", "work/CONSTRAINTS.corp.yaml"))


def load_rules(path: Path) -> tuple[dict, list[dict]]:
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rules = doc.get("constraints") or doc.get("rules") or []
    return doc, rules


def rule_meta(rules: list[dict]) -> dict:
    meta = {}
    for r in rules:
        if "name" in r:
            meta[r["name"]] = {
                "id": r.get("id", ""),
                "std_ref": r.get("std_ref", ""),
                "severity": r.get("severity", ""),
                "type": r.get("type", "unverifiable" if r.get("unverifiable") else ""),
            }
    return meta


def check_json(ctx: dict, repo: Path, rules: Path) -> dict:
    rc, out, err = run_be(ctx, ["control", "check", str(repo), "--constraints", str(rules),
                                "--no-exec", "--json"])
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        data = {"passed": False, "issues": [], "_error": (out + err).strip()[:800]}
    data["_rc"] = rc
    return data


def reports_dir(ctx: dict) -> Path:
    d = ctx["_root"] / "reports"
    d.mkdir(parents=True, exist_ok=True)
    return d


def md_cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")[:160]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"→ {path}")


# ----------------------------------------------------------------- init
def cmd_init(a) -> None:
    ws = Path(a.dir).resolve()
    for sub in ["context/standard", "work/rules-tests", "reports", "sandbox", "handout"]:
        (ws / sub).mkdir(parents=True, exist_ok=True)
    plan = {
        "context/session.yaml": "session.yaml",
        "context/exceptions.yaml": "exceptions.yaml",
        "work/requirements.md": "requirements.md",
        "work/pilot-canvas.md": "pilot-canvas.md",
        "work/CONSTRAINTS.corp.yaml": "CONSTRAINTS.corp.yaml",
    }
    for dst, src in plan.items():
        target = ws / dst
        if target.exists():
            print(f"= уже есть, не трогаю: {target}")
            continue
        shutil.copy(TEMPLATES / src, target)
        print(f"+ {target}")
    if a.demo:
        demo, spine = SKILL_DIR / "assets" / "demo", Path(os.path.expanduser(a.demo)).resolve()
        cases = {"payments-arm-a": spine / "кейсы" / "drift-control" / "armA-solution",
                 "payments-arm-b": spine / "кейсы" / "drift-control" / "armB-solution",
                 "cards-product": spine / "examples" / "corp-spine" / "product"}
        missing = [str(p) for p in cases.values() if not p.exists()]
        if missing:
            sys.exit("Не найдены каталоги репетиции в клоне Spine:\n  " + "\n  ".join(missing))
        shutil.copy(demo / "payment-core-standard.md", ws / "context" / "standard")
        shutil.copy(demo / "CONSTRAINTS.corp.yaml", ws / "work" / "CONSTRAINTS.corp.yaml")
        shutil.copy(demo / "new-rules.yaml", ws / "work" / "new-rules.yaml")
        shutil.copytree(demo / "rules-tests", ws / "work" / "rules-tests", dirs_exist_ok=True)
        cfg = yaml.safe_load((ws / "context" / "session.yaml").read_text(encoding="utf-8"))
        cfg["session"]["architect"] = "Репетиция"
        cfg["standard"].update({"title": "Стандарт платёжного ядра v2 (демо)",
                                "files": ["context/standard/payment-core-standard.md"],
                                "architecture_md": None})
        cfg["repos"] = [{"name": n, "path": str(p)} for n, p in cases.items()]
        cfg["tuning"] = {"min_findings": 3, "max_findings": 30}
        (ws / "context" / "session.yaml").write_text(
            yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False), encoding="utf-8")
        print(f"\nРепетиция: данные демо из {demo}, репозитории — кейсы из клона Spine {spine}")
        print("Дальше: preflight → check → selftest → fleet init/bump/report/repin → bypass → pack")
        return
    print("\nДальше: положите экспорт стандарта в context/standard/, заполните context/session.yaml")


# ----------------------------------------------------------------- preflight
def cmd_preflight(a) -> None:
    ctx = load_ctx(a.session)
    tuning = ctx.get("tuning") or {}
    lo, hi = int(tuning.get("min_findings", 5)), int(tuning.get("max_findings", 30))
    lines, problems = ["# Предполётная проверка сессии", ""], []

    rc, out, err = run_be(ctx, ["--version"], timeout=30)
    lines.append(f"- Spine Core: `{(out or err).strip()}`")
    if rc != 0:
        problems.append("arch-be не запускается")

    std = ctx.get("standard") or {}
    for f in std.get("files") or []:
        ok = rp(ctx, f).exists()
        lines.append(f"- Стандарт: `{f}` — {'есть' if ok else 'НЕТ'}")
        if not ok:
            problems.append(f"нет файла стандарта {f}")

    rules_path = corp_rules_path(ctx)
    try:
        _, rules = load_rules(rules_path)
    except Exception as e:  # noqa: BLE001
        sys.exit(f"Не читается {rules_path}: {e}")
    unverif = [r for r in rules if r.get("unverifiable")]
    no_ref = [r.get("name", "?") for r in rules if not r.get("std_ref") and not r.get("unverifiable")]
    lines.append(f"- Корпоративные правила: `{rules_path.name}` — {len(rules)} правил, "
                 f"из них непроверяемых (unverifiable): {len(unverif)}")
    if no_ref:
        problems.append("правила без std_ref (нет ссылки на пункт стандарта): " + ", ".join(no_ref))

    meta = rule_meta(rules)
    per_rule = {n: 0 for n in meta}
    total = 0
    lines += ["", "| Репозиторий | Гейт | error | warn |", "|---|---|---|---|"]
    for r in repos(ctx):
        if not r["path"].exists():
            problems.append(f"нет репозитория {r['path']}")
            lines.append(f"| {r['name']} | НЕТ ПУТИ | — | — |")
            continue
        d = check_json(ctx, r["path"], rules_path)
        if d.get("_error"):
            problems.append(f"{r['name']}: ошибка arch-be: {d['_error'][:200]}")
        issues = d.get("issues") or []
        e = sum(1 for i in issues if i.get("severity") in ("error", "critical", "high", "block"))
        w = len(issues) - e
        total += len(issues)
        for i in issues:
            per_rule[i.get("rule", "?")] = per_rule.get(i.get("rule", "?"), 0) + 1
        lines.append(f"| {r['name']} | {'PASS' if d.get('passed') else 'FAIL'} | {e} | {w} |")

    lines += ["", f"**Всего находок: {total}** (целевой коридор для встречи: {lo}–{hi})", ""]
    if total == 0:
        problems.append("ноль находок — вау-эффекта не будет: выберите другие правила или репозитории")
    elif total > hi:
        problems.append(f"находок больше {hi}: снимите baseline или покажите топ-10 (check --top 10)")
    silent = [n for n, c in per_rule.items() if c == 0 and meta.get(n, {}).get("type") != "unverifiable"]
    lines += ["| Правило | Пункт стандарта | Находок |", "|---|---|---|"]
    for n, c in sorted(per_rule.items(), key=lambda x: -x[1]):
        lines.append(f"| {n} | {md_cell(meta.get(n, {}).get('std_ref', ''))} | {c} |")
    if silent:
        lines += ["", "Правила без находок (проверьте, не сломаны ли они — selftest): " + ", ".join(silent)]
    lines += ["", "## Проблемы", ""] + ([f"- {p}" for p in problems] or ["- нет, можно проводить"])
    lines += ["", "Перед встречей вручную просмотрите находки на ложные срабатывания "
              "(reports/check.md): одно ложное срабатывание в начале сессии подрывает доверие."]
    write(reports_dir(ctx) / "preflight.md", "\n".join(lines) + "\n")
    print("\n".join(lines[-8:]))


# ----------------------------------------------------------------- check
def cmd_check(a) -> None:
    ctx = load_ctx(a.session)
    rules_path = Path(a.rules).resolve() if a.rules else corp_rules_path(ctx)
    _, rules = load_rules(rules_path)
    meta = rule_meta(rules)
    rows, summary, raw = [], [], {}
    for r in repos(ctx):
        d = check_json(ctx, r["path"], rules_path)
        raw[r["name"]] = d
        issues = d.get("issues") or []
        summary.append((r["name"], "PASS" if d.get("passed") else "FAIL", len(issues)))
        for i in issues:
            m = meta.get(i.get("rule", ""), {})
            rows.append((r["name"], i.get("rule", ""), m.get("std_ref", ""),
                         f"{i.get('file', '')}:{i.get('line', '')}", i.get("severity", ""),
                         i.get("message", "")))
    title = (ctx.get("standard") or {}).get("title", "стандарт")
    out = [f"# Проверка: {title}", "",
           f"Spine Core, правил: {len(rules)}, режим `--no-exec` (команды из правил не исполняются). "
           "Находки уровня warn видны, но гейт не ломают (PASS).", "",
           "| Репозиторий | Гейт | Находок |", "|---|---|---|"]
    out += [f"| {n} | {s} | {c} |" for n, s, c in summary]
    shown = rows[: a.top] if a.top else rows
    out += ["", "| Репозиторий | Правило | Пункт стандарта | Где | Уровень | Суть |",
            "|---|---|---|---|---|---|"]
    out += ["| " + " | ".join(md_cell(x) for x in row) + " |" for row in shown]
    if a.top and len(rows) > a.top:
        out.append(f"\n…и ещё {len(rows) - a.top} находок (полный список — reports/check.json)")
    write(reports_dir(ctx) / "check.md", "\n".join(out) + "\n")
    write(reports_dir(ctx) / "check.json", json.dumps(raw, ensure_ascii=False, indent=1))
    for n, s, c in summary:
        print(f"  {n:<30} {s:<5} находок: {c}")


# ----------------------------------------------------------------- effective
def build_effective(corp: Path, exceptions: Path, out: Path) -> tuple[int, int]:
    doc, rules = load_rules(corp)
    ex = {}
    if exceptions.exists():
        ex = yaml.safe_load(exceptions.read_text(encoding="utf-8")) or {}
    today, approved = dt.date.today(), []
    for o in ex.get("overrides") or []:
        missing = [k for k in ("rule", "adr", "until") if not o.get(k)]
        if missing:
            sys.exit(f"[error] исключение {o}: нет полей {missing}")
        until = str(o["until"])
        end = dt.date.fromisoformat(until if len(until) == 10 else until + "-28")
        if (end - today).days > MAX_EXCEPTION_DAYS:
            sys.exit(f"[error] {o['rule']}: исключение длиннее {MAX_EXCEPTION_DAYS} дней")
        approved.append({"rule": o["rule"], "adr": o["adr"], "until": until})
    doc.pop("overrides", None)
    if approved:
        doc["overrides"] = approved
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return len(rules), len(approved)


def exceptions_path(ctx: dict) -> Path:
    return rp(ctx, (ctx.get("spine") or {}).get("exceptions", "context/exceptions.yaml"))


def cmd_effective(a) -> None:
    ctx = load_ctx(a.session)
    out = ctx["_root"] / "sandbox" / "corp" / "effective-corp.yaml"
    n, k = build_effective(corp_rules_path(ctx), exceptions_path(ctx), out)
    print(f"эффективный файл ДКА: {out} — правил {n}, одобренных исключений {k}")


# ----------------------------------------------------------------- fleet
def fleet_paths(ctx: dict) -> tuple[Path, Path]:
    sb = ctx["_root"] / "sandbox"
    return sb / "corp" / "CONSTRAINTS.corp.yaml", sb / "products"


def corp_version(path: Path) -> str:
    doc, _ = load_rules(path)
    return str(doc.get("version", ""))


def bump_version(v: str) -> str:
    m = re.match(r"^(.*?)(\d+)$", v)
    return f"{m.group(1)}{int(m.group(2)) + 1}" if m else v + ".1"


def write_product(pfile: Path, version: str, extra: dict | None = None) -> None:
    doc = {"extends": [f"../../corp/CONSTRAINTS.corp.yaml@{version}"]}
    if extra:
        doc.update(extra)
    pfile.parent.mkdir(parents=True, exist_ok=True)
    pfile.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")


def cmd_fleet(a) -> None:
    ctx = load_ctx(a.session)
    corp, products = fleet_paths(ctx)
    if a.action == "init":
        doc, _ = load_rules(corp_rules_path(ctx))
        doc["version"] = str((ctx.get("spine") or {}).get("corp_version", doc.get("version", "2026.1")))
        doc.pop("overrides", None)
        corp.parent.mkdir(parents=True, exist_ok=True)
        corp.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")
        for r in repos(ctx):
            write_product(products / r["name"] / "CONSTRAINTS.yaml", doc["version"])
        print(f"флот: корпоративный слой версии {doc['version']}, продуктов {len(repos(ctx))}")
        print("Репозитории не изменяются: файлы продуктов лежат в sandbox/products/")
        return
    if not corp.exists():
        sys.exit("Сначала: session.py fleet init")
    if a.action == "bump":
        doc, rules = load_rules(corp)
        old = str(doc.get("version", ""))
        doc["version"] = a.to or bump_version(old)
        if a.add_rules:
            add = yaml.safe_load(Path(a.add_rules).read_text(encoding="utf-8")) or []
            add = add.get("constraints", add) if isinstance(add, dict) else add
            key = "constraints" if "constraints" in doc else "rules"
            doc[key] = (doc.get(key) or []) + list(add)
        corp.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")
        print(f"ДКА выпустила версию {old} → {doc['version']}"
              + (f", добавлено правил: {len(add)}" if a.add_rules else ""))
        a.action = "check"
    if a.action == "repin":
        v = corp_version(corp)
        for r in repos(ctx):
            write_product(products / r["name"] / "CONSTRAINTS.yaml", v)
        print(f"все продукты перепинены на {v}")
        a.action = "check"
    if a.action == "check":
        out = [f"# Флот: корпоративный слой версии {corp_version(corp)}", "",
               "| Продукт | Гейт | Находок | Версия стандарта |", "|---|---|---|---|"]
        for r in repos(ctx):
            d = check_json(ctx, r["path"], products / r["name"] / "CONSTRAINTS.yaml")
            issues = d.get("issues") or []
            pin = next((i.get("message", "") for i in issues if "родитель обновился" in i.get("message", "")), "")
            out.append(f"| {r['name']} | {'PASS' if d.get('passed') else 'FAIL'} | {len(issues)} | "
                       f"{md_cell(pin) if pin else 'актуальная'} |")
        write(reports_dir(ctx) / "fleet-check.md", "\n".join(out) + "\n")
        print("\n".join(out[2:]))
        return
    if a.action == "report":
        out = ["# Отчёт ДКА по флоту (control report --level corp)", "",
               "| Продукт | Унаследовано | pass | warn | fail | Исключения | Просрочено | Расхождения версий |",
               "|---|---|---|---|---|---|---|---|"]
        agg = []
        for r in repos(ctx):
            rc, so, se = run_be(ctx, ["control", "report", str(r["path"]), "--constraints",
                                      str(products / r["name"] / "CONSTRAINTS.yaml"),
                                      "--level", "corp", "--json"])
            try:
                d = json.loads(so)
            except json.JSONDecodeError:
                out.append(f"| {r['name']} | ошибка: {md_cell((so + se)[:120])} | | | | | | |")
                continue
            agg.append(d)
            inh = ", ".join(f"{k} ({v})" for k, v in (d.get("inherited") or {}).items())
            ovr = ", ".join(f"{o.get('rule')}:{o.get('status')}" for o in d.get("overrides") or []) or "—"
            out.append(f"| {r['name']} | {md_cell(inh)} | {d.get('pass', '')} | {d.get('warn', '')} | "
                       f"{d.get('fail', '')} | {md_cell(ovr)} | {len(d.get('expired_rules') or [])} | "
                       f"{len(d.get('version_mismatches') or [])} |")
        write(reports_dir(ctx) / "fleet-report.md", "\n".join(out) + "\n")
        write(reports_dir(ctx) / "fleet-report.json", json.dumps(agg, ensure_ascii=False, indent=1))
        print("\n".join(out[2:]))


# ----------------------------------------------------------------- bypass
def cmd_bypass(a) -> None:
    ctx = load_ctx(a.session)
    corp, _ = fleet_paths(ctx)
    if not corp.exists():
        sys.exit("Сначала: session.py fleet init")
    version = corp_version(corp)
    target, rule = None, a.rule
    for r in repos(ctx) if not a.repo else [x for x in repos(ctx) if x["name"] == a.repo]:
        d = check_json(ctx, r["path"], corp)
        hits = [i for i in d.get("issues") or [] if not rule or i.get("rule") == rule]
        if hits:
            target, rule = r, rule or hits[0]["rule"]
            break
    if not target:
        sys.exit("Нет находок для демо лазеек: укажите --repo/--rule или используйте selftest")

    sb = ctx["_root"] / "sandbox" / "bypass"
    own_rule = {"name": "product_readme", "type": "file_exists", "path": ".", "severity": "warn"}
    variants = [
        ("Честный продукт: наследует слой ДКА", {}),
        ("А. Удалил extends (оставил свои правила)", None),
        ("Б. Затенил правило ДКА своим пустым", {"constraints": [
            {"name": rule, "type": "file_exists", "path": ".", "severity": "warn"}]}),
        ("В. Исключение с несуществующим ADR до 2030", {"overrides": [
            {"rule": rule, "adr": "ADR-999", "until": "2030-01"}]}),
    ]
    rows = []
    for i, (label, extra) in enumerate(variants):
        pfile = sb / f"v{i}" / "CONSTRAINTS.yaml"
        if extra is None:
            pfile.parent.mkdir(parents=True, exist_ok=True)
            pfile.write_text(yaml.safe_dump({"constraints": [own_rule]}, allow_unicode=True), encoding="utf-8")
        else:
            write_product(pfile, version, extra)
        d = check_json(ctx, target["path"], pfile)
        seen = any(x.get("rule") == rule for x in d.get("issues") or [])
        rows.append((label, "продуктовый файл", "видно" if seen else "СКРЫТО"))

    eff = ctx["_root"] / "sandbox" / "corp" / "effective-corp.yaml"
    build_effective(corp, exceptions_path(ctx), eff)
    d = check_json(ctx, target["path"], eff)
    seen = any(x.get("rule") == rule for x in d.get("issues") or [])
    rows.append(("Любой из вариантов А–В", "эффективный файл ДКА", "видно" if seen else "скрыто (одобренное исключение)"))

    out = [f"# Лазейки и их закрытие: правило `{rule}` в `{target['name']}`", "",
           "| Что сделал продукт | Чем проверяли | Нарушение |", "|---|---|---|"]
    out += [f"| {a_} | {b_} | {c_} |" for a_, b_, c_ in rows]
    out += ["", "Вывод: проверка по продуктовому файлу доверяет продукту в части корпоративных правил. "
            "Эффективный файл ДКА собирается из правил и реестра исключений ДКА, "
            "поэтому продукт не может выключить корпоративный слой."]
    write(reports_dir(ctx) / "bypass.md", "\n".join(out) + "\n")
    print("\n".join(out[2:]))


# ----------------------------------------------------------------- selftest
def cmd_selftest(a) -> None:
    ctx = load_ctx(a.session)
    _, rules = load_rules(corp_rules_path(ctx))
    base = ctx["_root"] / "work" / "rules-tests"
    if a.scaffold:
        for r in rules:
            if r.get("unverifiable") or "name" not in r:
                continue
            for case in ("bad", "good", "bypass"):
                d = base / r["name"] / case
                d.mkdir(parents=True, exist_ok=True)
                note = d / "README.md"
                if not note.exists():
                    note.write_text(f"# {r['name']} / {case}\n\nПоложите сюда минимальные файлы: "
                                    f"bad — нарушение, good — соблюдение, bypass — формальный обход.\n"
                                    f"Пути внутри каталога должны попадать под glob правила: {r.get('glob', r.get('path', ''))}\n",
                                    encoding="utf-8")
        print(f"каталоги примеров созданы в {base}")
        return
    rows = []
    tmp = ctx["_root"] / "sandbox" / "selftest"
    for r in rules:
        name = r.get("name")
        if not name or r.get("unverifiable") or not (base / name).exists():
            continue
        single = tmp / f"{name}.yaml"
        single.parent.mkdir(parents=True, exist_ok=True)
        single.write_text(yaml.safe_dump({"constraints": [r]}, allow_unicode=True, sort_keys=False),
                          encoding="utf-8")
        res = {}
        for case in ("bad", "good", "bypass"):
            d = base / name / case
            files = [f for f in d.rglob("*") if f.is_file() and f.name != "README.md"] if d.exists() else []
            if not files:
                res[case] = None
                continue
            j = check_json(ctx, d, single)
            res[case] = any(x.get("rule") == name for x in j.get("issues") or [])
        if res["bad"] is False or res["good"] is True:
            verdict = "сломано"
        elif res["bypass"] is False:
            verdict = "хрупко: обходится"
        elif res["bypass"] is True:
            verdict = "надёжно"
        else:
            verdict = "нет примера обхода"
        mark = {True: "ловит", False: "не ловит", None: "—"}
        rows.append((name, mark[res["bad"]], mark[res["good"]], mark[res["bypass"]], verdict))
    out = ["# Надёжность правил", "",
           "| Правило | bad (должно ловить) | good (не должно) | bypass | Вердикт |", "|---|---|---|---|---|"]
    out += [f"| {' | '.join(row)} |" for row in rows]
    out += ["", "В блокирующий режим (block) переводятся только правила с вердиктом «надёжно»."]
    write(reports_dir(ctx) / "selftest.md", "\n".join(out) + "\n")
    print("\n".join(out[2:]))


# ----------------------------------------------------------------- pack
def cmd_pack(a) -> None:
    ctx = load_ctx(a.session)
    root, dst = ctx["_root"], ctx["_root"] / "handout"
    dst.mkdir(parents=True, exist_ok=True)
    items = [root / "work" / "requirements.md", corp_rules_path(ctx), root / "work" / "pilot-canvas.md"]
    items += sorted((root / "reports").glob("*.md"))
    copied = []
    for f in items:
        if f.exists():
            shutil.copy(f, dst / f.name)
            copied.append(f.name)
    std = ctx.get("standard") or {}
    readme = [f"# Итоги сессии Spine Core — {std.get('title', '')}", "",
              f"Архитектор: {(ctx.get('session') or {}).get('architect', '')}, "
              f"дата: {dt.date.today().isoformat()}", "", "## Что в пакете", ""]
    readme += [f"- `{c}`" for c in copied]
    readme += ["", "## Главное", "",
               "Раньше результатом работы был документ, который объясняет стандарт. "
               "Теперь — ещё и проверка, которая показывает, соблюдается ли он.", ""]
    write(dst / "README.md", "\n".join(readme) + "\n")
    archive = shutil.make_archive(str(root / "handout-spine-session"), "zip", dst)
    print(f"архив: {archive}")


# ----------------------------------------------------------------- main
def main() -> None:
    ap = argparse.ArgumentParser(description="Оркестратор сессии Spine Core")
    ap.add_argument("--session", default="context/session.yaml")
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("init"); p.add_argument("dir")
    p.add_argument("--demo", metavar="SPINE_REPO", help="репетиция на кейсах из клона Spine")
    p.set_defaults(fn=cmd_init)
    sp.add_parser("preflight").set_defaults(fn=cmd_preflight)
    p = sp.add_parser("check"); p.add_argument("--rules"); p.add_argument("--top", type=int, default=0)
    p.set_defaults(fn=cmd_check)
    sp.add_parser("effective").set_defaults(fn=cmd_effective)
    p = sp.add_parser("fleet"); p.add_argument("action", choices=["init", "check", "bump", "repin", "report"])
    p.add_argument("--to"); p.add_argument("--add-rules"); p.set_defaults(fn=cmd_fleet)
    p = sp.add_parser("bypass"); p.add_argument("--repo"); p.add_argument("--rule"); p.set_defaults(fn=cmd_bypass)
    p = sp.add_parser("selftest"); p.add_argument("--scaffold", action="store_true"); p.set_defaults(fn=cmd_selftest)
    sp.add_parser("pack").set_defaults(fn=cmd_pack)
    a = ap.parse_args()
    if a.cmd != "init":
        a.session = str(Path(a.session).resolve())
        os.chdir(Path(a.session).parent.parent)
    a.fn(a)


if __name__ == "__main__":
    main()
