# Паспорт вердикта

**FAIL** (exit 1) · маршрут Critical · репозиторий `.`  
Маршрут: auto: дифф недоступен (control: anti-bypass: . — база диффа недоступна: неоднозначный аргумент «origin/main...HEAD»: неизвестная редакция или не путь в рабочем каталоге. (не git-репозиторий, нет базового коммита или некорректный GIT_REF)) — fail-safe маршрут Critical

Красный здесь означает: механика нашла перечисленное в блоке 1. Блоки 2 и 3 говорят, чего не поймала и она, — на это не распространяется и красный.

## 1. Проверено

- **fitness** \* — FAIL — Правил: 7, нарушений: 3 (error: 1, warn: 2); реестр: 8 правил (error: 4), отпечаток 234b1f8c — файл: .arch-handoff/CONSTRAINTS.yaml
  находок: error 1, warn 2
- **delta_guard** \* — FAIL — сбой выполнения: control: git diff --name-only origin/main: неоднозначный аргумент «origin/main»: неизвестная редакция или не путь в рабочем каталоге.
- **rule_weakened** \* — SKIP — базовая ревизия 'origin/main' не существует (нет коммитов?) — сравнивать не с чем
- **spine_lint** \* — PASS — находок: 0 (error: 0)
- **trace_check** \* — SKIP — нет каталога model/
- **model_validate** \* — SKIP — нет каталога model/
- **sensors** \* — SKIP — нет каталога docs/spec — спецификаций для сенсоров нет
- **nfr** \* — SKIP — нет каталога model/ — нечего считать
- **evidence_verify** \* — SKIP — нет EVIDENCE.yaml ни в корне, ни в активных change-dir
- **decision_quality** — SKIP — не включена: добавьте 'decision_quality' в [gate.required] нужного маршрута
- **semantic_quality** — SKIP — не включена: добавьте 'semantic_quality' в [gate.required] нужного маршрута

\* — обязательна для маршрута Critical; остальные — сверх неё.

## 2. Заявлено, но механикой не проверяется

- **fitness** — правил, судящих по ТЕКСТУ файла (наличие/запрет слова), — 8 из 8; они зеленеют и когда инвариант соблюдён, и когда о нём просто написали (исполняемых проверок поведения: 0)
- **смысл** — смысл решения, ссылок и кода механикой не проверяется (не включена: добавьте 'semantic_quality' в [gate.required] нужного маршрута)
  → включите `semantic_quality` в [gate.required] и прогоните смысловую рубрику по досье: `adr_spine_consistency` — решение против инварианта, `model_link_semantics` — ссылка не на ту сущность, `nfr_mechanism_fit` — обещание без механизма, `code_invariant_conformance` — код против инварианта

## 3. Не проверено

- **rule_weakened** — базовая ревизия 'origin/main' не существует (нет коммитов?) — сравнивать не с чем (обязательна для маршрута Critical — итог INCOMPLETE)
- **trace_check** — нет каталога model/ (обязательна для маршрута Critical — итог INCOMPLETE)
- **model_validate** — нет каталога model/ (обязательна для маршрута Critical — итог INCOMPLETE)
- **sensors** — нет каталога docs/spec — спецификаций для сенсоров нет (обязательна для маршрута Critical — итог INCOMPLETE)
- **nfr** — нет каталога model/ — нечего считать (обязательна для маршрута Critical — итог INCOMPLETE)
- **evidence_verify** — нет EVIDENCE.yaml ни в корне, ни в активных change-dir (обязательна для маршрута Critical — итог INCOMPLETE)
- **decision_quality** — не включена: добавьте 'decision_quality' в [gate.required] нужного маршрута (не обязательна для маршрута)
- **semantic_quality** — не включена: добавьте 'semantic_quality' в [gate.required] нужного маршрута (не обязательна для маршрута)

## Аттестация

```
sha256:339c01a20cde52e7f55be41af7b080dda26aa83e94f94609c2f49de5197d2b4b
arch-be gate --repo . --format json > verdict.json && arch-be gate --repo . --verify-envelope verdict.json
```
