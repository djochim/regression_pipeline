
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_post_tasks():
    response = client.post("/tasks",
        json={"name": "Finish presentation"},
    )
    assert response.status_code == 200
    json_body = response.json()
    assert json_body['name'] == "Finish presentation"
    assert json_body['id'] is not None
    assert json_body['isFinished'] is False
    created_task_id = json_body['id']
    
    response = client.get("/tasks")
    assert response.status_code == 200
    json_body = response.json()[0]
    assert json_body['name'] == "Finish presentation"
    assert json_body['id'] == created_task_id
    assert json_body['isFinished'] is False