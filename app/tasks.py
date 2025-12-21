"""Регистрация Celery задач."""
from celery import Celery

celery_app = Celery('producer')
celery_app.config_from_object('app.celeryconfig')


@celery_app.task(name="tasks.low-priority")
def add_low_task(a: int, b: int) -> int:
    """Задача сложения двух чисел."""
    print(f"Выполняется low-priority: {a} + {b}")
    return a + b


@celery_app.task(name="tasks.high-priority")
def add_high_task(a: int, b: int) -> int:
    """Задача умножения двух чисел."""
    print(f"Выполняется high-priority: {a} * {b}")
    return a * b
