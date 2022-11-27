from typing import Protocol


class Database(Protocol):
    def add_employee(self, first_name: str, last_name: str, email: str) -> dict:
        """Abstract method for adding an employee to the employee register"""

    def get_employees(self) -> list[dict]:
        """Abstract method for getting all employees"""

    def remove_employee(self, id: str) -> None:
        """Abstract method for removing an employee"""
