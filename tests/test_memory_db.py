from dataclasses import dataclass


class DatabaseResponse:
    pass


@dataclass
class MemoryDB:
    def add_employee(self) -> DatabaseResponse:
        return DatabaseResponse()


def test_add_employee() -> None:
    memory_db = MemoryDB()
    response = memory_db.add_employee()

    assert isinstance(response, DatabaseResponse)
