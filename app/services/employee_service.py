
from bson import ObjectId
from bson.errors import InvalidId

from app.database import employee_collection
from app.models.employee import employee_helper


def create_employee(employee_data: dict):
    result = employee_collection.insert_one(employee_data)
    new_employee = employee_collection.find_one(
        {"_id": result.inserted_id}
    )
    return employee_helper(new_employee)


# GET: Fetch all employees
def get_all_employees():
    employees = employee_collection.find()
    return [employee_helper(employee) for employee in employees]


# GET: Fetch employee by ID
def get_employee_by_id(employee_id: str):
    try:
        employee = employee_collection.find_one(
            {"_id": ObjectId(employee_id)}
        )
    except (InvalidId, TypeError):
        return None

    if employee:
        return employee_helper(employee)

    return None


# PUT: Update employee
def update_employee(employee_id: str, employee_data: dict):
    try:
        object_id = ObjectId(employee_id)
    except (InvalidId, TypeError):
        return None

    result = employee_collection.update_one(
        {"_id": object_id},
        {"$set": employee_data}
    )

    if result.matched_count == 0:
        return None

    updated_employee = employee_collection.find_one(
        {"_id": object_id}
    )

    return employee_helper(updated_employee)


# DELETE: Delete employee
def delete_employee(employee_id: str):
    try:
        object_id = ObjectId(employee_id)
    except (InvalidId, TypeError):
        return False

    result = employee_collection.delete_one(
        {"_id": object_id}
    )

    return result.deleted_count > 0
