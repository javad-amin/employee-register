import uuid
from dataclasses import dataclass, field

from database.item import EmployeeItem
from database.response import DatabaseResponse


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

    def get_employees(self) -> DatabaseResponse:
        return DatabaseResponse(content=[])
