
def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "department": employee["department"],
        "designation": employee["designation"],
        "salary": employee["salary"]
    }
