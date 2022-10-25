from uuid import UUID
from fastapi import APIRouter, HTTPException

import app.schemas.task as schemas
import app.services.task_service as task_service

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return task_service.get_tasks()

@router.post("/tasks")
def create_tasks(task: schemas.Task):
    task_service.create_task(task)
    return task

@router.get('/tasks/{id}')
def get_tasks(*, id: UUID):
    result =  task_service.get_task(id)

    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        # 2
        raise HTTPException(
            status_code=404, detail=f"Category with ID {id} not found"
        )

    return result[0]