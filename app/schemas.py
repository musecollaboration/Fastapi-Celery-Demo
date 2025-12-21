from pydantic import BaseModel
from pydantic import Field
from typing import Annotated


class TaskStatusResponse(BaseModel):
    task_id: Annotated[str, Field(description="ID задачи в Celery")]
    status: Annotated[str, Field(description="Статус задачи в Celery")]
    result: Annotated[int | None, Field(description="Результат задачи, если доступен")]


class Message(BaseModel):
    """Модель сообщения для выполнения математических операций."""
    a: Annotated[int, Field(gt=0, description="Первое число для операции")]
    b: Annotated[int, Field(gt=0, description="Второе число для операции")]


class AddArgs(BaseModel):
    a: Annotated[int, Field(gt=0, description="Первое число для операции")]
    b: Annotated[int, Field(gt=0, description="Второе число для операции")]


class AddResult(BaseModel):
    result: Annotated[int, Field(description="Результат операции")]
