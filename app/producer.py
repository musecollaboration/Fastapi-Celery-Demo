from fastapi import APIRouter
from pydantic import Field
from app.schemas import Message
from app.tasks import add_low_task, add_high_task

router = APIRouter(prefix="/producer")


@router.post("/add")
async def low_task(message: Message) -> dict:
    '''Endpoint для отправки задачи сложения двух чисел в очередь Celery.'''
    task = add_low_task.delay(message.model_dump())
    return {
        "status": "Задача отправлена",
        'task_id': task.id
    }


@router.post("/heavy")
async def heavy_task(message: Message):
    '''Endpoint для отправки тяжёлой задачи в очередь Celery.'''
    task = add_high_task.delay(message.model_dump())
    return {
        "status": "Тяжёлая задача отправлена",
        'task_id': task.id
    }
