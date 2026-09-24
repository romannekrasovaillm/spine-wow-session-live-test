# Окружение и входные данные прогона скилла v3

## Версии

| Компонент | Версия | Примечание |
|---|---|---|
| Qwen Code | 0.24.4 | TUI, две панели: Qwen слева, плашка справа |
| Spine Core (`arch-be`) | 0.3.8 | `control check`, `control report --level corp` |
| Модель | DeepSeek V4 Flash | 1.0M контекст |
| **Python** | **3.11.8** | v3 работает на 3.9+: вложенные кавычки в f-string убраны, проверено на 3.11 и 3.12 |
| PyYAML | 6.0.3 | |
| tmux | 3.4 | |
| Навык | `spine-wow-session` **v3** из архива `spine-wow-session-v3.zip` | копия в `.qwen/skills/` проекта и в `~/.qwen/skills/` |

Отдельная проверка совместимости, которой не было в v2:

```bash
python3.11 -c "import ast; ast.parse(open('scripts/session.py').read())"   # OK
python3.12 -c "import ast; ast.parse(open('scripts/session.py').read())"   # OK
```

## Состояние рабочей папки до первого промпта

| Объект | Состояние |
|---|---|
| `context/session.yaml` | заполнен: стандарт, три репозитория с тегами (`payment-core`, `cards`, `rust`), коридор 3–30, `precision_min: 0.9` |
| `context/standard/payment-core-standard.md` | 11 строк, 5 пунктов |
| `work/requirements.md`, `work/CONSTRAINTS.corp.yaml`, `work/pilot-canvas.md` | шаблоны |
| `work/rules-tests/` | пусто |
| `reports/`, `sandbox/`, `handout/` | пусты |

## Как проводились LLM-прогоны дуэли (роль оператора)

1. Агент выполнил `session.py duel prepare` — создал 16 случаев, `spine-rules.yaml` и два набора:
   `sandbox/duel/kit-llm/` (случаи, стандарт, реестр исключений, `TASK.md`) и
   `sandbox/duel/kit-combo/` (то же + `spine-findings.json` и `spine-rules.yaml`).
2. Оператор скопировал каждый набор **в отдельный чистый каталог** (`~/spine-wow-live/duel-v3/…`),
   где нет ни истины, ни отчётов, ни `session.py`.
3. В каждом каталоге Qwen Code запускался неинтерактивно по три раза (отдельные сессии):
   `qwen "<задание>" --approval-mode yolo`; ответы сохранены как `answer.json`.
4. Оператор положил ответы в `reports/duel/`: `llm-1…3.json` (чистая LLM) и
   `combo-1…3.json` (LLM + находки Spine Core).
5. Агент выполнил `session.py duel score` и построил `reports/duel.md`.

Ответы LLM как есть — в `03-ДОКАЗАТЕЛЬСТВА/llm-answers/`.
