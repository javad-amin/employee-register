from typing import Generator

from fastapi import Depends, FastAPI, HTTPException, status

from database.interface import Database
from database.memory_db import MemoryDB
from database.response import ResponseStatus
from employee import Employee

app = FastAPI()

DATABASE = MemoryDB()


def get_database() -> Generator:
    yield DATABASE


@app.get("/")
def get_all_employees(
    database: Database = Depends(get_database),
):
    database_response = database.get_employees()
    if database_response.status == ResponseStatus.SUCCESS:
        return database_response.content
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@app.post("/employee", status_code=status.HTTP_201_CREATED)
def add_employee(
    employee: Employee,
    database: Database = Depends(get_database),
):
    database_response = database.add_employee(**employee.dict())
    if database_response.status == ResponseStatus.SUCCESS:
        return database_response.content
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=database_response.content or "Internal server error",
        )


@app.delete("/employee/{id}")
def remove_employee(
    id: str,
    database: Database = Depends(get_database),
):
    database_response = database.remove_employee(id)
    if database_response.status == ResponseStatus.SUCCESS:
        return {"detail": f"Employee {id} removed successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {id} was not found",
        )
