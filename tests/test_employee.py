from typing import Optional

import pytest
from pydantic import BaseModel


class Employee(BaseModel):
    first_name: str
    last_name: Optional[str] = ""
    email: str


def test_employee_empty() -> None:
    """We don't allow shallow employees"""
    with pytest.raises(Exception):
        Employee()

def test_employee_missing_first_name() -> None:
    """An employee without a first name is not acceptable"""
    with pytest.raises(Exception):
        Employee()

def test_employee_missing_last_name() -> None:
    """An employee without a last name is fine, let's not get so formal now"""
    employee = Employee(first_name="Lady", email="lady@gaga.com")
    assert employee.last_name == ""

def test_employee_missing_email() -> None:
    """An employee without a email address is not acceptable"""
    with pytest.raises(Exception):
        Employee(first_name="Lady", last_name="Gaga")
