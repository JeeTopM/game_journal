# game_journal 🎮

Персональный игровой журнал с Telegram-интерфейсом и веб-административной панелью.

## Возможности 🚀

### Через Telegram-бота:
- 📅 Запись игровых сессий с датой и временем
- 🎯 Автоматическое извлечение сущностей (персонажи, локации)
- 🔍 Поиск по истории игр

### Через веб-интерфейс:
- 👁️ Полный просмотр и редактирование записей
- ⚙️ Управление каталогом игр
- 🔎 Продвинутый поиск с фильтрами

## 🏗️ Архитектура
```bash
Game Journal/
├── 🐍 Django Backend (REST API + Admin)
├── 🐘 PostgreSQL (с полнотекстовым поиском)
├── 🤖 Telegram Bot (telebot)
└── 🐳 Docker контейнеры
```

## Технологии 🛠️
- **Backend**: Django 4.x, Django REST Framework
- **Database**: PostgreSQL с pg_trgm для поиска
- **Bot Framework**: telebot
- **Containerization**: Docker & Docker Compose
- **Search**: Django PostgreSQL full-text search
