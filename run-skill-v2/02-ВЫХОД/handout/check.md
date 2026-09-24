# Проверка: Стандарт платёжного ядра v2

Spine Core, правил: 6, режим `--no-exec` (команды из правил не исполняются). Находки уровня warn видны, но гейт не ломают (PASS).

| Репозиторий | Гейт | Находок |
|---|---|---|
| payments-arm-a | PASS | 2 |
| payments-arm-b | PASS | 0 |
| cards-product | PASS | 1 |

| Репозиторий | Правило | Пункт стандарта | Где | Уровень | Суть |
|---|---|---|---|---|---|
| payments-arm-a | thiserror_for_errors | Стандарт платёжного ядра §3.2 | Cargo.toml:0 | warn | must_contain: паттерн 'thiserror' не найден ни в одном файле по glob 'Cargo.toml' |
| payments-arm-a | authorize_idempotent | Стандарт платёжного ядра §4.1 | src/**/*.rs:0 | warn | must_contain: паттерн '[Ii]dempotenc' не найден ни в одном файле по glob 'src/**/*.rs' |
| cards-product | tech_radar_hold | Стандарт платёжного ядра §5.1 | Cargo.toml:10 | warn | deny_dependency: пакет 'left-pad' из deny-списка — основание: Техрадар ДКА, HOLD |

Не проверялось (вне области действия или нет файлов по glob):

| Репозиторий | Правило | Причина |
|---|---|---|
| cards-product | no_float_for_money | вне области: applies_to=['payment-core'] |
| cards-product | thiserror_for_errors | вне области: applies_to=['payment-core'] |
| cards-product | authorize_idempotent | вне области: applies_to=['payment-core'] |
