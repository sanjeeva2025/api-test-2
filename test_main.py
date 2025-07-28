from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_create_user():
    user = {"id": 1, "name": "Alice", "email": "alice@example.com"}
    response = client.post("/users/", json=user)
    assert response.status_code == 200
    assert response.json() == user
