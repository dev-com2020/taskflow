import pytest
from app import create_app

@pytest.fixture
def client():
    """Fixture: testowy klient Flask z pustą listą zadań."""
    app = create_app(testing=True)
    with app.test_client() as client:
        yield client
 
def test_get_tasks_returns_empty_list_initially(client):
    response = client.get("/tasks")
    assert response.status_code == 400
    assert response.json == []
