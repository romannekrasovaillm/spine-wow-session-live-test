# Предполётная проверка сессии

- Spine Core: `arch-be 0.3.8`
- Стандарт: `context/standard/payment-core-standard.md` — есть
- Корпоративные правила: `CONSTRAINTS.corp.yaml` — 9 правил, из них непроверяемых (unverifiable): 1

| Репозиторий | Гейт | error | warn |
|---|---|---|---|
| payments-arm-a | PASS | 0 | 2 |
| payments-arm-b | PASS | 0 | 0 |
| cards-product | FAIL | 1 | 2 |

**Всего находок: 5** (целевой коридор для встречи: 3–30)

| Правило | Пункт стандарта | Находок |
|---|---|---|
| errors_via_thiserror | §3.2 Ошибки | 2 |
| authorize_idempotent | §4.1 Идемпотентность | 2 |
| tech_radar_hold | §5.1 Техрадар | 1 |
| no_float_for_money | §2.1 Денежные суммы | 0 |
| no_anyhow_in_code | §3.2 Ошибки | 0 |
| no_box_dyn_error | §3.2 Ошибки | 0 |
| tech_radar_renamed | §5.1 Техрадар | 0 |
| no_float_literals_for_money | §2.1 Денежные суммы (ред. 2026.2) | 0 |
| observability_standard | §6.1 Наблюдаемость | 0 |

Правила без находок (проверьте, не сломаны ли они — selftest): no_float_for_money, no_anyhow_in_code, no_box_dyn_error, tech_radar_renamed, no_float_literals_for_money

## Проблемы

- нет, можно проводить

Перед встречей вручную просмотрите находки на ложные срабатывания (reports/check.md): одно ложное срабатывание в начале сессии подрывает доверие.
