from uuid import uuid4

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_guest_can_view_activities():
    response = client.get("/activities")
    assert response.status_code == 200


def test_guest_cannot_manage_activity_without_role():
    response = client.post(f"/activities/Chess Club/signup?email={uuid4()}@example.com")
    assert response.status_code == 401


def test_staff_can_manage_activity():
    response = client.post(
        f"/activities/Chess Club/signup?email={uuid4()}@example.com",
        headers={"X-Role": "staff"},
    )
    assert response.status_code == 200


def test_admin_can_manage_activity():
    response = client.post(
        f"/activities/Chess Club/signup?email={uuid4()}@example.com",
        headers={"X-Role": "admin"},
    )
    assert response.status_code == 200
