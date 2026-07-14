import pytest
from app import create_app
import app.routes as routes

@pytest.fixture
def client():
    app = create_app(testing=True)
    # upewnij się, że globalna lista jest czysta przed i po teście
    routes.tasks.clear()
    with app.test_client() as client:
        yield client
    routes.tasks.clear()

def test_get_tasks_empty(client):
    rv = client.get("/tasks")
    assert rv.status_code == 200
    assert rv.is_json
    assert rv.get_json() == []

def test_post_task_missing_content_returns_400(client):
    rv = client.post("/tasks", json={})
    assert rv.status_code == 400
    assert rv.is_json
    assert rv.get_json() == {"error": "Content is required"}

def test_post_task_with_content_current_behavior_detects_missing_implementation(client):
    # Obecna implementacja create_task kończy się bez return - test wykryje to (np. 500).
    rv = client.post("/tasks", json={"content": "moja treść"})
    # Sprawdzamy, że coś jest nie tak: oczekujemy, że status nie będzie 200 OK bez treści zwrotnej.
    # Można tu być bardziej precyzyjnym (np. ==500) ale różne wersje Flask/konfiguracja mogą różnić.
    assert rv.status_code != 200

def test_post_task_expected_behavior_when_fixed(client):
    # Ten test opisuje oczekiwane zachowanie po implementacji:
    # - zwrócenie 201 CREATED (lub 200) z JSON zawierającym dodane zadanie
    # - zadanie dodane do routes.tasks
    rv = client.post("/tasks", json={"content": "zadanie testowe"})
    # Ten test prawdopodobnie teraz failnie; po poprawce powinien przejść.
    assert rv.status_code in (200, 201)
    assert rv.is_json
    data = rv.get_json()
    # oczekujemy struktury listy lub pojedynczego obiektu — dopasuj do implementacji
    assert data  # niepuste
    assert any("zadanie testowe" in str(v) for v in (data, str(routes.tasks)))
