import uuid
from dataclasses import dataclass, field

from database.exception import EmployeeAlreadyExists, EmployeeNotFound
from database.item import EmployeeItem


@dataclass
class MemoryDB:
    employees: list[EmployeeItem] = field(default_factory=list)

    def add_employee(self, first_name: str, last_name: str, email: str) -> dict:
        if self._email_already_registered(email):
            raise EmployeeAlreadyExists("Email address is already registered.")

        new_employee = {
            "identifier": str(uuid.uuid4()),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }

        self.employees.append(EmployeeItem(**new_employee))

        return new_employee

    def get_employees(self) -> list[dict]:
        return [employee.__dict__ for employee in self.employees]

    def remove_employee(self, identifier: str) -> None:
        for i, employee in enumerate(self.employees):
            if identifier == employee.identifier:
                self.employees.pop(i)
                return
        raise EmployeeNotFound(f"Employee with {identifier=} not found.")

    def _email_already_registered(self, email) -> bool:
        for employee in self.employees:
            if email.lower() == employee.email.lower():
                return True
        return False
