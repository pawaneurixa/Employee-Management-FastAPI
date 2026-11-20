from fastapi import FastAPI
from app.database import check_database_connection
from app.routes.employees import router as employee_router

app = FastAPI(title="Employee Management System")


@app.on_event("startup")
def startup_event():
    check_database_connection()


app.include_router(employee_router)


@app.get("/")
def home():
    return {"message": "Employee Management System API is running"}