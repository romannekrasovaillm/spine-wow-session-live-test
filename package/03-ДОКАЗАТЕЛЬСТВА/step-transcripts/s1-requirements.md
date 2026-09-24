# Стандарт → требования (P1)

**Запрос оператора:**

Мы готовим вау-сессию Spine Core для архитектора домена «Платежи». Рабочая папка сессии — эта папка: контекст в context/session.yaml, экспорт моего стандарта — context/standard/payment-core-standard.md, три моих репозитория перечислены в session.yaml. Действуй по навыку spine-wow-session, этап подготовки, шаг 1: разбери стандарт на атомарные требования и заполни work/requirements.md — ID, формулировка, пункт стандарта, класс проверяемости A/B/C, способ проверки, будущее имя правила. Ничего не добавляй сверх текста стандарта. В конце перечисли, сколько требований в каждом классе, и отметь неоднозначные формулировки, если они есть.

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


### ▶ Запрос оператора 2

Мы готовим вау-сессию Spine Core для архитектора домена «Платежи». Рабочая папка сессии — эта папка: контекст в context/session.yaml, экспорт моего стандарта — context/standard/payment-core-standard.md, три моих репозитория перечислены в session.yaml. Действуй по навыку spine-wow-session, этап подготовки, шаг 1: разбери стандарт на атомарные требования и заполни work/requirements.md — ID, формулировка, пункт стандарта, класс проверяемости A/B/C, способ проверки, будущее имя правила. Ничего не добавляй сверх текста стандарта. В конце перечисли, сколько требований в каждом классе, и отметь неоднозначные формулировки, если они есть.

  `skill(skill="spine-wow-session")`

The user wants me to act per the skill spine-wow-session, preparation stage, step 1. I should invoke the skill tool per instructions ("When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action"). Let me invoke the skill.

Then read context/session.yaml, context/standard/payment-core-standard.md, and existing work/requirements.md, plus references/prompts.md (P1).

Let me start with the skill tool.

  `read_file(file_path="/home/roman/spine-wow-live/arch-session/context/session.yaml")` · `read_file(file_path="/home/roman/spine-wow-live/arch-session/context/standard/payment-core-standard.md")` · `read_file(file_path="/home/roman/spine-wow-live/arch-session/work/requirements.md")`

Now read the context files: context/session.yaml, context/standard/payment-core-standard.md, existing work/requirements.md, and references/prompts.md (P1) and references/rules.md maybe.

Let me read them in parallel.

  `run_shell_command(command="ls -R /home/roman/spine-wow-live/arch-session/.qwen/skills/spine-wow-session/references /home/roman/spine-wow-live/arch, description="List skill references and scripts")` · `read_file(file_path="/home/roman/spine-wow-live/arch-session/work/CONSTRAINTS.corp.yaml")`

Now let me look at references/prompts.md (P1) and references/rules.md to follow conventions for rule names. Also check the existing work/CONSTRAINTS.corp.yaml and session.py to understand naming.

Let me read the references dir.

  `read_file(file_path="/home/roman/spine-wow-live/arch-session/.qwen/skills/spine-wow-session/references/prompts.md")` · `read_file(file_path="/home/roman/spine-wow-live/arch-session/.qwen/skills/spine-wow-session/references/rules.md")`

