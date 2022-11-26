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


def test_get_employees(pre_populated_database: MemoryDB) -> None:
    assert len(pre_populated_database.get_employees().content) == 4

    pre_populated_database.add_employee(
        first_name="Lady",
        last_name="Gaga",
        email="lady@queen.com",
    )
    assert len(pre_populated_database.get_employees().content) == 5


def test_remove_employee(pre_populated_database: MemoryDB) -> None:
    second_employee = pre_populated_database.employees[1]
    uuid_to_delete = second_employee.identifier

    pre_populated_database.remove_employee(identifier=uuid_to_delete)

    # As the pre_populated_database has four employees after deleting we should have three left
    assert len(pre_populated_database.employees) == 3

    assert second_employee not in pre_populated_database.employees


def test_remove_employee_no_match_found(pre_populated_database: MemoryDB) -> None:
    none_existing_id = "06335e84-2872-4914-8c5d-3ed07d2a2f16"
    response = pre_populated_database.remove_employee(none_existing_id)
    assert response.status == ResponseStatus.FAILURE


def test_add_employee_duplicate_email(pre_populated_database: MemoryDB) -> None:
    pre_populated_database.add_employee(
        first_name="Lady",
        last_name="Gaga",
        email="lady@queen.com",
    )

    response = pre_populated_database.add_employee(
        first_name="Mr",
        last_name="Gaga",
        email="lady@queen.com",
    )
    assert response.status == ResponseStatus.FAILURE
