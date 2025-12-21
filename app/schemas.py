"""Схемы Pydantic для валидации и сериализации данных."""
from typing import Annotated

from pydantic import BaseModel, Field


class TaskStatusResponse(BaseModel):
    """Модель ответа о статусе задачи."""
    task_id: Annotated[str, Field(description="ID задачи в Celery")]
    status: Annotated[str, Field(description="Статус задачи в Celery")]
    result: Annotated[int | None, Field(description="Результат задачи, если доступен")]


class Message(BaseModel):
    """Модель сообщения для выполнения математических операций."""
    a: Annotated[int, Field(gt=0, description="Первое число для операции")]
    b: Annotated[int, Field(gt=0, description="Второе число для операции")]


class AddArgs(BaseModel):
    """Модель аргументов для операции сложения."""
    a: Annotated[int, Field(gt=0, description="Первое число для операции")]
    b: Annotated[int, Field(gt=0, description="Второе число для операции")]


class AddResult(BaseModel):
    """Модель результата операции сложения."""
    result: Annotated[int, Field(description="Результат операции")]


class AddId(BaseModel):
    """Модель для получения ID задачи."""
    task_id: Annotated[str, Field(description="ID задачи в Celery")]