Now read references/prompts.md (P1) and references/rules.md to align rule names/types.

  `write_file(file_path="/home/roman/spine-wow-live/arch-session/work/requirements.md", content="# Требования стандарта: Стандарт платёжного ядра v2\n\nИсточник: Confluence (демо-экспорт для живого теста), файл `cont)`

Now I have everything. The standard has 5 sections:

2.1 Денежные суммы — не хранятся в float. Class A (pattern check, must_not_contain f32/f64). Rule name: no_float_money.
3.2 Ошибки — типизированно (thiserror); anyhow и Box<dyn Error> запрещены. Class A: deny_dependency anyhow + must_not_contain Box<dyn Error>. Could split into two atomic requirements? The instruction says "разбери стандарт на атомарные требования". Section 3.2 contains two prohibitions: (a) errors typed via thiserror, (b) anyhow and Box<dyn Error> forbidden. Are these atomic? "Ошибки домена описываются типизированно (thiserror)" and "anyhow и Box<dyn Error> запрещены". Hmm "anyhow and Box<dyn Error> forbidden" - two different mechanisms but same rule. I'd split into: R-02 errors typed thiserror (B/A?), R-03 no anyhow (A: deny_dependency), R-04 no Box<dyn Error> (A: must_not_contain).

Actually "не добавляй требований, которых нет в тексте" — splitting is fine as long as it's within text. But over-splitting could be considered adding. Let me think: atomic decomposition is the goal. The 3.2 has arguably 2-3 atoms. I'll split into 2: typed errors (thiserror) and prohibition of anyhow/Box<dyn Error>. Hmm, but "anyhow and Box<dyn Error>" — both are "untyped error" escape hatches; one rule could cover both but the rule types differ (deny_dependency vs must_not_contain). For the "будущее имя правила" column, having distinct rule names is useful. I think splitting into R-03 (no anyhow) and R-04 (no Box<dyn Error>) is legitimate and gives better traceability. But is it "adding"? No — both are explicitly named in the text as forbidden.

Hmm, but maybe better to keep 3.2 as one requirement with two rule names? The template has one "Правило" column per requirement. Since rules map 1:1 to constraints, and anyhow is deny_dependency while Box<dyn Error> is must_not_contain, splitting is cleaner. I'll split but note the split in the ambiguous/notes section.

4.1 Идемпотентность — авторизация платежа идемпотентна по ключу. Class B or C? It's behavioral: needs a test. "B — нужен тест или анализ структуры кода". Class B: command_succeeds test (in pilot outside --no-exec). Rule name: payment_auth_idempotent. Ambiguous: "по ключу" — какой ключ? idempotency key header? TTL? Also "идемпотентна по ключу" — не указан источник ключа, срок хранения. Mark ambiguous.

5.1 Техрадар — библиотеки из зоны HOLD (anyhow, left-pad) не используются. Class A: deny_dependency. Note overlap with 3.2 (anyhow). Rule name: tech_radar_hold. Ambiguity: список HOLD приведён в скобках как примеры — полный список? Mark ambiguous (only two example libs named, the radar is external).

6.1 Наблюдаемость — каждый сервис публикует метрики по стандарту наблюдаемости. Class C (only human) — no, could be A/B via must_contain? The standard referenced (страдарт наблюдаемости) is external and not provided. Realistically: C — unverifiable, owner. But hmm, it could be B — check presence of metrics endpoint / dependency. But "публикует метрики по стандарту" — requires the observability standard which isn't in the export. So class C with note. Rule: unverifiable: true, name observability_standard, owner @dka-observability.

2.1 float money: Class A. Pattern `\bf(32|64)\b` in Rust files. Rule name: no_float_money. Ambiguity: which languages? standard says "типы с плавающей точкой" — for Rust f32/f64, but also f64 in other langs. Not necessarily ambiguous; but "Денежные суммы" scope — attribute vs all f64 (e.g., rate). That's ambiguity: use f64 for percentages okay? Mark ambiguous.

Now the ID naming: R-01..R-06.

Let me count: 
- R-01 2.1 no_float_money — A
- R-02 3.2 typed errors via thiserror — B? Check: "ошибки домена описываются типизированно (thiserror)" — verifying thiserror presence = deny/require dependency? must_contain thiserror in Cargo.toml — that's A-ish but weak. Actually structural analysis: B. Hmm. Let me classify: A — checks automatically by code/deps/config. "Ошибки типизированны через thiserror" can be approximated by must_contain `thiserror` in Cargo.toml — automatic but weak. I'd call it B (нужен анализ структуры кода — использование derive Error) or A with must_contain. The rules.md says must_contain is low reliability (bypassed by comment). I'll mark class B: частично — нужен анализ структуры (наличие derive Error на enum домена).

Hmm, but honest classification: the concrete check is presence of thiserror as dependency + derive usage. I'd say B.

- R-03 3.2 no anyhow — A (deny_dependency)
- R-04 3.2 no Box<dyn Error> — A (must_not_contain). Actually must_not_contain is "A" — automatic by code pattern. Yes A.
- R-05 4.1 idempotency — B (needs test)
- R-06 5.1 tech radar — A (deny_dependency)
- R-07 6.1 observability — C

That's 7 requirements? Let's recount: R-01, R-02, R-03, R-04, R-05, R-06, R-07 = 7. Classes: A: R-01, R-03, R-04, R-06 = 4; B: R-02, R-05 = 2; C: R-07 = 1.

Hmm, is splitting 3.2 into 3 requirements (typed, no anyhow, no Box) adding requirements? The prompt P1 says atomic requirements. The standard's 3.2 explicitly names three things: thiserror typed, anyhow forbidden, Box<dyn Error> forbidden. I'll present as 3 atoms with a note that they come from one paragraph 3.2.

Now I need to write work/requirements.md following the template. The template header:

```
# Требования стандарта: <название>

