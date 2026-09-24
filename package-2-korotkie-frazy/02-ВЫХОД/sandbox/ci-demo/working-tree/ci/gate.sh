#!/usr/bin/env bash
# Единый архитектурный гейт ДКА. Владелец: ДКА.
# Запускается на каждый MR/PR и на main; провал — exit 1 (механически).
#
# Проверяет: вердикт fitness (control check) + неизменность реестра правил
# (rule_weakened) + линтер спайна + delta guard (прямые правки спайна).
#
# Требование к продукту: реестр ДКА лежит ВНУТРИ репозитория
# (.arch-handoff/CONSTRAINTS.yaml). Иначе анти-ослабление невозможно:
# Spine честно ответит «реестр вне репозитория — сравнение невозможно».
set -euo pipefail

REPO="${1:-.}"
ARCH_BE="${ARCH_BE:-arch-be}"
BASE="${DKA_BASE:-origin/main}"
OUT="${DKA_OUT:-gate-artifacts}"
CONSTRAINTS="${DKA_CONSTRAINTS:-.arch-handoff/CONSTRAINTS.yaml}"

mkdir -p "$OUT"

# MR из форка (чужой код): команды из правил не исполняем — модель доверия A3.
NO_EXEC=()
if [ "${DKA_UNTRUSTED:-0}" = "1" ]; then NO_EXEC=(--no-exec); fi

# 1. Артефакт для CI: машинный вывод строго в stdout, exit-код не меняется.
set +e
"$ARCH_BE" gate --repo "$REPO" --constraints "$CONSTRAINTS" --base "$BASE" \
  "${NO_EXEC[@]}" --format junit > "$OUT/gate-junit.xml" 2>"$OUT/gate-junit.err"
RC=$?
set -e

# 2. Паспорт вердикта в лог джобы: что проверено, что заявлено, что не проверено.
"$ARCH_BE" gate --repo "$REPO" --constraints "$CONSTRAINTS" --base "$BASE" \
  "${NO_EXEC[@]}" --explain > "$OUT/verdict-passport.md" 2>/dev/null || true

# 3. Пломба: вердикт относится к ЭТОМУ состоянию дерева (Н3, ADR-043).
#    Позже проверяется так:
#    arch-be gate --repo . --constraints ... --verify-envelope "$OUT/verdict.json"
"$ARCH_BE" gate --repo "$REPO" --constraints "$CONSTRAINTS" --base "$BASE" \
  "${NO_EXEC[@]}" --format json > "$OUT/verdict.json" 2>/dev/null || true

case "$RC" in
  0) echo "гейт: ЗЕЛЁНЫЙ" ;;
  1) echo "гейт: КРАСНЫЙ — см. $OUT/gate-junit.xml и $OUT/verdict-passport.md" ;;
  3) echo "гейт: INCOMPLETE — вердикт неполон, см. паспорт" ;;
  *) echo "гейт: ошибка запуска, код $RC" ;;
esac
exit "$RC"
