# Доступные навыки в Qwen Code

**Запрос оператора:**

Привет. Какие навыки (skills) тебе сейчас доступны в этой рабочей папке? Перечисли их списком и по каждому — одну строку, что он делает. Отдельно скажи, для чего предназначен навык spine-wow-session и какие команды он даёт.

---

<!-- источник: /home/roman/.qwen/projects/-home-roman-spine-wow-live-arch-session/chats/48a5de95-206e-4d05-907c-9d7778006ed0.jsonl -->


### ▶ Запрос оператора 1

Привет. Какие навыки (skills) тебе сейчас доступны в этой рабочей папке? Перечисли их списком и по каждому — одну строку, что он делает. Отдельно скажи, для чего предназначен навык spine-wow-session и какие команды он даёт.

  `read_file(file_path="/home/roman/spine-wow-live/arch-session/.qwen/skills/spine-wow-session/SKILL.md")` · `run_shell_command(command="ls -la /home/roman/spine-wow-live/arch-session/.qwen/skills/ /home/roman/.qwen/skills 2>/dev/null; ls /home/roman/.qwen, description="List skill directories in project and user scope")`

The user asks: which skills are available in this working folder. List them, one line each. Separately explain what spine-wow-session is for and what commands it gives.

Let me check the skill file to describe spine-wow-session accurately, especially "какие команды он даёт".

Let me read the SKILL.md.

I should list the available skills from the system reminder. But also, the question is about skills available "в этой рабочей папке" — bundled + project + user skills. I could check for others.

Let me read the SKILL.md of spine-wow-session to give accurate commands.
Прочитаю SKILL.md навыка spine-wow-session, чтобы точно описать его команды.


The user asks which skills are available in this working folder. Should I list all available skills (bundled + user + project)? The question says "в этой рабочей папке" — available in this working folder. I'll list them all: project skill (spine-wow-session), user skills (vpn-egress), bundled skills.

Let me give a clear list. No need to read others deeply; descriptions come from the system reminder.

Then describe spine-wow-session and its commands (session.py commands — not slash commands, but script subcommands). Note the user asked "какие команды он даёт" — clarify it's not slash-commands; it's the workflow + session.py subcommands.

Let me structure the answer.

Also note: the project skill is at .qwen/skills/spine-wow-session within this folder (and mirrored in user skills dir).

Should I mention /batch etc as slash commands? The bundled skills are invoked via skill tool; some correspond to slash commands (/batch, /review, /simplify, /loop, /stuck, /qc-helper...).

Keep it one line each.

Note also that there are references/ and scripts/ dirs, and a references/commands? Let me just answer. Maybe I should verify whether the project mirror differs from user mirror... not needed.

Also mention that spine-wow-session exists both project-scope and user-scope (duplicate) — that's a useful observation since duplicates could cause confusion. Actually the system reminder listed it as (project). Both exist on disk. I'll mention briefly.

Let me write the answer in Russian.

Commands of the skill: script `session.py` subcommands: init, preflight, check, effective, fleet init/check/bump/repin/report, bypass, selftest, pack. Plus prompt templates P1–P5 (references/prompts.md).

Answer.
## Навыки, доступные в этой папке

**Проектный (`.qwen/skills/`)**

- **spine-wow-session** — подготовка и проведение 90-минутной вау-сессии Spine Core (`arch-be`) для корпоративного архитектора: его стандарт → `requirements.md` → `CONSTRAINTS.corp.yaml` → проверка его репозиториев, демо дрейфа кодового агента, версии корпоративного слоя, отчёт ДКА по флоту, лазейки, надёжность правил, план пилота и раздаточный пакет.

**Пользовательские (`~/.qwen/skills/`)**

- **spine-wow-session** — тот же навык, продублированный в пользовательском скоупе (лежит и в проекте, и в `~/.qwen/skills/`).
- **vpn-egress** — включение/выключение/диагностика локального egress-шлюза VPN (sing-box на `127.0.0.1:12080`), когда LLM API или Telegram отдают региональную блокировку из РФ; TUN и вторую ноду не трогает (моно-нода, ADR-006).

**Встроенные (bundled)**

