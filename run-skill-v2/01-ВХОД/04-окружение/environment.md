# Окружение и входные данные прогона скилла v2

## Версии

| Компонент | Версия | Примечание |
|---|---|---|
| Qwen Code | 0.24.4 | TUI, две панели: Qwen слева, плашка справа |
| Spine Core (`arch-be`) | 0.3.8 | `control check`, `control report --level corp` |
| Модель | DeepSeek V4 Flash | 1.0M контекст |
| **Python** | **3.12.3** | обязателен: `session.py` v2 не компилируется на 3.9–3.11 |
| PyYAML | 6.0.3 | |
| tmux | 3.4 | |
| Навык | `spine-wow-session` **v2** из архива `spine-wow-session-v2.zip` | копия в `.qwen/skills/` проекта и в `~/.qwen/skills/` |

## Почему Python 3.12

`scripts/session.py` v2 содержит вложенные кавычки внутри f-string (строки 1074–1075):

```python
f"- **Spine прав, LLM ошибся:** {', '.join(f'{c} ({DUEL_NOTES.get(c, '')})' for c in spine_only) or 'нет'}"
```

Такая запись допустима только с Python 3.12+ (PEP 701). В SKILL.md заявлено «Python 3.9+»,
поэтому на 3.9–3.11 скрипт падает с `SyntaxError` ещё до запуска. В прогоне использован
`python3` = `/usr/bin/python3.12` (шим в `PATH` для сессии Qwen Code); сам навык не правился.

## Состояние рабочей папки до первого промпта

| Объект | Состояние |
|---|---|
| `context/session.yaml` | заполнен: стандарт, три репозитория с тегами (`payment-core`, `cards`, `rust`), коридор 3–30, `precision_min: 0.9` |
| `context/standard/payment-core-standard.md` | 11 строк, 5 пунктов |
| `work/requirements.md`, `work/CONSTRAINTS.corp.yaml`, `work/pilot-canvas.md` | шаблоны |
| `work/rules-tests/` | пусто |
| `reports/`, `sandbox/`, `handout/` | пусты |

## Как проводился LLM-прогон дуэли (роль оператора)

Дуэль требует независимого LLM-участника. Порядок был такой:

1. агент выполнил `session.py duel prepare` — создал 12 случаев и `TASK.md`;
2. оператор скопировал `cases/` и `TASK.md` **в отдельный чистый каталог** (без `reports/`,
   `rules.yaml` и `session.py`);
3. в этом каталоге дважды запускался Qwen Code в неинтерактивном режиме
   (`qwen "<задание>" --approval-mode yolo`, отдельные сессии) — ответы записаны в
   `answer-1.json` и `answer-2.json`;
4. оператор положил ответы в `reports/duel-llm-1.json` и `reports/duel-llm-2.json`;
5. агент выполнил `session.py duel score` и построил `reports/duel.md`.

Агент, получив от LLM 12 из 12, сначала расценил это как возможную утечку истины
и запросил подтверждение чистоты прогона — подтверждение дано в реплике 6.
