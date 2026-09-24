#!/usr/bin/env bash
# dka-gate.sh — архитектурный гейт ДКА (шаблон; агент его НЕ генерирует и НЕ правит).
#
# Запускается ТОЛЬКО из checkout репозитория ДКА. Скрипты, лежащие в репозитории
# продукта, не используются: продукт не может «починить» гейт правкой своих файлов.
#
# usage: dka-gate.sh <product_repo> <dka_dir> <product_name> [<base_ref>]
#   <dka_dir>/corp/CONSTRAINTS.corp.yaml   корпоративный слой (владелец ДКА)
#   <dka_dir>/exceptions/<product>.yaml    одобренные исключения (владелец ДКА)
#   <dka_dir>/baselines/<product>.json     baseline долга (необязательно; владелец ДКА)
#   <dka_dir>/contracts/                   контрактные тесты ДКА (command_succeeds, необязательно)
# exit: 0 — зелёный, 1 — красный, 2 — ошибка конфигурации
#
# Команды (command_succeeds) исполняются ТОЛЬКО из корпоративного слоя: эффективный файл
# собирается из реестра ДКА, продукт не может подложить туда свою команду. Правила продукта
# проверяются с --no-exec.
set -uo pipefail

REPO="${1:?product repo}"; DKA="${2:?dka dir}"; PRODUCT="${3:?product name}"; BASE="${4:-origin/main}"
ARCH_BE="${ARCH_BE:-arch-be}"
OUT="${DKA_OUT:-$DKA/out/$PRODUCT}"
mkdir -p "$OUT"
DKA="$(cd "$DKA" && pwd)"; OUT="$(cd "$OUT" && pwd)"
export DKA_HOME="$DKA"

if ! python3 "$DKA/ci/build_effective.py" "$DKA/corp/CONSTRAINTS.corp.yaml" \
     "$DKA/exceptions/$PRODUCT.yaml" "$OUT/effective-corp.yaml" 2>"$OUT/effective.err"; then
  echo "гейт ДКА: КРАСНЫЙ — реестр исключений ДКА некорректен: $(cat "$OUT/effective.err")"
  exit 1
fi

BASELINE=()
[ -f "$DKA/baselines/$PRODUCT.json" ] && BASELINE=(--baseline "$DKA/baselines/$PRODUCT.json")

# 1. Корпоративный слой — по эффективному файлу ДКА, с исполнением контрактов ДКА. Решающая проверка.
"$ARCH_BE" control check "$REPO" --constraints "$OUT/effective-corp.yaml" \
  ${BASELINE[@]+"${BASELINE[@]}"} --json > "$OUT/corp.json" 2>"$OUT/corp.err"
CORP_RC=$?
"$ARCH_BE" control check "$REPO" --constraints "$OUT/effective-corp.yaml" \
  ${BASELINE[@]+"${BASELINE[@]}"} --format junit > "$OUT/corp-junit.xml" 2>/dev/null || true
if [ "$CORP_RC" -gt 1 ]; then
  echo "гейт ДКА: ошибка запуска Spine Core (код $CORP_RC): $(head -c 300 "$OUT/corp.err")"
  exit 2
fi

# 2. Собственные правила продукта — информативно; решающее только их ослабление.
WEAKENED=0
if [ -f "$REPO/CONSTRAINTS.yaml" ] && git -C "$REPO" rev-parse --verify -q "$BASE" >/dev/null; then
  (cd "$REPO" && "$ARCH_BE" control check . --constraints CONSTRAINTS.yaml --no-exec \
     --base "$BASE" --json) > "$OUT/product.json" 2>/dev/null || true
  if python3 - "$OUT/product.json" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception:
    sys.exit(1)
sys.exit(0 if any(i.get("rule") == "rule_weakened" for i in d.get("issues", [])) else 1)
PY
  then WEAKENED=1; fi
fi

if [ "$CORP_RC" -ne 0 ] || [ "$WEAKENED" -ne 0 ]; then
  echo "гейт ДКА: КРАСНЫЙ (корпоративный слой: код $CORP_RC; ослабление правил продукта: $WEAKENED) — $OUT"
  exit 1
fi
echo "гейт ДКА: ЗЕЛЁНЫЙ — $OUT"
exit 0
