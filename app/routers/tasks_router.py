from uuid import UUID
from fastapi import APIRouter, HTTPException

import app.schemas.task as schemas
from app.services import task_service

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return task_service.get_tasks()

@router.delete("/tasks")
def delete_tasks():
    return task_service.delete_tasks()

@router.post("/tasks")
def create_tasks(task: schemas.Task):
    task_service.create_task(task)
    return task

@router.get('/tasks/{uid}')
def get_task(*, uid: UUID):
    result =  task_service.get_task(uid)

    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        # 2
        raise HTTPException(
            status_code=404, detail=f"Category with ID {uid} not found"
        )

    return result[0]