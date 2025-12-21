from typing import Annotated
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.tasks import add_low_task, add_high_task

router = APIRouter(prefix="/producer")


class Message(BaseModel):
    """Модель сообщения для выполнения математических операций."""
    a: Annotated[int, Field(gt=0, description="Первое число для операции")]
    b: Annotated[int, Field(gt=0, description="Второе число для операции")]


@router.post("/add")
async def low_task(message: Message) -> dict:
    '''Endpoint для отправки задачи сложения двух чисел в очередь Celery.'''
    task = add_low_task.delay(message.a, message.b)
    return {
        "status": "Задача отправлена",
        'task_id': task.id
    }


@router.post("/heavy")
async def heavy_task(message: Message):
    '''Endpoint для отправки тяжёлой задачи в очередь Celery.'''
    task = add_high_task.delay(message.a, message.b)
    return {
        "status": "Тяжёлая задача отправлена",
        'task_id': task.id
    }
