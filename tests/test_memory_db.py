import uuid
from dataclasses import dataclass, field
from typing import Final, Union


class ResponseStatus:
    FAILURE: Final = "failure"
    SUCCESS: Final = "success"


@dataclass
class DatabaseResponse:
    status: str = ResponseStatus.SUCCESS
    content: dict | str = ""


@dataclass
class EmployeeItem:
    identifier: str
    email: str
    first_name: str = ""
    last_name: str = ""


@dataclass
class MemoryDB:
    employees: list[EmployeeItem] = field(default_factory=list)

    def add_employee(
        self, first_name: str, last_name: str, email: str
    ) -> DatabaseResponse:
        new_employee = {
            "identifier": str(uuid.uuid4()),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }

        self.employees.append(EmployeeItem(**new_employee))

        return DatabaseResponse(content=new_employee)


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
