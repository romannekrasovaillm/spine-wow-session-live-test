#!/usr/bin/env bash
# Контрактный тест ДКА §4.1 под фактический интерфейс проверяемого репозитория.
# Вызывается Spine Core правилом command_succeeds; рабочий каталог — корень репозитория.
# Скрипт и тесты принадлежат ДКА и лежат вне продукта ($DKA_HOME); репозиторий не изменяется.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(pwd)"
CACHE="${DKA_CARGO_TARGET:-${XDG_CACHE_HOME:-$HOME/.cache}/dka-contract-target}"
command -v cargo >/dev/null || { echo "контракт §4.1: cargo не найден — проверка невозможна"; exit 2; }

if grep -rq 'struct PaymentProcessor' "$REPO/src" 2>/dev/null; then
  VARIANT="API с ключом"; PKG="payments-core"; TEST="contract_keyed.rs"
elif grep -rqE 'fn[[:space:]]+authorize[[:space:]]*\(' "$REPO/src" 2>/dev/null; then
  VARIANT="API без ключа"; PKG="payment-core"; TEST="contract_retry.rs"
else
  echo "контракт §4.1: функция authorize не найдена — не применимо"; exit 0
fi

W="$(mktemp -d)"; mkdir -p "$W/tests"
printf '[package]\nname = "dka_contract_target"\nversion = "0.0.0"\nedition = "2021"\n\n[dependencies]\n%s = { path = "%s" }\n' \
  "$PKG" "$REPO" > "$W/Cargo.toml"
cp "$HERE/$TEST" "$W/tests/contract.rs"

if (cd "$W" && CARGO_TARGET_DIR="$CACHE" cargo test --quiet --test contract >"$W/out.txt" 2>&1); then
  echo "контракт §4.1 (вариант: $VARIANT) выполнен"
  RC=0
else
  reason="$(grep -hoE '(повторный вызов с тем же ключом[^"]*|авторизация записана в журнал дважды|повторная авторизация отклонена[^"]*|разные ключи[^"]*|error\[E[0-9]+\][^\n]*)' "$W/out.txt" | head -2 | tr '\n' ' ')"
  echo "контракт §4.1 (вариант: $VARIANT) НЕ выполнен: ${reason:-см. вывод cargo test}"
  RC=1
fi
rm -rf "$W"
exit "$RC"
