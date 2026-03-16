from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def _create_user_and_token():
    email = "test@example.com"
    password = "password123"

    resp = client.post(
        "/api/signup",
        json={"full_name": "Test User", "email": email, "password": password},
    )
    assert resp.status_code in (200, 201)

    resp = client.post(
        "/api/login",
        data={"username": email, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert resp.status_code == 200
    data = resp.json()
    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    return headers


def test_full_flow_projects_and_tasks():
    headers = _create_user_and_token()

    # Create project
    resp = client.post(
        "/api/projects",
        json={"name": "My Project", "description": "Test project"},
        headers=headers,
    )
    assert resp.status_code == 201
    project = resp.json()
    project_id = project["id"]

    # List projects
    resp = client.get("/api/projects", headers=headers)
    assert resp.status_code == 200
    projects = resp.json()
    assert len(projects) == 1
    assert projects[0]["id"] == project_id

    # Create task
    resp = client.post(
        f"/api/projects/{project_id}/tasks",
        json={"title": "My Task", "description": "Do something"},
        headers=headers,
    )
    assert resp.status_code == 201
    task = resp.json()
    task_id = task["id"]
    assert task["title"] == "My Task"

    # Toggle completion via update
    resp = client.put(
        f"/api/tasks/{task_id}",
        json={"is_completed": True},
        headers=headers,
    )
    assert resp.status_code == 200
    task = resp.json()
    assert task["is_completed"] is True

    # Delete task
    resp = client.delete(f"/api/tasks/{task_id}", headers=headers)
    assert resp.status_code == 204

    # Delete project
    resp = client.delete(f"/api/projects/{project_id}", headers=headers)
    assert resp.status_code == 204

