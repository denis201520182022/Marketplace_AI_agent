# 🗺️ ROADMAP — План поэтапной реализации

> Этот документ — **главный навигатор разработки и трекер прогресса**.
> Каждый этап и каждая задача строго согласованы с [docs/SPECIFICATION.md](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md).
> Любой разработчик или ИИ-агент должен идти **строго последовательно**, открывать гиперссылки на соответствующие разделы спецификации, выполнять задачу, отмечать чекбокс `[x]` и проверять критерии приёмки (Definition of Done).

---

## 📊 Сводный статус этапов

| Этап | Название этапа | Раздел спецификации | Статус |
|------|----------------|---------------------|--------|
| **Этап 1** | [Инфраструктурный фундамент, База данных и Сетевой прокси](#этап-1--инфраструктурный-фундамент-база-данных-и-сетевой-прокси) | [§2.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема), [§2.2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#22-сетевая-топология-и-поддержка-прокси-hybrid--sovereign-modes), [§9](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql), [§10](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | ⬜ Не начат |
| **Этап 2** | [Омниканальный бот, Админ-консоль и Служба заботы](#этап-2--омниканальный-бот-админ-консоль-и-служба-заботы-telegram--max) | [§3.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#31-принцип-унификации), [§3.2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [§3.3](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console), [§3.4](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#34-модуль-технической-поддержки-two-way-helpdesk-relay), [§3.5](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#35-стандарты-uiux-button-first-и-отказ-от-слэш-команд) | ⬜ Не начат |
| **Этап 3** | [База знаний (Knowledge Base) и Интерактивное управление](#этап-3--база-знаний-knowledge-base-и-интерактивное-управление) | [§3.2.4](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [§5.3](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#53-база-знаний-и-rag-стратегия), [§9](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql) | ⬜ Не начат |
| **Этап 4** | [Система коннекторов маркетплейсов и Симулятор (WB, Ozon, Mock)](#этап-4--система-коннекторов-маркетплейсов-и-симулятор-wb-ozon-mock) | [§3.6](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#36-селективная-обработка-товаров-product-scope-filter), [§4.1–§4.7](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#4-система-коннекторов-маркетплейсов-pluggable-connector-architecture), [§12.1.6](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#6-отзыв-на-товар-вне-белого-списка-product-scope-whitelist) | ⬜ Не начат |
| **Этап 5** | [ИИ-агент (LangGraph + OpenAI) и Human-in-the-loop](#этап-5--ии-агент-langgraph--openai-и-human-in-the-loop) | [§3.2.5](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [§5.1–§5.3](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#5-ии-ядро-и-langgraph-state-machine), [§7.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#71-двойной-учёт-токенов-redundancy), [§12.2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#122-приёмочные-критерии-bdd-acceptance-criteria-given-when-then) | ⬜ Не начат |
| **Этап 6** | [Очереди, Воркеры, Идемпотентность и Защита от гонок](#этап-6--очереди-воркеры-идемпотентность-и-защита-от-гонок) | [§2.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема), [§6.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq), [§12.1.2–§12.1.4](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#121-обработка-пограничных-сценариев-edge-cases) | ⬜ Не начат |
| **Этап 7** | [Биллинг (ЮKassa), Тарифная сетка и Контроль квот](#этап-7--биллинг-юkassa-тарифная-сетка-и-контроль-квот) | [§1.2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#12-ключевые-бизнес-цели-mvp), [§3.2.6](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [§7.1–§7.2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#7-учёт-ресурсов-токенов-и-биллинг), [§12.1.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#1-исчерпание-лимита-ответов-во-время-активного-потока-quota-depletion) | ⬜ Не начат |
| **Этап 8** | [Командная работа, Делегирование и Служба заботы](#этап-8--командная-работа-делегирование-и-служба-заботы) | [§3.4](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#34-модуль-технической-поддержки-two-way-helpdesk-relay), [§3.7](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#37-командная-работа-делегирование-сотрудникам-и-групповые-рабочие-чаты), [§9](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql), [§12.1.5](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#5-отзыв-инвайта-или-увольнение-менеджера) | ⬜ Не начат |
| **Этап 9** | [Мобильная админ-панель владельца и Пульт тестирования](#этап-9--мобильная-админ-панель-владельца-и-пульт-тестирования) | [§3.3](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console), [§4.7](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#47-встроенный-режим-симулятора-mock-marketplace-connector--sandbox-mode) | ⬜ Не начат |
| **Этап 10** | [Модуль продуктовой AI-аналитики и Авто-дайджест](#этап-10--модуль-продуктовой-ai-аналитики-и-авто-дайджест) | [§3.2.7](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [§3.8](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#38-модуль-ai-аналитики-отзывов-и-стратегических-рекомендаций-селлеру) | ⬜ Не начат |
| **Этап 11** | [Мониторинг, Логирование и Алертинг (Prometheus/Grafana/Loki)](#этап-11--мониторинг-логирование-и-алертинг) | [§2.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема), [§8.1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | ⬜ Не начат |
| **Этап 12** | [Финальное сквозное тестирование (E2E), Стресс-тест и Релиз](#этап-12--финальное-сквозное-тестирование-e2e-стресс-тест-и-релиз) | [§10](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture), [§11](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#11-поэтапный-план-реализации-roadmap), [§12.2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#122-приёмочные-критерии-bdd-acceptance-criteria-given-when-then) | ⬜ Не начат |

---

## Этап 1 — Инфраструктурный фундамент, База данных и Сетевой прокси

**Цель:** Развернуть базовую инфраструктуру проекта. Локальное окружение поднимается одной командой `docker compose up`. База данных инициализируется через Alembic. Все 11 таблиц созданы. Реализован и протестирован модуль AES-256-GCM шифрования токенов. Приложение отвечает на health-check.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 1.1 | Сформировать `pyproject.toml` со всеми зависимостями (FastAPI, uvicorn, aiogram 3, aio-pika, sqlalchemy[asyncio], alembic, asyncpg, pydantic-settings, langchain, langgraph, langfuse, cryptography, prometheus-client, httpx, pdfplumber, python-docx, openpyxl, redis, pytest, pytest-asyncio) | [pyproject.toml](file:///d:/actual_projects/AI_for_salers/pyproject.toml) | [§10 Структура проекта](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | [ ] |
| 1.2 | Описать `docker-compose.yml`: PostgreSQL 16, Redis 7, RabbitMQ 3.13 (management + delayed_message_exchange плагин), Qdrant, Prometheus, Grafana, Loki, Promtail | [docker-compose.yml](file:///d:/actual_projects/AI_for_salers/docker-compose.yml) | [§2.1 C4-схема](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема), [§8.1 Observability](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 1.3 | Реализовать `config/settings.py` на базе `pydantic-settings`: валидация подключения к Postgres, Redis, RabbitMQ, секретный ключ AES-256, токены ботов, флаг `USE_PROXY`, URL прокси JustHost, админские ID | [config/settings.py](file:///d:/actual_projects/AI_for_salers/config/settings.py) | [§2.2 Сетевая топология](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#22-сетевая-топология-и-поддержка-прокси-hybrid--sovereign-modes), [§4.6 Безопасность ключей](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#46-безопасность-api-ключей) | [ ] |
| 1.4 | Оформить `.env.example` с полным описанием всех переменных окружения, дефолтных значений и инструкций по заполнению | [.env.example](file:///d:/actual_projects/AI_for_salers/.env.example) | [§2.2 Режимы системы](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#22-сетевая-топология-и-поддержка-прокси-hybrid--sovereign-modes) | [ ] |
| 1.5 | Реализовать `config/logging.py`: структурированное JSON-логирование для Loki с метками `service`, `seller_id`, `event_id` | [config/logging.py](file:///d:/actual_projects/AI_for_salers/config/logging.py) | [§8.1 Loki-логирование](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 1.6 | Настроить `src/database/session.py`: асинхронный движок SQLAlchemy 2.0 `create_async_engine`, фабрику сессий `async_sessionmaker` и зависимость `get_db` | [src/database/session.py](file:///d:/actual_projects/AI_for_salers/src/database/session.py) | [§10 База данных](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | [ ] |
| 1.7 | Создать ORM-модели для всех 11 сущностей базы данных: `User`, `SellerAccount`, `StoreMembers`, `StoreProductsScope`, `KnowledgeBaseDoc`, `ReviewQuestion`, `Subscription`, `Payment`, `EventAuditLog`, `SupportTicket`, `SupportMessage` со всеми связями, индексами и типами (строковые GUID для MAX, bigint для TG) | [src/database/models/](file:///d:/actual_projects/AI_for_salers/src/database/models/) | [§9 Схема БД PostgreSQL](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql) | [ ] |
| 1.8 | Создать базовый generic репозиторий `src/database/repositories/base.py` с CRUD-методами | [src/database/repositories/base.py](file:///d:/actual_projects/AI_for_salers/src/database/repositories/base.py) | [§10 Clean Architecture](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | [ ] |
| 1.9 | Настроить `alembic/env.py` для асинхронной работы с метаданными моделей SQLAlchemy | [alembic/env.py](file:///d:/actual_projects/AI_for_salers/alembic/env.py) | [§10 Alembic](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | [ ] |
| 1.10 | Сгенерировать и применить первоначальную миграцию Alembic, создающую все 11 таблиц схемы БД | [alembic/versions/](file:///d:/actual_projects/AI_for_salers/alembic/versions/) | [§9 Схема БД PostgreSQL](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql) | [ ] |
| 1.11 | Реализовать модуль `src/common/crypto.py`: алгоритм AES-256-GCM (`cryptography`) для симметричного шифрования/дешифрования JSON credentials селлера и маскирования в логах (`wb_token_***abc`) | [src/common/crypto.py](file:///d:/actual_projects/AI_for_salers/src/common/crypto.py) | [§4.4 Гибкие credentials](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#44-хранение-параметров-авторизации-гибкие-credentials), [§4.6 Безопасность ключей](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#46-безопасность-api-ключей) | [ ] |
| 1.12 | Реализовать `src/common/metrics.py`: базовые счётчики и гистограммы Prometheus (`reviews_processed_total`, `llm_request_duration_seconds`, `rabbitmq_queue_depth`) | [src/common/metrics.py](file:///d:/actual_projects/AI_for_salers/src/common/metrics.py) | [§8.1 Стек Observability](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 1.13 | Реализовать `src/main.py`: точка входа FastAPI с lifespan (проверка соединений к Postgres, Redis, RMQ при старте и graceful shutdown) | [src/main.py](file:///d:/actual_projects/AI_for_salers/src/main.py) | [§2.1 C4-схема](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема) | [ ] |
| 1.14 | Реализовать роутер `src/api/routers/health.py`: эндпоинты `GET /health` (liveness probe) и `GET /ready` (readiness probe с проверкой пинга БД, Redis и RabbitMQ) | [src/api/routers/health.py](file:///d:/actual_projects/AI_for_salers/src/api/routers/health.py) | [§10 API эндпоинты](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | [ ] |
| 1.15 | Подготовить конфиг Squid и скрипт настройки forward-proxy: `deploy/proxy/squid.conf` и `deploy/proxy/setup_proxy.sh` для зарубежного VPS | [deploy/proxy/](file:///d:/actual_projects/AI_for_salers/deploy/proxy/) | [§2.2 Сетевая топология](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#22-сетевая-топология-и-поддержка-прокси-hybrid--sovereign-modes) | [ ] |
| 1.16 | Написать юнит-тесты на модуль шифрования: проверка корректности `decrypt(encrypt(text)) == text`, обработка неверного мастер-ключа, валидация маскирования | [tests/unit/test_crypto.py](file:///d:/actual_projects/AI_for_salers/tests/unit/) | [§4.6 Безопасность ключей](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#46-безопасность-api-ключей) | [ ] |

### Definition of Done (Критерии завершения Этапа 1)
- [ ] Контейнеры поднимаются командой `docker compose up -d` без ошибок.
- [ ] Команда `alembic upgrade head` успешно накатывает полную схему со всеми 11 таблицами.
- [ ] Запрос `curl http://localhost:8000/health` возвращает `{"status": "ok"}`.
- [ ] Запрос `curl http://localhost:8000/ready` подтверждает доступность PostgreSQL, Redis и RabbitMQ.
- [ ] Тесты `pytest tests/unit/test_crypto.py` проходят зелёным.

---

## Этап 2 — Омниканальный бот, Админ-консоль и Служба заботы (Telegram + MAX)

**Цель:** Создать работающий омниканальный слой ботов (Telegram + VK MAX) с 100% реализацией принципа **Button-First** (ноль слэш-команд для обычных пользователей). Реализовать онбординг, подключение кабинетов WB/Ozon, переключение режимов работы, мобильную админ-консоль владельца (`/admin`) и двухсторонний шлюз техподдержки.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 2.1 | Разработать ядро абстракций `src/bot/core/`: унифицированные типы `BotMessage`, `BotKeyboard`, `BotCallback`, исключающие привязку к библиотекам мессенджеров | [src/bot/core/](file:///d:/actual_projects/AI_for_salers/src/bot/core/) | [§3.1 Принцип унификации](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#31-принцип-унификации) | [ ] |
| 2.2 | Реализовать фабрику клавиатур `src/bot/core/keyboards.py`: постоянное нижнее меню (Reply Keyboard: 6 кнопок) и инлайн-карточки со стандартными кнопками `[ 🔙 Назад ]` и `[ 🏠 В главное меню ]` | [src/bot/core/keyboards.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/keyboards.py) | [§3.5 Стандарты UI/UX: Button-First](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#35-стандарты-uiux-button-first-и-отказ-от-слэш-команд) | [ ] |
| 2.3 | Реализовать `src/bot/telegram/bot.py` на `aiogram 3`: поддержка вебхуков и polling, роутинг исходящих запросов через прокси при флаге `USE_PROXY=true` | [src/bot/telegram/bot.py](file:///d:/actual_projects/AI_for_salers/src/bot/telegram/bot.py) | [§2.2 Сетевая топология](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#22-сетевая-топология-и-поддержка-прокси-hybrid--sovereign-modes), [§3.1 Принцип унификации](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#31-принцип-унификации) | [ ] |
| 2.4 | Реализовать `src/bot/max/bot.py` на базе официального MAX Bot API (`platform-api2.max.ru`): асинхронный HTTP-клиент `httpx` с прямой работой из РФ контура | [src/bot/max/bot.py](file:///d:/actual_projects/AI_for_salers/src/bot/max/bot.py) | [§2.2 Сетевая топология](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#22-сетевая-топология-и-поддержка-прокси-hybrid--sovereign-modes), [§3.1 Принцип унификации](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#31-принцип-унификации) | [ ] |
| 2.5 | Реализовать сценарий онбординга: обработка команды запуска, автоматическая регистрация в таблице `users` (привязка `telegram_id` или `max_id`), выдача постоянной Reply-клавиатуры | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.1 Онбординг](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 2.6 | Реализовать раздел `[ 🏢 Мои кабинеты ]`: вывод списка ЛК селлера, карточка конкретного ЛК, действия «Пауза», «Снять с паузы», «Переименовать», «Удалить» | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.2 Управление ЛК](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 2.7 | Реализовать мастер подключения нового ЛК: выбор площадки (WB, Ozon, Mock), вывод интерактивной подсказки, ввод ключей, проверка «на лету» пробным запросом и сохранение зашифрованных credentials в `seller_accounts` | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.2 Управление ЛК](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [docs/seller_onboarding_guide.md](file:///d:/actual_projects/AI_for_salers/docs/seller_onboarding_guide.md) | [ ] |
| 2.8 | Реализовать раздел `[ 🤖 Режим работы ]`: тумблер переключения режимов «Автономный режим» (Full Auto) vs «Всегда с подтверждением» (Copilot) с обновлением поля `mode` в БД | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.3 Режимы работы](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 2.9 | Реализовать модуль `src/bot/admin/`: закрытая консоль администратора (`/admin`): проверка `ADMIN_TELEGRAM_IDS`/`ADMIN_MAX_IDS`, живой дашборд статистики, принудительный Kill-Switch селлеров, ручная корректировка баланса (+50, +100 ответов) | [src/bot/admin/](file:///d:/actual_projects/AI_for_salers/src/bot/admin/) | [§3.3 Мобильная админ-панель](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console) | [ ] |
| 2.10 | Реализовать двухсторонний саппорт-шлюз `src/support/`: приём вопросов через кнопку `[ 💬 Поддержка ]`, сохранение тикета в `support_tickets`, мгновенный пуш Денису с контекстом и доставка ответа селлеру через нативный Reply | [src/support/](file:///d:/actual_projects/AI_for_salers/src/support/) | [§3.4 Двухсторонний Helpdesk Relay](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#34-модуль-технической-поддержки-two-way-helpdesk-relay), [§12.2 Сценарий 4](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-4-двухсторонний-тикет-в-службу-поддержки) | [ ] |
| 2.11 | Покрыть сценарии онбординга, валидации токенов и тикетов саппорта юнит-тестами | [tests/unit/](file:///d:/actual_projects/AI_for_salers/tests/unit/) | [§10 Clean Architecture](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | [ ] |

### Definition of Done (Критерии завершения Этапа 2)
- [ ] Telegram-бот запускается, принимает команду `/start` и выводит постоянное нижнее меню из 6 кнопок.
- [ ] MAX-бот подключается к тестовому аккаунту и корректно отвечает на входящие вебхуки/сообщения.
- [ ] Пользователь может подключить тестовый/боевой ЛК, ключи шифруются в базе данных.
- [ ] Денис может вызвать `/admin` и видеть карточку живого дашборда; для обычных пользователей команда заблокирована.
- [ ] Сообщение селлера в техподдержку прилетает Денису, а ответ через Reply возвращается селлеру в чат бота.

---

## Этап 3 — База знаний (Knowledge Base) и Интерактивное управление

**Цель:** Реализовать подсистему работы с документами селлера: парсинг файлов (`.txt`, `.pdf`, `.docx`, `.xlsx`, `.csv`), хранение контента в PostgreSQL, настройку Tone of Voice и алгоритм сборки системного промпта (`PromptBuilder`) с бесшовной передачей контекста в LLM.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 3.1 | Реализовать модуль парсеров `src/ai_agent/knowledge_base/parser.py`: извлечение текста из `.txt`, `.pdf` (`pdfplumber`), `.docx` (`python-docx`), `.xlsx`/`.csv` (`openpyxl`) с очисткой спецсимволов | [src/ai_agent/knowledge_base/parser.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/knowledge_base/parser.py) | [§3.2.4 Управление БЗ](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [§5.3 RAG-стратегия](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#53-база-знаний-и-rag-стратегия) | [ ] |
| 3.2 | Реализовать репозиторий `KnowledgeBaseRepository` для работы с таблицей `knowledge_base_docs`: сохранение контента, версионирование, каскадное удаление документов при удалении ЛК | [src/database/repositories/](file:///d:/actual_projects/AI_for_salers/src/database/repositories/) | [§9 Схема БД](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql) | [ ] |
| 3.3 | Реализовать сборщик контекста `src/ai_agent/knowledge_base/prompt_builder.py`: форматирование блоков `[FAQ]`, `[Характеристики и гарантия]`, `[Правила возврата]`, склейка с карточкой товара и правилами Tone of Voice | [src/ai_agent/knowledge_base/prompt_builder.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/knowledge_base/prompt_builder.py) | [§5.3 Context Prompting](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#53-база-знаний-и-rag-стратегия) | [ ] |
| 3.4 | Реализовать пользовательский интерфейс в боте по кнопке `[ 📚 База знаний ]`: просмотр загруженных файлов, приём новых документов прямо в чат, удаление, ввод быстрых ответов текстом | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.4 Управление БЗ](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 3.5 | Реализовать интерфейс настройки Tone of Voice: выбор предустановок («Вежливый и тёплый», «Строгий деловой», «С эмодзи» / «Без эмодзи») с сохранением в метаданные ЛК | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.4 Tone of Voice](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 3.6 | Написать юнит-тесты на парсеры документов всех форматов и генерацию промпта через `PromptBuilder` | [tests/unit/test_kb.py](file:///d:/actual_projects/AI_for_salers/tests/unit/) | [§5.3 RAG-стратегия](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#53-база-знаний-и-rag-стратегия) | [ ] |

### Definition of Done (Критерии завершения Этапа 3)
- [ ] Селлер отправляет PDF или DOCX файл в бот — система парсит документ и сохраняет чистый текст в `knowledge_base_docs`.
- [ ] Селлер может просмотреть список файлов и удалить ненужный документ через инлайн-кнопки.
- [ ] `PromptBuilder` собирает системный промпт с корректными маркерами секций и установленным Tone of Voice.
- [ ] Все тесты парсинга файлов проходят без ошибок.

---

## Этап 4 — Система коннекторов маркетплейсов и Симулятор (WB, Ozon, Mock)

**Цель:** Создать расширяемую pluggable-систему коннекторов маркетплейсов. Реализовать официальные клиенты WB и Ozon API с защитой от блокировок по Rate Limits, селективный фильтр артикулов (Scope Mode) и полноценный локальный симулятор `MockMarketplaceConnector` для 100% автономной разработки без боевых ключей.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 4.1 | Реализовать абстрактный базовый класс `src/marketplaces/base_connector.py` (`validate_credentials`, `poll_new_events`, `fetch_live_product_context`, `publish_answer`) | [src/marketplaces/base_connector.py](file:///d:/actual_projects/AI_for_salers/src/marketplaces/base_connector.py) | [§4.2 Спецификация BaseMarketplaceConnector](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#42-спецификация-интерфейса-basemarketplaceconnector) | [ ] |
| 4.2 | Реализовать динамический реестр `src/marketplaces/registry.py` (паттерн Pluggable Registry): регистрация коннекторов по `platform_id` и фабричный метод `get_connector` | [src/marketplaces/registry.py](file:///d:/actual_projects/AI_for_salers/src/marketplaces/registry.py) | [§4.1 Архитектурный паттерн коннекторов](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#41-архитектурный-паттерн-коннекторов) | [ ] |
| 4.3 | Реализовать унифицированные DTO `src/marketplaces/schemas.py`: `InboundEventDTO` (с pros, cons, buyer_name), `LiveProductContextDTO`, `PublishResultDTO` | [src/marketplaces/schemas.py](file:///d:/actual_projects/AI_for_salers/src/marketplaces/schemas.py) | [§4.3 Унифицированные структуры DTO](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#43-унифицированные-структуры-данных-dto) | [ ] |
| 4.4 | Реализовать коннектор Wildberries `src/marketplaces/wb/`: интеграция с Feedbacks API (неотвеченные отзывы, ответ), Questions API (вопросы, ответ), Content No-Cache API (живая карточка товара по `nmId`) | [src/marketplaces/wb/](file:///d:/actual_projects/AI_for_salers/src/marketplaces/wb/) | [§4.1–§4.5](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#4-система-коннекторов-маркетплейсов-pluggable-connector-architecture), [docs/wb_api.md](file:///d:/actual_projects/AI_for_salers/docs/wb_api.md) | [ ] |
| 4.5 | Реализовать коннектор Ozon `src/marketplaces/ozon/`: интеграция с Reviews API v2 (неотвеченные отзывы, ответ), Questions API (вопросы, ответ), Attributes API (актуальные характеристики товара по `SKU`) | [src/marketplaces/ozon/](file:///d:/actual_projects/AI_for_salers/src/marketplaces/ozon/) | [§4.1–§4.5](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#4-система-коннекторов-маркетплейсов-pluggable-connector-architecture), [docs/ozon_api.md](file:///d:/actual_projects/AI_for_salers/docs/ozon_api.md) | [ ] |
| 4.6 | Реализовать `MockMarketplaceConnector` (`src/marketplaces/mock/`): виртуальный каталог на 5 категорий товаров, генератор синтетических событий (5★ авто, 1★ негатив с браком, вопрос с данными в БЗ, вопрос без данных, эмуляция сбоя HTTP 500) и виртуальную публикацию в таблицу `mock_published_answers` | [src/marketplaces/mock/](file:///d:/actual_projects/AI_for_salers/src/marketplaces/mock/) | [§4.7 Встроенный режим симулятора Mock](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#47-встроенный-режим-симулятора-mock-marketplace-connector--sandbox-mode) | [ ] |
| 4.7 | Реализовать распределённый Rate Limiter `src/marketplaces/rate_limiter.py` на базе Redis (Token Bucket + семафоры на токен и глобальный IP) | [src/marketplaces/rate_limiter.py](file:///d:/actual_projects/AI_for_salers/src/marketplaces/rate_limiter.py) | [§4.5 Поллер и Rate Limiting](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#45-распределённый-поллер-и-rate-limiting) | [ ] |
| 4.8 | Реализовать логику Product Scope Filter: проверка режима охвата товаров магазина («Все товары», «Белый список / Whitelist», «Чёрный список / Blacklist»). При несовпадении артикула событие помечается `ignored_out_of_scope`, LLM не вызывается, баланс селлера не списывается | [src/marketplaces/](file:///d:/actual_projects/AI_for_salers/src/marketplaces/) | [§3.6 Селективная обработка товаров](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#36-селективная-обработка-товаров-product-scope-filter), [§12.1.6 Edge Case: Whitelist](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#6-отзыв-на-товар-вне-белого-списка-product-scope-whitelist) | [ ] |
| 4.9 | Реализовать сценарий управления охватом артикулов в боте: массовый ввод артикулов сообщением через запятую, валидация по каталогу маркетплейса и сохранение в `store_products_scope` | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.6 Интерфейс настройки товаров](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#36-селективная-обработка-товаров-product-scope-filter) | [ ] |
| 4.10 | Написать юнит-тесты на коннекторы: валидация ключей, парсинг входящих DTO, фильтрация по Whitelist, эмуляция задержек Rate Limiter | [tests/unit/test_connectors.py](file:///d:/actual_projects/AI_for_salers/tests/unit/) | [§4.1–§4.7](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#4-система-коннекторов-маркетплейсов-pluggable-connector-architecture) | [ ] |

### Definition of Done (Критерии завершения Этапа 4)
- [ ] `MockMarketplaceConnector` генерирует реалистичные синтетические отзывы и вопросы всех 5 типов без внешних вызовов к маркетплейсам.
- [ ] Фильтр артикулов игнорирует события на товары вне белого списка со статусом `ignored_out_of_scope`.
- [ ] Валидация ключей WB и Ozon корректно распознаёт ошибки прав доступа (`401/403`) и информирует селлера.
- [ ] Rate Limiter блокирует превышение частоты запросов к API маркетплейсов.

---

## Этап 5 — ИИ-агент (LangGraph + OpenAI) и Human-in-the-loop

**Цель:** Собрать интеллектуальное ядро системы на базе LangGraph. Реализовать граф обработки событий: классификацию тональности, запрос живой карточки товара, интеграцию базы знаний, проверку guardrails, автопубликацию позитива и эскалацию негатива селлеру через интерактивную карточку в боте (Human-in-the-loop) с полным аудитом токенов в Langfuse.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 5.1 | Реализовать универсальный интерфейс LLM-провайдера `src/ai_agent/llm_provider/base.py` с поддержкой стриминга, структурированного вывода и метрик | [src/ai_agent/llm_provider/base.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/llm_provider/base.py) | [§5.1 Универсальный LLM-интерфейс](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#51-универсальный-llm-интерфейс) | [ ] |
| 5.2 | Реализовать клиент OpenAI `src/ai_agent/llm_provider/openai_client.py` (`gpt-4o-mini`) с маршрутизацией запросов через forward-прокси (JustHost) при `USE_PROXY=true` | [src/ai_agent/llm_provider/openai_client.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/llm_provider/openai_client.py) | [§2.2 Сетевая топология](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#22-сетевая-топология-и-поддержка-прокси-hybrid--sovereign-modes), [§5.1 Провайдеры LLM](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#51-универсальный-llm-интерфейс) | [ ] |
| 5.3 | Описать состояние графа `src/ai_agent/graph/state.py`: структуры `EventProcessingState` (входящее событие, контекст карточки, фрагменты БЗ, тональность, черновик ответа, флаги эскалации, статус) | [src/ai_agent/graph/state.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/graph/state.py) | [§5.2 Граф обработки LangGraph](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#52-граф-обработки-события-langgraph-workflow) | [ ] |
| 5.4 | Реализовать ноды графа `src/ai_agent/graph/nodes.py`: `fetch_live_context`, `classify_and_evaluate` (проверка рейтинга и тональности), `generate_draft_answer`, `safety_guardrails`, `decide_routing` | [src/ai_agent/graph/nodes.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/graph/nodes.py) | [§5.2 Граф обработки LangGraph](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#52-граф-обработки-события-langgraph-workflow) | [ ] |
| 5.5 | Собрать воркфлоу `src/ai_agent/graph/workflow.py`: компиляция StateGraph с условными переходами (позитив + автопилот → публикация; негатив 1–3★ ИЛИ режим Copilot ИЛИ нехватка данных → эскалация в бот) | [src/ai_agent/graph/workflow.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/graph/workflow.py) | [§5.2 Схема переходов LangGraph](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#52-граф-обработки-события-langgraph-workflow) | [ ] |
| 5.6 | Реализовать валидатор безопасности `src/ai_agent/guardrails.py`: проверка сгенерированного ответа на галлюцинации цен, стоп-слова, контакты вне площадки, ненормативную лексику | [src/ai_agent/guardrails.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/guardrails.py) | [§5.2 Safety Guardrails](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#52-граф-обработки-события-langgraph-workflow) | [ ] |
| 5.7 | Подключить трейсинг Langfuse: логирование каждого вызова LLM с параметрами `trace_id`, `seller_id`, токенами prompt/completion, latency и стоимостью | [src/ai_agent/graph/nodes.py](file:///d:/actual_projects/AI_for_salers/src/ai_agent/graph/nodes.py) | [§7.1 Langfuse трейсинг](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#71-двойной-учёт-токенов-redundancy) | [ ] |
| 5.8 | Реализовать карточку согласования Human-in-the-loop в боте: отправка отзыва с форматированием (товар, покупатель, оценка, текст, ответ ИИ) и 4 кнопками: `[ ✅ Одобрить и отправить ]`, `[ ✏️ Редактировать ответ ]`, `[ 🔄 Сгенерировать заново ]`, `[ ✍️ Ответить вручную ]` | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.5 Карточка события](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота), [§12.2 Сценарий 2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-2-эскалация-негативного-отзыва-13-человеку) | [ ] |
| 5.9 | Реализовать обработчики действий по карточке согласования: Одобрение → отправка публикатору; Редактирование → ожидание нового текста; Регенерация → повторная отправка в ИИ-ядро; Вручную → сохранение ручного текста | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.5 Действия по карточке](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 5.10 | Написать интеграционные E2E-тесты на симуляторе `MockMarketplaceConnector`: прогон позитивного отзыва 5★ в режиме Auto и негативного 1★ в режиме Copilot | [tests/e2e/test_ai_agent.py](file:///d:/actual_projects/AI_for_salers/tests/e2e/) | [§12.2 BDD Приёмочные сценарии](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#122-приёмочные-критерии-bdd-acceptance-criteria-given-when-then) | [ ] |

### Definition of Done (Критерии завершения Этапа 5)
- [ ] При поступлении 5★ отзыва в режиме Auto ответ генерируется с учётом карточки и автоматически отправляется в маркетплейс ([BDD Сценарий 1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-1-автономный-ответ-на-5-отзыв-при-активной-подписке)).
- [ ] При поступлении негативного отзыва (1–3★) генерация переходит в статус `waiting_approval`, селлеру в бот прилетает интерактивная карточка ([BDD Сценарий 2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-2-эскалация-негативного-отзыва-13-человеку)).
- [ ] Нажатие кнопки `[ ✅ Одобрить ]` переводит статус в `published` и публикует ответ.
- [ ] Токены, модель и время ответа фиксируются в Langfuse и в таблице `event_audit_log`.

---

## Этап 6 — Очереди, Воркеры, Идемпотентность и Защита от гонок

**Цель:** Перевести систему на промышленную шину очередей RabbitMQ. Настроить топологию exchanges, очереди с Dead-Letter Exchange (DLX), реализовать распределенные асинхронные воркеры на чистом RabbitMQ (`aio-pika`), внедрить двухуровневую клиентскую идемпотентность (Redis Lease Lock + PostgreSQL status) и защиту от одновременных кликов менеджеров в групповых чатах.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 6.1 | Реализовать модуль очередей `src/workers/rabbitmq_bus.py`: автоматическая инициализация Exchanges (`events.inbound`, `ai.processing`, `events.escalation`, `marketplace.publish`, `events.dlx`), очередей с Manual ACKs и Delayed Message плагином | [src/workers/rabbitmq_bus.py](file:///d:/actual_projects/AI_for_salers/src/workers/rabbitmq_bus.py) | [§2.1 Схема очередей](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема), [§6.1 Надежность RabbitMQ](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq) | [ ] |
| 6.2 | Реализовать `PollerWorker` (`src/workers/poller_worker.py`): опрос активных магазинов по расписанию с учетом Token Bucket Rate Limiter, фильтрация Whitelist и публикация событий в `events.inbound` | [src/workers/poller_worker.py](file:///d:/actual_projects/AI_for_salers/src/workers/poller_worker.py) | [§4.5 Распределённый поллер](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#45-распределённый-поллер-и-rate-limiting) | [ ] |
| 6.3 | Реализовать `AIWorker` (`src/workers/ai_worker.py`): потребление задач из `ai.processing`, запуск LangGraph State Machine, маршрутизация в `events.escalation` или `marketplace.publish` | [src/workers/ai_worker.py](file:///d:/actual_projects/AI_for_salers/src/workers/ai_worker.py) | [§2.1 C4-схема воркеров](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема) | [ ] |
| 6.4 | Реализовать `PublisherWorker` (`src/workers/publisher_worker.py`): потребление задач из `marketplace.publish`, проверка статуса отзыва на площадке (проверка не был ли дан ответ вручную в браузере), вызов `publish_answer` и подтверждение `basic_ack` | [src/workers/publisher_worker.py](file:///d:/actual_projects/AI_for_salers/src/workers/publisher_worker.py) | [§6.1 Manual ACKs](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq), [§12.1.3 Ручной ответ](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#3-отзыв-уже-отвечен-селлером-вручную-в-личном-кабинете-маркетплейса) | [ ] |
| 6.5 | Внедрить двухуровневый алгоритм идемпотентности: краткосрочный Redis Lease Lock `SET idempotency_lock:{key} NX EX 120` при начале работы воркера + сверка статуса в PostgreSQL (`published` / `rejected` → сброс задачи как дубликата) + финальный маркер на 7 дней | [src/workers/ai_worker.py](file:///d:/actual_projects/AI_for_salers/src/workers/ai_worker.py), [src/workers/publisher_worker.py](file:///d:/actual_projects/AI_for_salers/src/workers/publisher_worker.py) | [§6.1 Двухуровневая дедупликация](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq), [§12.2 Сценарий 3](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-3-защита-от-дубликатов-при-сбое-сети) | [ ] |
| 6.6 | Реализовать защиту от гонок в групповых чатах (Race Condition Guard): распределенный мьютекс `SET action_lock:{event_id} {user_id} NX EX 10` при клике кнопок согласования несколькими сотрудниками | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§6.1 Race Condition Guard](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq), [§12.1.4 Одновременный клик менеджеров](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#4-одновременный-клик-двух-менеджеров-в-групповом-чате-race-condition) | [ ] |
| 6.7 | Реализовать Dead-Letter Exchange (DLX) и экспоненциальный retry (Retry Backoff: 1м, 5м, 15м, 1ч, 4ч до 5 попыток). При исчерпании попыток — выставление статуса `error` и пуш-алерт Денису в Telegram и MAX | [src/workers/rabbitmq_bus.py](file:///d:/actual_projects/AI_for_salers/src/workers/rabbitmq_bus.py) | [§6.1 DLX и ретраи](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq), [§12.1.2 Ошибки API](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#2-временная-недоступность-api-маркетплейса-http-500--502--503--504--429) | [ ] |
| 6.8 | Реализовать `SchedulerWorker` (`src/workers/scheduler.py`): запуск регламентных задач (проверка истекающих подписок, сброс агрегатов токенов в БД, очистка устаревших блокировок) | [src/workers/scheduler.py](file:///d:/actual_projects/AI_for_salers/src/workers/scheduler.py) | [§2.1 Воркеры C4](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#21-концептуальная-c4-схема), [§7.2 Subscription Sentinel](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#72-биллинг-и-юkassa) | [ ] |
| 6.9 | Написать интеграционные тесты очередей: эмуляция сетевого сбоя при отправке ACK, проверка отсутствия повторной публикации при дубликатах сообщений | [tests/integration/test_queues.py](file:///d:/actual_projects/AI_for_salers/tests/integration/) | [§12.2 BDD Сценарий 3](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-3-защита-от-дубликатов-при-сбое-сети) | [ ] |

### Definition of Done (Критерии завершения Этапа 6)
- [ ] Одно и то же входящее событие, отправленное в очередь дважды, публикуется в маркетплейс строго один раз.
- [ ] При падении воркера во время генерации задача возвращается в очередь и корректно подхватывается другим воркером после истечения Lease Lock (120 с).
- [ ] Одновременный клик двух менеджеров в группе приводит к обработке первым и дружелюбному алерту для второго.
- [ ] Ошибки `500` маркетплейса отправляются в DLX с возрастающей задержкой.

---

## Этап 7 — Биллинг (ЮKassa), Тарифная сетка и Контроль квот

**Цель:** Реализовать подсистему монетизации на базе ЮKassa API v3: генерацию платёжных ссылок для СБП и банковских карт РФ, транзакционную обработку вебхуков без рекуррентов, поддержку 3-уровневой сетки тарифов («Старт» 990 ₽, «Бизнес» 2 490 ₽, «Профи» 4 990 ₽), несгораемых пакетов ответов и автоматическое управление квотами селлеров.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 7.1 | Реализовать клиент ЮKassa `src/billing/yookassa_client.py`: методы `create_payment` (генерация ссылки на оплату СБП/карта для самозанятого) и `get_payment_info` | [src/billing/yookassa_client.py](file:///d:/actual_projects/AI_for_salers/src/billing/yookassa_client.py) | [§7.2 Схема оплаты ЮKassa](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#72-биллинг-и-юkassa), [docs/economics_and_budget.md](file:///d:/actual_projects/AI_for_salers/docs/economics_and_budget.md) | [ ] |
| 7.2 | Реализовать сервис управления биллингом `src/billing/service.py`: логика тарифных планов («Старт» 990 ₽ / 150 ответов, «Бизнес» 2 490 ₽ / 500 ответов, «Профи» 4 990 ₽ / 1 500 ответов) и несгораемых пакетов ответов (+100 за 490 ₽, +300 за 1 190 ₽, +1 000 за 2 990 ₽) | [src/billing/service.py](file:///d:/actual_projects/AI_for_salers/src/billing/service.py) | [§1.2 Монетизация](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#12-ключевые-бизнес-цели-mvp), [§7.2 Тарифная сетка](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#72-биллинг-и-юkassa) | [ ] |
| 7.3 | Реализовать вебхук-обработчик `src/api/routers/billing_webhook.py`: проверка белого списка IP-адресов ЮKassa, валидация цифровой подписи, транзакционное начисление баланса в `subscriptions` и запись в `payments` | [src/api/routers/billing_webhook.py](file:///d:/actual_projects/AI_for_salers/src/api/routers/billing_webhook.py) | [§7.2 Вебхуки ЮKassa](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#72-биллинг-и-юkassa) | [ ] |
| 7.4 | Реализовать обработку исчерпания квоты ответов: при `responses_used >= responses_limit` новые события получают статус `out_of_quota`, селлеру отправляется уведомление с кнопкой быстрой докупки, а после оплаты задачи автоматически поднимаются в очередь генерации | [src/billing/service.py](file:///d:/actual_projects/AI_for_salers/src/billing/service.py), [src/workers/ai_worker.py](file:///d:/actual_projects/AI_for_salers/src/workers/ai_worker.py) | [§7.2 Лимиты ответов](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#72-биллинг-и-юkassa), [§12.1.1 Edge Case: Исчерпание квоты](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#1-исчерпание-лимита-ответов-во-время-активного-потока-quota-depletion) | [ ] |
| 7.5 | Реализовать меню `[ 💳 Тариф и баланс ]` в боте: отображение остатка ответов, даты окончания подписки, выбор тарифа и генерация кнопки на оплату | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.6 Биллинг в боте](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 7.6 | Реализовать планировщик подписок `Subscription Sentinel`: рассылка предупреждений об истечении подписки за 3 дня, 1 день и в день завершения; временная приостановка поллинга при неоплате | [src/workers/scheduler.py](file:///d:/actual_projects/AI_for_salers/src/workers/scheduler.py) | [§7.2 Subscription Sentinel](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#72-биллинг-и-юkassa) | [ ] |
| 7.7 | Реализовать резервный аудит токенов: атомарный инкремент в Redis (`seller:{id}:tokens:total`, `seller:{id}:responses:used`) и периодический сброс агрегатов в таблицу `token_usage_audit` | [src/billing/service.py](file:///d:/actual_projects/AI_for_salers/src/billing/service.py) | [§7.1 Резервный учёт токенов](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#71-двойной-учёт-токенов-redundancy) | [ ] |
| 7.8 | Покрыть логику биллинга юнит- и интеграционными тестами (успешная оплата, повторный вебхук, исчерпание лимита) | [tests/unit/test_billing.py](file:///d:/actual_projects/AI_for_salers/tests/unit/) | [§7.2 Биллинг](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#72-биллинг-и-юkassa) | [ ] |

### Definition of Done (Критерии завершения Этапа 7)
- [ ] Селлер в боте нажимает покупку тарифа/пакета → получает платёжную ссылку ЮKassa.
- [ ] Тестовый вебхук ЮKassa (`payment.succeeded`) увеличивает баланс ответов селлера в единой транзакции БД.
- [ ] Повторный вебхук с тем же `payment_id` игнорируется без двойного начисления.
- [ ] При нулевом балансе событие получает статус `out_of_quota`, а после оплаты автоматически уходит в публикацию.

---

## Этап 8 — Командная работа, Делегирование и Служба заботы

**Цель:** Обеспечить командную работу для селлеров с сотрудниками: персональное делегирование менеджеру по одноразовым deep-link ссылкам, подключение общих рабочих групповых чатов Telegram/MAX для согласования отзывов, обработку увольнения менеджеров и полную маршрутизацию тикетов в службу заботы Дениса.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 8.1 | Реализовать генерацию одноразовых инвайт-ссылок `https://t.me/SellerBot?start=invite_<token>` с записью в `store_members` (`status="pending"`, `role="manager"`, `expires_at`) | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.7.1 Персональное делегирование](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#37-командная-работа-делегирование-сотрудникам-и-групповые-рабочие-чаты), [§9 STORE_MEMBERS](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql) | [ ] |
| 8.2 | Реализовать обработку перехода менеджера по инвайт-ссылке: привязка `user_id` менеджера к магазину, статус `accepted`, блокировка доступа к API-ключам и биллингу владельца | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.7.1 Безопасность прав](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#37-командная-работа-делегирование-сотрудникам-и-групповые-рабочие-чаты) | [ ] |
| 8.3 | Реализовать подключение командных групповых чатов Telegram/MAX: добавление бота в группу, привязка через команду/кнопку и сохранение `notification_target_type="group_chat"`, `notification_target_id` и `notification_platform` | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.7.2 Подключение группового чата](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#37-командная-работа-делегирование-сотрудникам-и-групповые-рабочие-чаты) | [ ] |
| 8.4 | Реализовать маршрутизацию отправки карточек событий: проверка целевого адреса (`user` vs `group_chat`, Telegram vs MAX) при эскалации задачи из очереди `events.escalation` | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.7.2 Маршрутизация](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#37-командная-работа-делегирование-сотрудникам-и-групповые-рабочие-чаты) | [ ] |
| 8.5 | Реализовать сценарий отзыва инвайта / увольнения менеджера: перевод статуса в `revoked`, блокировка действий в боте и автоматический возврат уведомлений в личный чат владельца | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§12.1.5 Edge Case: Увольнение менеджера](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#5-отзыв-инвайта-или-увольнение-менеджера) | [ ] |
| 8.6 | Расширить службу заботы `src/support/`: поддержка вложений (фото брака, накладные), привязка тикета к магазину селлера и сохранение всей истории в `support_messages` | [src/support/](file:///d:/actual_projects/AI_for_salers/src/support/) | [§3.4 Модуль техподдержки](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#34-модуль-технической-поддержки-two-way-helpdesk-relay), [§9 SUPPORT_MESSAGES](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#9-схема-базы-данных-postgresql) | [ ] |

### Definition of Done (Критерии завершения Этапа 8)
- [ ] Владелец генерирует инвайт-ссылку → менеджер переходит → уведомления магазина приходят только менеджеру.
- [ ] Бот добавлен в групповой рабочий чат → карточки отзывов поступают в группу.
- [ ] При увольнении менеджера попытки нажать инлайн-кнопки отклоняются, а уведомления возвращаются владельцу.
- [ ] Селлер отправляет скриншот в поддержку → Денис получает его в пуше и отвечает через Reply.

---

## Этап 9 — Мобильная админ-панель владельца и Пульт тестирования

**Цель:** Предоставить Денису полноценный инструмент мониторинга и управления всей платформой прямо из мессенджера (Telegram и MAX) без необходимости SSH-доступа к серверу: живой дашборд, ручное начисление балансов, принудительный Kill-Switch магазинов, интерактивный пульт тестов и экстренный рубильник очередей (Circuit Breaker).

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 9.1 | Реализовать систему контроля доступа админ-панели (RBAC): привязка к `ADMIN_TELEGRAM_IDS` и `ADMIN_MAX_IDS` в `.env`, полное сокрытие команды `/admin` для селлеров | [src/bot/admin/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/admin/handlers.py) | [§3.3.1 Безопасность RBAC](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console) | [ ] |
| 9.2 | Реализовать экран живого дашборда системы: вывод агрегатов за сутки в одном сообщении с кнопкой `[ 🔄 Обновить ]` (активные селлеры, обработанные отзывы, срез 1–5★, средний latency LLM, расход токенов, выручка) | [src/bot/admin/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/admin/handlers.py) | [§3.3.2 Живой дашборд](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console) | [ ] |
| 9.3 | Реализовать модуль управления селлерами и Kill-Switch: поиск по username / ID, просмотр баланса, кнопки `[ ⏸ Принудительная пауза ]`, `[ ▶️ Снять с паузы ]`, `[ ⛔ Заблокировать ]`, `[ 🎁 Начислить ответы ]` | [src/bot/admin/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/admin/handlers.py) | [§3.3.3 Управление селлерами и Kill-Switch](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console) | [ ] |
| 9.4 | Реализовать интерактивный пульт симулятора (Sandbox Console): кнопки `[ 🟢 Тест 5★ отзыва ]`, `[ 🔴 Тест 1★ негатива ]`, `[ ❓ Тест вопроса с БЗ ]`, `[ ⚠️ Тест нехватки данных ]`, `[ 💥 Тест сбоя API 500 ]` | [src/bot/admin/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/admin/handlers.py), [src/api/routers/sandbox.py](file:///d:/actual_projects/AI_for_salers/src/api/routers/sandbox.py) | [§3.3.4 Пульт тестирования](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console), [§4.7 Режим симулятора](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#47-встроенный-режим-симулятора-mock-marketplace-connector--sandbox-mode) | [ ] |
| 9.5 | Реализовать экран контроля очередей и Circuit Breaker: отображение глубины очередей RabbitMQ, сообщений в DLX, кнопки `[ 🛑 ЭКСТРЕННЫЙ СТОП ВСЕХ ВОРКЕРОВ ]`, `[ ♻️ Перезапуск воркеров ]`, `[ 🧹 Очистить зависшие блокировки ]` | [src/bot/admin/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/admin/handlers.py) | [§3.3.6 Контроль очередей и Circuit Breaker](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console) | [ ] |
| 9.6 | Реализовать экран детального учёта финансов и токенов: распределение себестоимости вызовов по моделям (`gpt-4o-mini`, `gigachat`) и селлерам | [src/bot/admin/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/admin/handlers.py) | [§3.3.5 Финансы и учёт токенов](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#33-встроенная-мобильная-админ-панель-admin-bot-console) | [ ] |

### Definition of Done (Критерии завершения Этапа 9)
- [ ] Денис отправляет `/admin` в Telegram или MAX и получает интерактивное меню админ-консоли.
- [ ] Нажатие кнопки `[ 🔴 Тест 1★ негатива ]` мгновенно запускает синтетическое событие и присылает карточку согласования.
- [ ] Нажатие кнопки `[ ⏸ Принудительная пауза ]` блокирует поллинг выбранного магазина селлера.
- [ ] Экран очередей показывает реальное число сообщений в RabbitMQ.

---

## Этап 10 — Модуль продуктовой AI-аналитики и Авто-дайджест

**Цель:** Реализовать функционал ИИ как продуктового аналитика магазина селлера: агрегацию статистики отзывов и вопросов, выявление частых болей покупателей (кластеризация жалоб на брак, доставку, несоответствие описанию), обнаружение пробелов в карточках товаров и регулярную рассылку структурированных дайджестов с рекомендациями по росту продаж.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 10.1 | Реализовать сервис агрегации статистики `src/analytics/service.py`: расчёт динамики рейтинга, индекса NPS, распределения оценок и сбор текстов вопросов/отзывов за 7, 30 и 90 дней | [src/analytics/service.py](file:///d:/actual_projects/AI_for_salers/src/analytics/service.py) | [§3.8 Модуль AI-аналитики](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#38-модуль-ai-аналитики-отзывов-и-стратегических-рекомендаций-селлеру) | [ ] |
| 10.2 | Реализовать модуль суммаризации `src/analytics/summarizer.py`: промпт-пайплайн для LLM с кластеризацией проблем (брак, логистика WB/Ozon, размер), частых вопросов и формированием рекомендаций по карточкам товаров | [src/analytics/summarizer.py](file:///d:/actual_projects/AI_for_salers/src/analytics/summarizer.py) | [§3.8 Структура аналитического отчёта](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#38-модуль-ai-аналитики-отзывов-и-стратегических-рекомендаций-селлеру) | [ ] |
| 10.3 | Реализовать генератор отчётов `src/analytics/reports.py`: форматирование текста отчёта для Telegram и MAX (эмодзи, структурированные списки, цитаты болей клиентов, маркеры 💡) | [src/analytics/reports.py](file:///d:/actual_projects/AI_for_salers/src/analytics/reports.py) | [§3.8 Структура отчёта](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#38-модуль-ai-аналитики-отзывов-и-стратегических-рекомендаций-селлеру) | [ ] |
| 10.4 | Реализовать пользовательский интерфейс в боте по кнопке `[ 📊 Аналитика ]`: выбор периода (7, 30, 90 дней), формирование отчёта по запросу в один клик | [src/bot/core/handlers.py](file:///d:/actual_projects/AI_for_salers/src/bot/core/handlers.py) | [§3.2.7 Аналитика и отчёты магазина](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#32-функциональные-возможности-бота) | [ ] |
| 10.5 | Настроить регулярный еженедельный дайджест в `SchedulerWorker`: автоматическая генерация отчёта каждый понедельник в 09:00 и рассылка в ЛС селлера или рабочий командный чат | [src/workers/scheduler.py](file:///d:/actual_projects/AI_for_salers/src/workers/scheduler.py) | [§3.8 Формирование отчётов](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#38-модуль-ai-аналитики-отзывов-и-стратегических-рекомендаций-селлеру) | [ ] |

### Definition of Done (Критерии завершения Этапа 10)
- [ ] Селлер нажимает `[ 📊 Аналитика ]` → `[ 7 дней ]` → получает структурированный отчёт с процентами жалоб и практическими рекомендациями.
- [ ] Рекомендации содержат конкретные советы (по инфографике, описанию, упаковке товара).
- [ ] Планировщик автоматически доставляет еженедельный дайджест в целевой чат магазина.

---

## Этап 11 — Мониторинг, Логирование и Алертинг

**Цель:** Развернуть полноценный стек наблюдаемости (Observability): сбор Prometheus-метрик, дашборды Grafana, агрегацию структурированных JSON-логов в Loki и автоматические мгновенные пуш-алерты Денису в Telegram и MAX при возникновении критических инцидентов.

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 11.1 | Настроить экспорт метрик Prometheus через эндпоинт `GET /metrics`: метрики очередей, latency нейросети, счётчики обработанных отзывов по статусам и маркетплейсам | [src/common/metrics.py](file:///d:/actual_projects/AI_for_salers/src/common/metrics.py), [src/main.py](file:///d:/actual_projects/AI_for_salers/src/main.py) | [§8.1 Стек Observability](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 11.2 | Настроить конфигурацию Prometheus `deploy/prometheus/prometheus.yml`: периодический scrape FastAPI-бэкенда, RabbitMQ exporter и PostgreSQL exporter | [deploy/prometheus/prometheus.yml](file:///d:/actual_projects/AI_for_salers/deploy/prometheus/prometheus.yml) | [§8.1 Prometheus](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 11.3 | Подготовить готовые JSON-дашборды Grafana (`deploy/grafana/provisioning/`): экраны общего здоровья системы, активности селлеров, очередей RabbitMQ и финансов | [deploy/grafana/](file:///d:/actual_projects/AI_for_salers/deploy/grafana/) | [§8.1 Grafana дашборды](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 11.4 | Настроить конфигурацию Loki `deploy/loki/loki-config.yml` и сборщик Promtail для парсинга потоков JSON-логов по сервисам (`tg_bot`, `max_bot`, `ai_worker`, `billing`) | [deploy/loki/loki-config.yml](file:///d:/actual_projects/AI_for_salers/deploy/loki/loki-config.yml) | [§8.1 Loki + Promtail](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 11.5 | Настроить правила AlertManager: алертинг при превышении 500-х ошибок, росте очереди DLX (> 5 задач), падении соединений к БД или сбоях вебхуков ЮKassa | [deploy/prometheus/](file:///d:/actual_projects/AI_for_salers/deploy/prometheus/) | [§8.1 AlertManager](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |
| 11.6 | Реализовать программный шлюз мгновенных алертов: отправка критических инцидентов напрямую в личный Telegram и MAX Дениса через ботов | [src/common/](file:///d:/actual_projects/AI_for_salers/src/common/) | [§6.1 DLX Алертинг](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq), [§8.1 Инциденты](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#81-стек-observability) | [ ] |

### Definition of Done (Критерии завершения Этапа 11)
- [ ] Дашборд Grafana открывается на `http://localhost:3000` и отображает реальные графики нагрузки и очередей.
- [ ] Логи приложения доступны в Grafana Explore (Loki) с удобной фильтрацией по тегам сервисов.
- [ ] При искусственной эмуляции падения воркера или переполнении DLX Денис моментально получает пуш-уведомление в личные сообщения Telegram и MAX.

---

## Этап 12 — Финальное сквозное тестирование (E2E), Стресс-тест и Релиз

**Цель:** Провести комплексную приёмку всей системы по BDD-сценариям спецификации, стресс-тестирование под параллельной нагрузкой, собрать production-образ Docker и подготовить проект к запуску на боевых серверах (Timeweb Cloud + JustHost proxy).

### Задачи этапа

| # | Задача | Файл(ы) реализации | Раздел спецификации | Статус |
|---|--------|-------------------|---------------------|:------:|
| 12.1 | Реализовать и выполнить полный прогон BDD-сценария 1: Автономный ответ на 5★ отзыв при активной подписке (генерация, списание 1 ответа, статус `published`) | [tests/e2e/test_bdd_scenarios.py](file:///d:/actual_projects/AI_for_salers/tests/e2e/) | [§12.2 BDD Сценарий 1](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-1-автономный-ответ-на-5-отзыв-при-активной-подписке) | [ ] |
| 12.2 | Реализовать и выполнить полный прогон BDD-сценария 2: Эскалация негативного отзыва (1–3★) человеку (карточка согласования, одобрение, публикация) | [tests/e2e/test_bdd_scenarios.py](file:///d:/actual_projects/AI_for_salers/tests/e2e/) | [§12.2 BDD Сценарий 2](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-2-эскалация-негативного-отзыва-13-человеку) | [ ] |
| 12.3 | Реализовать и выполнить полный прогон BDD-сценария 3: Защита от дубликатов при сбое сети (проверка Lease Lock и PostgreSQL статуса, zero duplicates) | [tests/e2e/test_bdd_scenarios.py](file:///d:/actual_projects/AI_for_salers/tests/e2e/) | [§12.2 BDD Сценарий 3](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-3-защита-от-дубликатов-при-сбое-сети) | [ ] |
| 12.4 | Реализовать и выполнить полный прогон BDD-сценария 4: Двухсторонний тикет в службу заботы со скриншотом и ответом владельца через Reply | [tests/e2e/test_bdd_scenarios.py](file:///d:/actual_projects/AI_for_salers/tests/e2e/) | [§12.2 BDD Сценарий 4](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#сценарий-4-двухсторонний-тикет-в-службу-поддержки) | [ ] |
| 12.5 | Провести стресс-тестирование: запуск 50 параллельных синтетических событий на 5 конкурентных воркеров, подтверждение отсутствия дедлоков и потерь | [tests/e2e/test_stress.py](file:///d:/actual_projects/AI_for_salers/tests/e2e/) | [§1.2 Отказоустойчивость](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#12-ключевые-бизнес-цели-mvp), [§6.1 Надежность](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#61-проблема-дублирования-и-потерь-в-rabbitmq) | [ ] |
| 12.6 | Подготовить многоэтапный `Dockerfile` (multi-stage build): оптимизация слоёв, non-root пользователь, минимальный размер контейнера | [Dockerfile](file:///d:/actual_projects/AI_for_salers/Dockerfile) | [§10 Clean Architecture](file:///d:/actual_projects/AI_for_salers/docs/SPECIFICATION.md#10-структура-проекта-clean-architecture) | [ ] |
| 12.7 | Оформить [README.md](file:///d:/actual_projects/AI_for_salers/README.md): архитектура, требования, команды локального запуска, инструкции по деплою и ссылки на документацию | [README.md](file:///d:/actual_projects/AI_for_salers/README.md) | [docs/production_launch_guide.md](file:///d:/actual_projects/AI_for_salers/docs/production_launch_guide.md) | [ ] |

### Definition of Done (Критерии завершения Этапа 12)
- [ ] Все 4 BDD-сценария спецификации проходят со статусом `PASSED`.
- [ ] Стресс-тест подтверждает стабильность очередей при пиковых нагрузках.
- [ ] Docker-образ успешно собирается и запускается на чистом стенде.
- [ ] Система готова к подключению боевых магазинов селлеров и запуску коммерческой подписки.

---

## 🔒 Незыблемые архитектурные правила проекта

1. **Button-First UX:** Пользовательский интерфейс строится исключительно на Reply и Inline клавиатурах. Слэш-команды запрещены для клиентского опыта.
2. **Асинхронность и очереди:** Никакого Celery и сторонних обёрток. Все фоновые задачи выполняются нативно через чистый RabbitMQ (`aio-pika`).
3. **Отсутствие кэширования карточек:** Информация о товаре (`fetch_live_product_context`) запрашивается свежей на каждый отзыв, чтобы исключить ответы по устаревшим данным.
4. **Абсолютная клиентская идемпотентность:** Защита от дублей строится на связке Redis Lease Lock (120 с) + статус в PostgreSQL + долговременный маркер (7 дней).
5. **Безопасность ключей:** Все токены маркетплейсов хранятся строго в зашифрованном виде (AES-256-GCM). Логирование открытых ключей категорически запрещено.
6. **Двухсерверная гибридная сеть:** Telegram-трафик и вызовы OpenAI идут через зарубежный forward-прокси JustHost (`USE_PROXY=true`). Мессенджер MAX, вебхуки ЮKassa и API маркетплейсов работают напрямую из РФ.

---

*Примечание: По мере выполнения задач разработчик или агент обязан отмечать выполненные пункты `[x]` в этом файле.*
