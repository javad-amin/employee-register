import uuid
from dataclasses import dataclass, field

from database.item import EmployeeItem
from database.response import DatabaseResponse, ResponseStatus


@dataclass
class MemoryDB:
    employees: list[EmployeeItem] = field(default_factory=list)

    def add_employee(
        self, first_name: str, last_name: str, email: str
    ) -> DatabaseResponse:
        if self._email_already_registered(email):
            return DatabaseResponse(
                "Employee with the given email address is already registered.",
                ResponseStatus.FAILURE,
            )

        new_employee = {
            "identifier": str(uuid.uuid4()),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }

        self.employees.append(EmployeeItem(**new_employee))

        return DatabaseResponse(content=new_employee)

    def get_employees(self) -> DatabaseResponse:
        employees_response = [employee.__dict__ for employee in self.employees]
        return DatabaseResponse(content=employees_response)

    def remove_employee(self, identifier: str) -> DatabaseResponse:
        for i, employee in enumerate(self.employees):
            if identifier == employee.identifier:
                self.employees.pop(i)
                return DatabaseResponse(
                    {"message": "Employee was removed successfully"}
                )
        return DatabaseResponse(
            f"The employee with employee identifier {identifier} not found.",
            ResponseStatus.FAILURE,
        )

    def _email_already_registered(self, email) -> bool:
        for employee in self.employees:
            if email.lower() == employee.email.lower():
                return True
        return False
