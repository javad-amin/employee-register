import uuid

from database.memory_db import MemoryDB
from database.response import DatabaseResponse, ResponseStatus


def test_add_employee() -> None:
    employee = {
        "first_name": "James",
        "last_name": "Bond",
        "email": "james@bond.com",
    }
    memory_db = MemoryDB()
    response = memory_db.add_employee(**employee)

    assert isinstance(response, DatabaseResponse)
    assert response.status == ResponseStatus.SUCCESS

    assert response.content.get("first_name") == employee["first_name"]
    assert response.content.get("last_name") == employee["last_name"]
    assert response.content.get("email") == employee["email"]
    assert uuid.UUID(response.content.get("identifier"))

    saved_employees = memory_db.employees

    assert saved_employees[0].first_name == employee["first_name"]
    assert saved_employees[0].last_name == employee["last_name"]
    assert saved_employees[0].email == employee["email"]
    assert uuid.UUID(saved_employees[0].identifier)


def test_get_employees_empty():
    memory_db = MemoryDB()
    response = memory_db.get_employees()
    employees = response.content

    assert employees == []
