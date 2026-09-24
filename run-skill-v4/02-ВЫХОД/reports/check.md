# Проверка: Стандарт платёжного ядра v2

Spine Core, правил: 7, режим `--no-exec` (команды из правил не исполняются). Гейт FAIL в 0 из 3 репозиториев; находок, ломающих гейт: 0; предупреждений (гейт не ломают): 4.

| Репозиторий | Гейт | Находок |
|---|---|---|
| payments-arm-a | PASS | 3 |
| payments-arm-b | PASS | 0 |
| cards-product | PASS | 1 |

| Репозиторий | Правило | Пункт стандарта | Где | Уровень | Суть |
|---|---|---|---|---|---|
| payments-arm-a | idempotency_contract | Стандарт платёжного ядра §4.1 | /home/roman/spine-bank/кейсы/drift-control/armA-solution:0 | warn | command_succeeds: команда 'bash "$DKA_HOME/contracts/idempotency/run_contract.sh"' завершилась неуспешно (код 1); хвост вывода: контракт §4.1 (вариант: API без  |
| payments-arm-a | thiserror_for_errors | Стандарт платёжного ядра §3.2 | Cargo.toml:0 | warn | must_contain: паттерн 'thiserror' не найден ни в одном файле по glob 'Cargo.toml' |
| payments-arm-a | authorize_idempotent | Стандарт платёжного ядра §4.1 | src/**/*.rs:0 | warn | must_contain: паттерн '[Ii]dempotenc' не найден ни в одном файле по glob 'src/**/*.rs' |
| cards-product | tech_radar_hold | Стандарт платёжного ядра §5.1 | Cargo.toml:10 | warn | deny_dependency: пакет 'left-pad' из deny-списка — основание: Техрадар ДКА, HOLD |

Не проверялось (вне области действия или нет файлов по glob):

| Репозиторий | Правило | Причина |
|---|---|---|
| cards-product | no_float_for_money | вне области: applies_to=['payment-core'] |
| cards-product | thiserror_for_errors | вне области: applies_to=['payment-core'] |
| cards-product | authorize_idempotent | вне области: applies_to=['payment-core'] |