Источник: <ссылка на Confluence>. Сгенерировано агентом, проверено архитектором: <да/нет>.

Классы проверяемости:
- **A** — ...
```

I should keep the template's class legend and fill in. Should I preserve exact template? Yes, mirror it.

Source: standard title "Стандарт платёжного ядра v2", source_url "Confluence (демо-экспорт для живого теста)". checked by architect: нет (not yet).

Let me also check the requirement IDs used in skill examples: R-01, R-__, P3 says "возьми требование R-__ из work/requirements.md". Good.

Rule names should be snake_case as in rules.md (tech_radar_hold). Note the existing CONSTRAINTS.corp.yaml already has C-DKA-001 tech_radar_hold with deny [log4j-core] — that's a placeholder from init, will be replaced in step 2. My rule name for 5.1 tech_radar_hold matches. Good.

Note: 5.1 says HOLD libraries (anyhow, left-pad) — the deny list. And 3.2 also forbids anyhow. So anyhow appears in two rules. Note it.

Also note: the existing C-DKA-001 uses log4j-core which is NOT in the standard — that's a leftover; in step 2 it'll be regenerated. I could mention, but not required. Maybe mention briefly as a heads-up.

Now, "Не добавляй требований, которых нет в тексте." So I must not invent e.g. "no secrets", "PII", etc. Good.

Ambiguous formulations to flag:
1. §2.1 — «денежные суммы» без указания, к каким типам/языкам относится (f32/f64 в Rust? BigDecimal в Java?); неясно, допустим ли f64 для не-денежных величин (курсы, проценты) — риск ложных срабатываний.
2. §4.1 — «идемпотентна по ключу»: не указан источник ключа (заголовок Idempotency-Key?), область действия (ключ + операция?), срок хранения ключа/окно повторной отправки, поведение при конфликте (тот же ответ vs 409). Без этого правило проверяемо только на уровне «есть тест», и то по договорённости.
3. §5.1 — список HOLD дан в скобках как примеры (anyhow, left-pad); неясно, полный ли он и где актуальный техрадар (ссылки нет) — правило можно сгенерировать только по этим двум именам.
4. §6.1 — «по стандарту наблюдаемости» ссылается на внешний документ, которого нет в экспорте: что именно считать метриками (RED/USE, обязательные метки), не определён.
5. §3.2 — «ошибки домена» — граница домена не определена (какие модули считать доменом); «типизированно (thiserror)» — не сказано, требуется ли thiserror именно как библиотека или любой типизированный enum.
6. §3.2 vs §5.1 — anyhow фигурирует в обоих пунктах: одна и та же библиотека запрещена по двум причинам; нужно решить, будут ли это два правила (двойные находки) или одно.

Also §2.1: "не хранятся" — хранение vs передача/вычисления. Maybe fold in.

Now write the file. I'll use write_file with the full content.

Table columns: ID | Требование | Пункт стандарта | Класс | Как проверить | Правило

Let me draft rows.

R-01 | Денежные суммы не хранятся в типах с плавающей точкой | §2.1 Денежные суммы | A | Поиск float-типов (`\bf(32|64)\b`) в исходниках денежной логики; в перспективе — `must_not_contain` | no_float_money
R-02 | Ошибки домена описываются типизированно (thiserror) | §3.2 Ошибки | B | Структурный анализ: `thiserror` в манифесте + `#[derive(Error)]` на enum'ах ошибок домена (не только упоминание слова) | domain_errors_typed
R-03 | `anyhow` не используется | §3.2 Ошибки | A | Отсутствие `anyhow` в манифестах (`deny_dependency`) | no_anyhow
R-04 | `Box<dyn Error>` не используется | §3.2 Ошибки | A | Поиск `Box<dyn Error>` в исходниках (`must_not_contain`, с учётом `(?m)` и оговоркой про Box<dyn Error + Send/Sync) | no_box_dyn_error
R-05 | Авторизация платежа идемпотентна по ключу | §4.1 Идемпотентность | B | Поведенческий тест повторной авторизации с тем же ключом (один результат, повторный запрос не создаёт вторую авторизацию) — `command_succeeds` в пилоте, вне `--no-exec`. Неоднозначно: ключ, окно, поведение при конфликте | payment_auth_idempotent
R-06 | Библиотеки из зоны HOLD техрадара не используются (в стандарте названы `anyhow`, `left-pad`) | §5.1 Техрадар | A | Отсутствие названных HOLD-библиотек в манифестах (`deny_dependency`). Неоднозначно: список HOLD неполон/без ссылки | tech_radar_hold
R-07 | Каждый сервис публикует метрики по стандарту наблюдаемости | §6.1 Наблюдаемость | C | Только человеком: сверить с внешним стандартом наблюдаемости (в экспорте отсутствует); до уточнения — `unverifiable: true` с owner | observability_standard

