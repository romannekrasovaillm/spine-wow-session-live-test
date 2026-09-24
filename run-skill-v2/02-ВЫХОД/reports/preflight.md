# Предполётная проверка сессии

- Spine Core: `arch-be 0.3.8`
- Стандарт: `context/standard/payment-core-standard.md` — есть
- Корпоративные правила: `CONSTRAINTS.corp.yaml` — 6 правил, из них непроверяемых (unverifiable): 1

| Репозиторий | Гейт | error | warn |
|---|---|---|---|
| payments-arm-a | PASS | 0 | 2 |
| payments-arm-b | PASS | 0 | 0 |
| cards-product | PASS | 0 | 1 |

**Всего находок: 3** (целевой коридор для встречи: 3–30)

| Правило | Пункт стандарта | Находок |
|---|---|---|
| thiserror_for_errors | Стандарт платёжного ядра §3.2 | 1 |
| authorize_idempotent | Стандарт платёжного ядра §4.1 | 1 |
| tech_radar_hold | Стандарт платёжного ядра §5.1 | 1 |
| no_float_for_money | Стандарт платёжного ядра §2.1 | 0 |
| tech_radar_renamed | Стандарт платёжного ядра §5.1 | 0 |
| observability_standard | Стандарт платёжного ядра §6.1 | 0 |

Правила без находок (проверьте, не сломаны ли они — selftest): no_float_for_money, tech_radar_renamed

Пропущено по области действия или из-за пустого набора файлов (не находка и не ложное срабатывание):

| Репозиторий | Правило | Причина |
|---|---|---|
| cards-product | no_float_for_money | вне области: applies_to=['payment-core'] |
| cards-product | thiserror_for_errors | вне области: applies_to=['payment-core'] |
| cards-product | authorize_idempotent | вне области: applies_to=['payment-core'] |

## Проблемы

- нет, можно проводить

Перед встречей вручную просмотрите находки на ложные срабатывания (reports/check.md): одно ложное срабатывание в начале сессии подрывает доверие.
