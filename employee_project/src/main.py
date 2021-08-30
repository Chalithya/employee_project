from typing import List
from fastapi import FastAPI, Depends, HTTPException
# import services as services
from sqlalchemy.orm import Session

from . import services, models, schemas
from .database import SessionLocal, engine



models.Base.metadata.create_all(bind = engine)

app = FastAPI()


#Dependacy creation
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""---------------------------------------------------------------------------------------------------------------------------------------
                                                            Employee
---------------------------------------------------------------------------------------------------------------------------------------"""

@app.post("/employees/", response_model = schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate,  db: Session = Depends(get_db)):
    db_employee = services.get_employee_by_id(db, id = employee.id)
    if db_employee:
        raise HTTPException(status_code = 400, detail = "Employee Id already registered")
    
    return services.create_employee(db = db, employee = employee) 



# @app.get("/employees/", response_model = List[schemas.Employee])
# def read_employee(skip: int = 0, limit: int = 100, db: Session = Depends[get_db]):
#     employees = services.get_employees(db, skip = skip, limit = limit)
#     return employees



"""---------------------------------------------------------------------------------------------------------------------------------------
                                                             Project 
---------------------------------------------------------------------------------------------------------------------------------------"""

@app.post("/projects/", response_model = schemas.Project)
def create_project(project: schemas.ProjectCreate,  db: Session = Depends(get_db)):
    db_project = services.get_project_by_name(db, pro_name = project.pro_name)
    if db_project:
        raise HTTPException(status_code = 400, detail = "Project ID already registered")
    
    return services.create_project(db = db, project = project) 




"""---------------------------------------------------------------------------------------------------------------------------------------
                                                             Allocation 
---------------------------------------------------------------------------------------------------------------------------------------"""

@app.post("/allocation/", response_model = schemas.Allocation)
def create_allocation(allocation: schemas.AllocationCreate,  db: Session = Depends(get_db)):
    
    return services.create_allocation(db = db, allocation = allocation) 
