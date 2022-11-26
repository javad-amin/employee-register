import json
from os import path

import pytest

from database.memory_db import MemoryDB

from .datatools import DATA_FOLDER


@pytest.fixture
def pre_populated_database() -> MemoryDB:
    with open(path.join(DATA_FOLDER, "employees.json")) as employees_file:
        employees: dict = json.loads(employees_file.read())
        memory_db = MemoryDB()
        for employee in employees:
            memory_db.add_employee(**employee)
        yield memory_db
