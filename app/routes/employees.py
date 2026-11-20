
from fastapi import APIRouter, HTTPException

from app.schemas.employee import EmployeeCreate, EmployeeUpdate

from app.services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)

router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)


# POST: Create employee
@router.post("/")
def add_employee(employee: EmployeeCreate):
    employee_data = employee.model_dump()
    result = create_employee(employee_data)

    return {
        "message": "Employee created successfully",
        "employee": result
    }


# GET: Get all employees
@router.get("/")
def fetch_all_employees():
    return get_all_employees()


# GET: Get employee by ID
@router.get("/{employee_id}")
def fetch_employee(employee_id: str):
    employee = get_employee_by_id(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# PUT: Update employee
@router.put("/{employee_id}")
def edit_employee(employee_id: str, employee: EmployeeUpdate):
    employee_data = employee.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    if not employee_data:
        raise HTTPException(
            status_code=400,
            detail="Please provide at least one field to update"
        )

    updated_employee = update_employee(employee_id, employee_data)

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee updated successfully",
        "employee": updated_employee
    }


# DELETE: Delete employee
@router.delete("/{employee_id}")
def remove_employee(employee_id: str):
    deleted = delete_employee(employee_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }
