"""Регистрация Celery задач."""
from datetime import timedelta
from celery import Celery

from app.schemas import AddArgs, AddResult


celery_app = Celery('producer')
celery_app.config_from_object('app.celeryconfig')


@celery_app.task(name="tasks.low-priority", pydantic=True)
def add_low_task(args: AddArgs) -> AddResult:
    """Задача сложения двух чисел."""
    print(f"Выполняется low-priority: {args.a} + {args.b}")
    return AddResult(result=args.a + args.b)


@celery_app.task(name="tasks.high-priority", pydantic=True)
def add_high_task(args: AddArgs) -> AddResult:
    """Задача умножения двух чисел."""
    print(f"Выполняется high-priority: {args.a} * {args.b}")
    return AddResult(result=args.a * args.b)


@celery_app.task
def my_periodic_task(x=1, y=2):
    """Пример периодической задачи, выполняемой каждую минуту."""
    # Здесь сами определяете x, y (например, из БД, времени, API)
    # x, y = 1, 2
    print(f"Выполняется периодическая задача с x={x}, y={y}, результат: {x + y}")


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    """Настройка периодических задач после конфигурации Celery."""
    # Добавляем задачу динамически (например, x=5, y=10)
    sender.add_periodic_task(
        timedelta(seconds=30),         # каждые 30 секунд
        my_periodic_task.s(5, 10),
        name='dynamic-each-30-seconds'
    )
