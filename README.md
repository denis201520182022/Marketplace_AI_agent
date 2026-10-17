# AI for Salers — Омниканальный AI-агент для селлеров Wildberries и Ozon

> Высоконадежная отказоустойчивая система автоматизации поддержки селлеров с использованием ИИ (LangGraph, OpenAI), омниканальным управлением (Telegram + MAX) и поддержкой 100% суверенного РФ-контура или гибридного прокси-режима.


Стек включает в себя:
- **PostgreSQL 16** (порт 5432)
- **Redis 7** (порт 6379)
- **RabbitMQ 3.13** (порты 5672, 15672)
- **Qdrant** (порт 6333)
- **Prometheus** (порт 9090)
- **Grafana** (порт 3000, логин/пароль: `admin`/`admin`)
- **Loki** (порт 3100)
- **Promtail**

## 📚 Документация проекта
- [Техническая спецификация](docs/SPECIFICATION.md)
- [ROADMAP поэтапной разработки](docs/ROADMAP.md)
- [Регламент подключения селлеров](docs/seller_onboarding_guide.md)
- [Экономика и юнит-экономика токенов](docs/economics_and_budget.md)
- [Интеграция Wildberries API](docs/wb_api.md)
- [Интеграция Ozon API](docs/ozon_api.md)
