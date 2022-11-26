from typing import Protocol

from database.response import DatabaseResponse


class Database(Protocol):
    def add_employee(
        self, first_name: str, last_name: str, email: str
    ) -> DatabaseResponse:
        """Abstract method for adding an employee to the employee register"""

    def get_employees(self) -> DatabaseResponse:
        """Abstract method for getting all employees"""

    def remove_employee(self, id: str) -> DatabaseResponse:
        """Abstract method for removing an employee"""
