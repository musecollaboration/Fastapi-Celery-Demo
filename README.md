# Celery + FastAPI Example Project

## Описание

Этот проект демонстрирует базовую интеграцию FastAPI и Celery для асинхронной обработки задач с использованием RabbitMQ (брокер) и Redis (backend). Подходит для учебных и production-прототипов.

- FastAPI — REST API для постановки и отслеживания задач
- Celery — обработка задач в очередях
- RabbitMQ — брокер сообщений
- Redis — хранилище результатов
- Flower — мониторинг очередей и воркеров

## Структура проекта

```txt
celery_fastapi_demo/
├── app/
│ ├── __init__.py
│ ├── celeryconfig.py      # Конфиг Celery
│ ├── consumer.py          # Endpoint для получения статуса задачи
│ ├── main.py              # FastAPI app
│ ├── producer.py          # Endpoint для постановки задач
│ ├── tasks.py             # Регистрация Celery задач
│ └── schemas.py           # Pydantic-схемы
│
├── docker-compose.yml   # Инфраструктура (RabbitMQ, Redis, Flower)
├── Makefile             # Быстрый запуск API и worker
├── pyproject.toml       # Poetry/зависимости
└── README.md
```

## Быстрый старт

1. **Запуск инфраструктуры**

```bash
docker-compose up -d
```

2. **Установка зависимостей**

```bash
poetry install
```

3. **Запуск FastAPI**

```bash
make run
# или вручную:
# poetry run uvicorn app.main:app --reload
```

4. **Запуск Celery worker**

```bash
make celery
# или вручную:
# poetry run celery -A app.tasks worker --loglevel=info -Q low-priority,high-priority
```

Откройте http://127.0.0.1:8000/docs

---

5. **Мониторинг очередей (Flower)**

Откройте http://localhost:5555

---

## Основные компоненты

### FastAPI endpoints

- `POST /producer/add` — отправить задачу сложения
- `POST /producer/heavy` — отправить задачу умножения
- `GET /consume?task_id=...` — получить статус и результат задачи

### Celery задачи

- `add_low_task` — сложение двух чисел (low-priority)
- `add_high_task` — умножение двух чисел (high-priority)

### Конфиг Celery (app/celeryconfig.py)

- task_routes — маршрутизация задач по очередям
- task_queues — явное объявление очередей
- task_annotations — лимиты на задачи
- broker_url, result_backend — настройки RabbitMQ и Redis

---

## Примеры запросов

### Отправить задачу

```bash
curl -X POST http://localhost:8000/producer/add -H "Content-Type: application/json" -d '{"a": 2, "b": 3}'
```

### Проверить статус задачи

```bash
curl "http://localhost:8000/consume?task_id=<ID_ЗАДАЧИ>"
```

---

## Мониторинг

- Flower: http://localhost:5555 (логин/пароль guest/guest)
- RabbitMQ UI: http://localhost:15672 (логин/пароль guest/guest)

---

## Возможности для расширения

- Добавить периодические задачи (Periodic Tasks)
- Добавить цепочки задач (Canvas)
- Настроить логирование (logging вместо print)
- Добавить тесты
- Реализовать аутентификацию и защиту API
- Добавить healthcheck endpoint для FastAPI

---

## Лицензия

MIT

## Автор

#### [Python Backend на FastAPI](https://stepik.org/a/223717)