Counts: A=4 (R-01,R-03,R-04,R-06), B=2 (R-02,R-05), C=1 (R-07). Total 7.

Wait: R-04 `Box<dyn Error>` — the grep pattern needs to handle `Box<dyn std::error::Error>` and `Box<dyn Error + Send + Sync>`. Note it.

Now write file. Header: "# Требования стандарта: Стандарт платёжного ядра v2".

Should I keep "проверено архитектором: нет"? Yes.

I'll write it. Then reply with summary and ambiguities.

Let me construct the file content carefully.
Контекст и стандарт прочитал, шаблон P1 и шпаргалку по правилам тоже. Заполняю `work/requirements.md`.


Verify file content quickly (optional). I'll just report.

Report: 7 requirements, classes: A=4, B=2, C=1. Ambiguities listed.

Also mention two heads-ups: existing CONSTRAINTS.corp.yaml C-DKA-001 has log4j-core, not from this standard — will be regenerated in step 2. And anyhow overlap decision needed before step 2.

Keep concise.
`work/requirements.md` заполнен из текста стандарта — 7 атомарных требований, ничего сверх экспорта не добавлено.

**Разбивка по классам**

| Класс | Кол-во | Требования |
|---|---|---|
| A — автоматически по коду/зависимостям | 4 | R-01 (float-деньги), R-03 (`no_anyhow`), R-04 (`no_box_dyn_error`), R-06 (`tech_radar_hold`) |
| B — тест или анализ структуры | 2 | R-02 (типизированные ошибки через `thiserror`), R-05 (идемпотентность авторизации) |
| C — только человеком | 1 | R-07 (метрики по стандарту наблюдаемости) |
| **Итого** | **7** | |

Пункт §3.2 разложен на три требования (типизация + два запрета: `anyhow`, `Box<dyn Error>`), потому что проверяются они разными типами правил (`deny_dependency` vs `must_not_contain`); в таблице это отражено через `Правило`.

**Неоднозначные формулировки (6)**

1. **§2.1** — «денежные суммы» не ограничены ни языком, ни типами, и не разграничены с не-денежными расчётами (`f64` для курсов и процентов) → риск ложных срабатываний.
2. **§4.1** — «идемпотентна по ключу»: не определены источник ключа, область действия, окно хранения и поведение при повторной отправке.
3. **§5.1** — список зоны HOLD дан примерами (`anyhow`, `left-pad`) без ссылки на сам техрадар.
4. **§6.1** — «по стандарту наблюдаемости» ссылается на документ, которого нет в экспорте → класс C, а не A.
5. **§3.2** — не определена граница «домена» и не сказано, обязателен ли именно `thiserror` или достаточно типизированного enum.
6. **§3.2 ↔ §5.1** — `anyhow` запрещён двумя пунктами; нужно решить, будет ли это двумя правилами (двойные находки) или одним с двумя `std_ref`. Это решение стоит принять до шага 2, иначе возможны дубли в отчёте на встрече.

Замечание по шагу 2: в текущем `work/CONSTRAINTS.corp.yaml` лежит заготовка из `init` — `C-DKA-001 tech_radar_hold` с `deny: [log4j-core]`. `log4j-core` в тексте стандарта не упоминается, так что при генерации по P2 этот список нужно заменить на `anyhow`/`left-pad` (по R-06) — иначе в `check` пойдут находки не из стандарта архитектора.

Дальше по навыку — шаг 2: требования класса A → `CONSTRAINTS.corp.yaml`. Сказать, когда генерировать?
