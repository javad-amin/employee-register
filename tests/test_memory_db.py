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
            "identifier": "917c1ecd-4e07-4a1c-8f9e-f189e95564e6",
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

    expected = employee.copy()
    expected["identifier"] = "917c1ecd-4e07-4a1c-8f9e-f189e95564e6"

    assert isinstance(response, DatabaseResponse)
    assert response.status == ResponseStatus.SUCCESS
    assert response.content == expected
    assert memory_db.employees == [EmployeeItem(**expected)]
