from typing import Annotated

from celery.result import AsyncResult
from fastapi import APIRouter, Depends

from app.schemas import AddResult, TaskStatusResponse, AddId
from app.tasks import celery_app


router = APIRouter()


@router.get("/consume", response_model=TaskStatusResponse)
async def consume_message(add_id: Annotated[AddId, Depends()]) -> TaskStatusResponse:
    result = AsyncResult(
        add_id.task_id,
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
        task_id=add_id.task_id,
        status=result.status,
        result=value
    )
