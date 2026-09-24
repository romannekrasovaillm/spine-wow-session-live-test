#!/usr/bin/env bash
# Запуск контрактного теста ДКА §4.1. Вызывается Spine Core через command_succeeds в корне
# проверяемого репозитория. Скрипт и тест принадлежат ДКА и лежат вне продукта ($DKA_HOME).
#
# Для каждого крейта, где объявлена authorize, исходники копируются во временный крейт
# с манифестом ДКА, к ним добавляется контрактный тест, выполняется cargo test.
# Репозиторий продукта не изменяется. Нужен cargo; сборочный кэш общий для всех прогонов.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE="${DKA_CARGO_TARGET:-${XDG_CACHE_HOME:-$HOME/.cache}/dka-contract-target}"
command -v cargo >/dev/null || { echo "контракт §4.1: cargo не найден — проверка невозможна"; exit 2; }

mapfile -t ROOTS < <(grep -rlE --include='*.rs' --exclude-dir=target --exclude-dir=.git \
    'fn[[:space:]]+authorize[[:space:]]*\(' . 2>/dev/null | sed -E 's#^\./##' \
    | grep -E '(^|/)src/' | sed -E 's#(^|/)src/.*$#\1#' | sort -u)
if [ "${#ROOTS[@]}" -eq 0 ]; then
  echo "контракт §4.1: функция authorize не найдена — не применимо"; exit 0
fi

FAIL=0
for r in "${ROOTS[@]}"; do
  root="${r%/}"; [ -z "$root" ] && root="."
  W="$(mktemp -d)"; mkdir -p "$W/tests"
  cp -r "$root/src" "$W/src"
  DEPS=""
  grep -rq "rust_decimal" "$W/src" && DEPS='rust_decimal = "1"'
  printf '[package]\nname = "dka_contract_target"\nversion = "0.0.0"\nedition = "2021"\n\n[dependencies]\n%s\n' \
    "$DEPS" > "$W/Cargo.toml"
  cp "$HERE/contract_test.rs" "$W/tests/contract.rs"
  if ! (cd "$W" && CARGO_TARGET_DIR="$CACHE" cargo test --quiet --test contract >"$W/out.txt" 2>&1); then
    reason="$(grep -hoE "(повторный вызов с тем же ключом[^\"]*|разные ключи[^\"]*|error\[E[0-9]+\][^\n]*)" "$W/out.txt" | head -2 | tr '\n' ' ')"
    echo "контракт §4.1 НЕ выполнен в ${root}: ${reason:-см. вывод cargo test}"
    FAIL=1
  else
    echo "контракт §4.1 выполнен в ${root}"
  fi
  rm -rf "$W"
done
exit "$FAIL"
