import pytest
from pydantic import BaseModel


class Employee(BaseModel):
    first_name: str
    last_name: str
    email: str


def test_employee_empty() -> None:
    """We don't allow shallow employees"""
    with pytest.raises(Exception):
        Employee()