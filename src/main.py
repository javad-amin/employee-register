from typing import Generator

from fastapi import Depends, FastAPI, HTTPException, status

from database.exception import EmployeeAlreadyExists, EmployeeNotFound
from database.interface import Database
from database.memory_db import MemoryDB
from employee import Employee

app = FastAPI()

DATABASE = MemoryDB()


def get_database() -> Generator:
    yield DATABASE


@app.get("/")
def get_all_employees(
    database: Database = Depends(get_database),
):
    """Endpoint for listing all of the employees.

    Raises HTTPException for other unknown exceptions."""
    try:
        database_response = database.get_employees()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

    return database_response


@app.post("/employee", status_code=status.HTTP_201_CREATED)
def add_employee(
    employee: Employee,
    database: Database = Depends(get_database),
):
    """Endpoint for adding an employee to the database.

    Expects a json body with the defined schema in Employee class.

    Raises HTTPException 400 in case of taken email.

    Raises HTTPException for other unknown exceptions."""
    try:
        database_response = database.add_employee(**employee.dict())
    except EmployeeAlreadyExists as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error.",
        )

    return database_response


@app.delete("/employee/{id}")
def remove_employee(
    id: str,
    database: Database = Depends(get_database),
):
    """Endpoint for removing an employee from the database.

    Expects the id of the employee as a path parameter.

    Raises HTTPException 404 in case of the employee does not exist.

    Raises HTTPException for other unknown exceptions."""
    try:
        database.remove_employee(id)
    except EmployeeNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error.",
        )

    return {"detail": f"Employee {id} removed successfully"}
