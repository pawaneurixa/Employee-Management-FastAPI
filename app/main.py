from fastapi import FastAPI
from app.database import check_database_connection

app = FastAPI(title="Employee Management System")


@app.on_event("startup")
def startup_event():
    check_database_connection()


@app.get("/")
def home():
    return {
        "message": "Employee Management System API is running"
    }
