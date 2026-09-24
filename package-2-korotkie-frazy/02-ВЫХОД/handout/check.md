# Проверка: Стандарт платёжного ядра v2

Spine Core, правил: 9, режим `--no-exec` (команды из правил не исполняются). Находки уровня warn видны, но гейт не ломают (PASS).

| Репозиторий | Гейт | Находок |
|---|---|---|
| payments-arm-a | PASS | 2 |
| payments-arm-b | PASS | 0 |
| cards-product | FAIL | 3 |

| Репозиторий | Правило | Пункт стандарта | Где | Уровень | Суть |
|---|---|---|---|---|---|
| payments-arm-a | errors_via_thiserror | §3.2 Ошибки | **/Cargo.toml:0 | warn | must_contain: паттерн 'thiserror' не найден ни в одном файле по glob '**/Cargo.toml' |
| payments-arm-a | authorize_idempotent | §4.1 Идемпотентность | **/src/**/*.rs:0 | warn | must_contain: паттерн 'idempotenc' не найден ни в одном файле по glob '**/src/**/*.rs' |
| cards-product | errors_via_thiserror | §3.2 Ошибки | **/Cargo.toml:0 | warn | must_contain: паттерн 'thiserror' не найден ни в одном файле по glob '**/Cargo.toml' |
| cards-product | authorize_idempotent | §4.1 Идемпотентность | **/src/**/*.rs:0 | warn | must_contain: паттерн 'idempotenc' не найден ни в одном файле по glob '**/src/**/*.rs' |
| cards-product | tech_radar_hold | §5.1 Техрадар | Cargo.toml:10 | error | deny_dependency: пакет 'left-pad' из deny-списка — основание: Техрадар ДКА, зона HOLD |
