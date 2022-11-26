import uuid

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_api_crud():
    add_employee_response = client.post(
        "/employee",
        json={
            "first_name": "The Notorious",
            "last_name": "BIG",
            "email": "notorous.big@hof.com",
        },
    )
    assert add_employee_response.status_code == 201
    assert add_employee_response.json().get("first_name") == "The Notorious"
    assert add_employee_response.json().get("last_name") == "BIG"
    assert add_employee_response.json().get("email") == "notorous.big@hof.com"
    assert uuid.UUID(add_employee_response.json().get("identifier"))

    get_employee_response = client.get("/")
    assert get_employee_response.status_code == 200

    recently_added_employee = get_employee_response.json()[0]
    assert recently_added_employee.get("first_name") == "The Notorious"
    assert recently_added_employee.get("last_name") == "BIG"
    assert recently_added_employee.get("email") == "notorous.big@hof.com"
    assert uuid.UUID(recently_added_employee.get("identifier"))

    remove_employee_response = client.delete(
        f"employee/{recently_added_employee.get('identifier')}"
    )
    assert remove_employee_response.status_code == 200
    get_employee_response = client.get("/")

    get_employee_response.json() == []
