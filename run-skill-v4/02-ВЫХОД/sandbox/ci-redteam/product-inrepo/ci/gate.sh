#!/usr/bin/env bash
# Гейт «как в прогоне Qwen Code»: реестр ДКА и скрипт гейта лежат В РЕПОЗИТОРИИ ПРОДУКТА.
"$ARCH_BE" control check . --constraints .arch-handoff/CONSTRAINTS.yaml --no-exec --base main >/dev/null 2>&1
