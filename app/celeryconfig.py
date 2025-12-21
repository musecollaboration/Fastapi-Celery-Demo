
from kombu import Queue


# Брокер и backend


broker_url = 'pyamqp://guest@localhost//'
result_backend = 'redis://localhost:6379/1'

# Сериализация
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']   # игнорируем небезопасный pickle

# Время
timezone = 'Europe/Moscow'
enable_utc = True

# Политика хранения результатов
task_ignore_result = False
result_expires = 86400  # TTL 24 часа

# Наблюдаемость и контроль времени
task_track_started = True
task_time_limit = 300        # жёсткий лимит: 5 минут
task_soft_time_limit = 260   # мягкий: 4 мин 20 сек

# Определяет, какая задача в какую очередь попадёт (маршрутизация)
task_routes = {
    'tasks.low-priority': {'queue': 'low-priority'},
    'tasks.high-priority': {'queue': 'high-priority'},
}

# Для явного создания очередей на стороне брокера.
task_queues = (
    Queue('low-priority'),
    Queue('high-priority'),
)

# Аннотации (ограничения и лимиты)
task_annotations = {
    'tasks.low-priority': {'rate_limit': '10/m'},      # не более 10 задач low-priority в минуту
    'tasks.high-priority': {'rate_limit': '2/m'}       # тяжёлые задачи — максимум 2 в минуту
}
