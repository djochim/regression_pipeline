import pytest

from app.schemas.task import Task
import app.services.task_service as task_service

@pytest.fixture
def clear_tests():
    task_service.delete_tasks()

def test_create_get_tasks(clear_tests):
    task = Task(name="Test")
    task_service.create_task(task)

    received_tasks = task_service.get_tasks()
    assert received_tasks.count is not 0
    assert received_tasks[0] != task

def test_create_get_task(clear_tests):
    task = Task(name="Test")
    task_service.create_task(task)

    received_task = task_service.get_task(task.id)
    assert received_task == task