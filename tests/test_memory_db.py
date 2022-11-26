from dataclasses import dataclass
from typing import Final, Union


class ResponseStatus:
    FAILURE: Final = "failure"
    SUCCESS: Final = "success"


@dataclass
class DatabaseResponse:
    status: str = ResponseStatus.SUCCESS
    content: dict | str = ""


@dataclass
class MemoryDB:
    def add_employee(
        self, first_name: str, last_name: str, email: str
    ) -> DatabaseResponse:
        new_employee = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }
        return DatabaseResponse(content=new_employee)


def test_add_employee() -> None:
    memory_db = MemoryDB()
    response = memory_db.add_employee(
        first_name="James",
        last_name="Bond",
        email="james@bond.com",
    )

    assert isinstance(response, DatabaseResponse)
    assert response.status == ResponseStatus.SUCCESS
    assert response.content == {
        "first_name": "James",
        "last_name": "Bond",
        "email": "james@bond.com",
    }
