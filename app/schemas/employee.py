
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    department: str
    designation: str
    salary: float = Field(..., gt=0)


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    salary: Optional[float] = Field(default=None, gt=0)
