"""Регистрация Celery задач."""
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
