# Гейт в CI: доказательства

Прогон на живом контуре `sandbox/ci-demo/` (репозиторий продукта с реестром ДКА
внутри: `.arch-handoff/CONSTRAINTS.yaml`). Скрипт — `work/ci/gate.sh`.

## 1. Ветка `main`: нарушение стандарта

```
$ bash ci/gate.sh .
гейт: КРАСНЫЙ — см. gate-artifacts/gate-junit.xml и gate-artifacts/verdict-passport.md
exit 1
```

Паспорт вердикта, блок «Проверено»:

| Составляющая | Вердикт | Что внутри |
|---|---|---|
| `fitness` | **FAIL** | Правил: 8, нарушений: 3 (error: 1, warn: 2); отпечаток реестра `234b1f8c` |
| `delta_guard` | PASS | изменённых файлов: 0 |
| `rule_weakened` | PASS | реестр не ослаблен относительно `main` |
| `spine_lint` | PASS | находок: 0 |

`error` — это `tech_radar_hold` (`left-pad` в `Cargo.toml`). Артефакт `gate-junit.xml`
падает в UI Jenkins как failed test:

```xml
<testsuites name="arch-be gate" tests="10" failures="1" skipped="4">
  <testsuite name="fitness" tests="3" failures="1">
    <testcase classname="fitness" name="[warn] errors_via_thiserror — **/Cargo.toml:0">…
```

## 2. Ветка `weaken-registry`: продукт правит реестр ДКА

Продукт понизил `tech_radar_hold` с `block` до `warn` и вырезал `left-pad` из `deny`.

| Составляющая | Вердикт | Что внутри |
|---|---|---|
| `fitness` | **PASS** | нарушений: 2 (error: 0, warn: 2) — нарушение спрятано |
| `rule_weakened` | **FAIL** | ослаблений правил относительно `main`: 1 |

Итог — гейт всё равно красный (`exit 1`). Отпечаток реестра сменился
`234b1f8c` → `3342ab7c`: расхождение видно и в отчёте, и в дифе реестра.

**Вывод:** проверка идёт по реестру ДКА, лежащему в репозитории, а его ослабление —
самостоятельное нарушение. Продукт не может ни отключить корпоративное правило,
ни тихо понизить его уровень.

## 3. Пломба вердикта

`gate.sh` сохраняет `verdict.json` — конверт с аттестацией `sha256`. Вердикт относится
к конкретному состоянию дерева; подмену состояния после зелёного ловит:

```bash
arch-be gate --repo . --constraints .arch-handoff/CONSTRAINTS.yaml \
  --verify-envelope gate-artifacts/verdict.json
```

## 4. Детерминизм

Два прогона `session.py check` по трём репозиториям дали побайтово идентичный
`check.json`. Одинаковый вход — одинаковый вердикт: гейт не «мигает».
