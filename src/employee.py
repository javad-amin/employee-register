from typing import Optional

from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    first_name: str
    last_name: Optional[str] = ""
    email: EmailStr
