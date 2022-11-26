from dataclasses import dataclass


@dataclass
class EmployeeItem:
    identifier: str
    email: str
    first_name: str = ""
    last_name: str = ""
