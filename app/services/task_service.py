import uuid
from app.schemas.task import Task

tasks = []

def delete_tasks():
    tasks.clear()

def get_tasks():
    return tasks

def create_task(task: Task):
    tasks.append(task)

def get_task(uid: uuid.UUID):
    return [task for task in tasks if task.id == uid][0]