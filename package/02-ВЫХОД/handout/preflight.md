# Предполётная проверка сессии

- Spine Core: `arch-be 0.3.8`
- Стандарт: `context/standard/payment-core-standard.md` — есть
- Корпоративные правила: `CONSTRAINTS.corp.yaml` — 6 правил, из них непроверяемых (unverifiable): 2

| Репозиторий | Гейт | error | warn |
|---|---|---|---|
| payments-arm-a | PASS | 0 | 2 |
| payments-arm-b | PASS | 0 | 0 |
| cards-product | PASS | 0 | 1 |

**Всего находок: 3** (целевой коридор для встречи: 3–30)

| Правило | Пункт стандарта | Находок |
|---|---|---|
| thiserror_for_errors | Стандарт платёжного ядра v2 §3.2 | 2 |
| tech_radar_hold | Стандарт платёжного ядра v2 §5.1 | 1 |
| no_float_for_money | Стандарт платёжного ядра v2 §2.1 | 0 |
| authorize_idempotent | Стандарт платёжного ядра v2 §4.1 | 0 |
| observability_standard | Стандарт платёжного ядра v2 §6.1 | 0 |
| no_box_dyn_error | Стандарт платёжного ядра v2 §3.2 | 0 |

Правила без находок (проверьте, не сломаны ли они — selftest): no_float_for_money, no_box_dyn_error

## Проблемы

- нет, можно проводить

Перед встречей вручную просмотрите находки на ложные срабатывания (reports/check.md): одно ложное срабатывание в начале сессии подрывает доверие.
