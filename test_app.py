import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == []

def test_add_task(client):
    response = client.post("/tasks", json={"task": "Buy groceries"})
    assert response.status_code == 201
    assert response.json["task"] == "Buy groceries"

def test_add_task_without_data(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400
    assert response.json["error"] == "Task is required"

def test_delete_task(client):
    client.post("/tasks", json={"task": "Buy groceries"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json["message"] == "Task deleted"
