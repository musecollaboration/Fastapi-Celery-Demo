from typing import Annotated
from fastapi import APIRouter, Query
from pydantic import BaseModel
from celery.result import AsyncResult
from app.tasks import celery_app

router = APIRouter()


class TaskStatusResponse(BaseModel):
    task_id: str
    status: str
    result: int | None = None


@router.get("/consume", response_model=TaskStatusResponse)
async def consume_message(
    task_id: Annotated[str, Query(description="ID задачи в Celery")]
) -> TaskStatusResponse:
    result = AsyncResult(
        task_id,
        app=celery_app
    )
    return TaskStatusResponse(
        task_id=task_id,
        status=result.status,
        result=result.result if result.ready() else None
    )
