from typing import Annotated
from fastapi import APIRouter, Query
from app.schemas import TaskStatusResponse
from celery.result import AsyncResult
from app.tasks import celery_app
from app.schemas import AddResult

router = APIRouter()


@router.get("/consume", response_model=TaskStatusResponse)
async def consume_message(
    task_id: Annotated[str, Query(description="ID задачи в Celery")]
) -> TaskStatusResponse:
    result = AsyncResult(
        task_id,
        app=celery_app
    )
    if result.ready() and result.result:
        try:
            add_result = AddResult.model_validate(result.result)
            value = add_result.result
        except Exception:
            value = None
    else:
        value = None
    return TaskStatusResponse(
        task_id=task_id,
        status=result.status,
        result=value
    )
