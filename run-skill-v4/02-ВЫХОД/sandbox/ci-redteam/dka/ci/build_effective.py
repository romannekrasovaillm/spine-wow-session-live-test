#!/usr/bin/env python3
"""build_effective.py — эффективный корпоративный файл для продукта (шаблон ДКА, не генерируется агентом).

Правила берутся ТОЛЬКО из слоя ДКА, исключения — ТОЛЬКО из реестра ДКА.
Продуктовый CONSTRAINTS.yaml в корпоративной проверке не участвует: так закрываются
самовольные исключения, затенение корпоративных правил и удаление extends.

usage: build_effective.py <corp.yaml> <exceptions.yaml> <out.yaml> [--max-days 180]
"""
import datetime as dt
import sys
from pathlib import Path

import yaml


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    max_days = 180
    if "--max-days" in sys.argv:
        max_days = int(sys.argv[sys.argv.index("--max-days") + 1])
        args = [a for a in args if a != str(max_days)]
    if len(args) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    corp, exc, out = map(Path, args)
    doc = yaml.safe_load(corp.read_text(encoding="utf-8")) or {}
    ex = yaml.safe_load(exc.read_text(encoding="utf-8")) if exc.exists() else {}
    today, approved = dt.date.today(), []
    for o in (ex or {}).get("overrides") or []:
        missing = [k for k in ("rule", "adr", "until") if not o.get(k)]
        if missing:
            print(f"[error] исключение {o}: нет полей {missing}", file=sys.stderr)
            return 1
        until = str(o["until"])
        end = dt.date.fromisoformat(until if len(until) == 10 else until + "-28")
        if (end - today).days > max_days:
            print(f"[error] {o['rule']}: исключение длиннее {max_days} дней", file=sys.stderr)
            return 1
        approved.append({"rule": o["rule"], "adr": o["adr"], "until": until})
    doc.pop("overrides", None)
    doc.pop("extends", None)
    if approved:
        doc["overrides"] = approved
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
