# Проверка: Стандарт платёжного ядра v2

Spine Core, правил: 6, режим `--no-exec` (команды из правил не исполняются). Находки уровня warn видны, но гейт не ломают (PASS).

| Репозиторий | Гейт | Находок |
|---|---|---|
| payments-arm-a | PASS | 2 |
| payments-arm-b | PASS | 0 |
| cards-product | PASS | 1 |

| Репозиторий | Правило | Пункт стандарта | Где | Уровень | Суть |
|---|---|---|---|---|---|
| payments-arm-a | thiserror_for_errors | Стандарт платёжного ядра v2 §3.2 | src/error.rs:50 | warn | must_not_contain: запрещённый паттерн '(?m)^\s*impl\s+(?:std::error::Error\|std::fmt::Display\|fmt::Display\|Error)\s+for\s+\w*Error\b': impl fmt::Display for P |
| payments-arm-a | thiserror_for_errors | Стандарт платёжного ядра v2 §3.2 | src/error.rs:78 | warn | must_not_contain: запрещённый паттерн '(?m)^\s*impl\s+(?:std::error::Error\|std::fmt::Display\|fmt::Display\|Error)\s+for\s+\w*Error\b': impl std::error::Error  |
| cards-product | tech_radar_hold | Стандарт платёжного ядра v2 §5.1 | Cargo.toml:10 | warn | deny_dependency: пакет 'left-pad' из deny-списка — основание: Стандарт платёжного ядра v2 §5.1 (зона HOLD) |