- **batch** — параллельная пакетная обработка файлов: сам находит файлы, режет на чанки и раздаёт воркерам (`/batch <операция> <маска>`).
- **browser-use** — управление твоим Chrome через persistent Node REPL и Qwen Browser SDK.
- **computer-use** — управление локальными десктоп-приложениями через их UI (когда нет CLI/API/коннектора).
- **dataviz** — гайдлайны по дизайну графиков, дашбордов, карт и любой визуализации данных + локальный валидатор палитры.
- **extension-creator** — создание, настройка, валидация и локальное тестирование расширений Qwen Code (`/extension-creator <путь> [шаблон]`).
- **goal-draft** — превращает расплывчатое «хочу, чтобы…» в objective для `/goal` с бинарными проверками, бюджетом и протоколом блокировки.
- **loop** — запускает промпт сейчас и повторяет по расписанию или через self-paced wakeups (`/loop`, `/loop list`, `/loop clear`).
- **new-app** — рабочий процесс создания нового приложения/сайта/игры/CLI с нуля: требования, стек, скаффолд, реализация, прототип.
- **qc-helper** — ответы по использованию, фичам, конфигурации и траблшутингу Qwen Code + правка `settings.json`.
- **review** — ревью изменённого кода, PR или файлов (`/review <pr|file> [--comment|--fix|--resume] [--effort …]`).
- **simplify** — пост-имплементационный cleanup-проход по свежим изменениям с применением простых улучшений.
- **stuck** — диагностика зависших/тормозящих сессий Qwen Code на этой машине (`/stuck [PID]`).
- **workflow-authoring** — справочник по написанию скриптов Dynamic Workflow (API, `agent()`, `pipeline()` vs `parallel()`, resume, пример).
- **workflow-creator** — создание и обновление переиспользуемых workflow-файлов в `.qwen/workflows`.

## Отдельно про spine-wow-session

**Назначение.** Навык готовит и проводит встречу, на которой корпоративный архитектор впервые видит **свой** стандарт исполняемым на **своём** коде: проверки выполняет Spine Core (`arch-be`), а скрипт `scripts/session.py` готовит входы, вызывает `arch-be` и собирает отчёты. Главная мысль: результат работы архитектора — не только документ, объясняющий стандарт, но и проверка, показывающая, соблюдается ли он. Ключевые принципы — его данные вместо учебного примера, прослеживаемость каждой находки на пункт стандарта (`std_ref`), честный показ лазеек и хрупких правил, минимум два действия архитектора своими руками (промпт P3 и `fleet bump`). Репозитории архитектора не изменяются — всё демо живёт в `sandbox/`; проверки идут с `--no-exec`.

Он активируется не только по слову «Spine»: достаточно просьбы «превратить стандарт/кукбук/architecture.md в проверяемые правила» или «проверить, как репозитории соблюдают корпоративный стандарт».

**Команды.** Отдельных слэш-команд навык не даёт — это не CLI-плагин, а набор шагов и подкоманд скрипта `python3 <skill>/scripts/session.py`:

| Команда | Что делает |
|---|---|
| `init <dir> [--demo SPINE_REPO]` | Рабочая папка из шаблонов (или режим репетиции на демо-данных) |
| `preflight` | Окружение, контекст, коридор находок, правила без находок |
| `check [--rules F] [--top N]` | Проверка репозиториев, таблица со ссылками на пункты стандарта |
| `effective` | Эффективный файл ДКА: правила ДКА + реестр исключений ДКА |
| `fleet init / check / bump / repin / report` | Корпоративный слой с версией, продукты с `extends`, пины версий, отчёт ДКА по флоту |
| `bypass [--repo R] [--rule N]` | Три лазейки и их закрытие эффективным файлом |
| `selftest [--scaffold]` | Надёжность правил на примерах bad/good/bypass |
| `pack` | Раздаточный пакет `handout/` и архив `handout-spine-session.zip` |

Плюс промпт-шаблоны **P1–P5** из `references/prompts.md` (стандарт → требования → правила → тесты надёжности → эксперимент с дрейфом) и сценарий по минутам из `references/scenario.md`. Требуется Python 3.9+ и PyYAML.

Одно замечание: навык продублирован в проекте и в `~/.qwen/skills/` — если он будет правиться, стоит держать копии синхронными, иначе легко потерять изменения.
