from typing import List
from fastapi import FastAPI, Depends, HTTPException
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
"""
        Create
"""

@app.post("/employees/", response_model = schemas.Employee, tags=["Employee"])
def create_employee(employee: schemas.EmployeeCreate,  db: Session = Depends(get_db)):
    db_employee = services.get_employee_by_id(db, id = employee.id)
    if db_employee:
        raise HTTPException(status_code = 400, detail = "Employee Id Already Registered")
    
    return services.create_employee(db = db, employee = employee) 



"""
        View
"""
#------------ Read all employees-----------------------------------------------------------------------
@app.get("/employees/", response_model = List[schemas.Employee], tags=["Employee"])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = services.get_employees(db = db, skip = skip, limit = limit)
    return employees



#------------ Read by id ------------------------------------------------------------------------------
@app.get("/employees/{id}", response_model=schemas.Employee, tags=["Employee"])
def read_employee_by_id(id: str, db: Session = Depends(get_db)):
    db_employee = services.get_employee_by_id(db, id = id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee ID Not Found")
    return db_employee



#------------ Read by Name -----------------------------------------------------------------------------
@app.get("/employees/name/{name}", response_model = List[schemas.Employee], tags=["Employee"])
def read_employee_by_name(name: str, db: Session = Depends(get_db)):
    db_employee = services.get_employee_by_name(db, name = name)
    if db_employee == []:
        raise HTTPException(status_code=404, detail="Employee Name Not Found")
    return db_employee





"""---------------------------------------------------------------------------------------------------------------------------------------
                                                             Project 
---------------------------------------------------------------------------------------------------------------------------------------"""
"""
        Create
"""
@app.post("/projects/", response_model = schemas.Project, tags=["Projects"])
def create_project(project: schemas.ProjectCreate,  db: Session = Depends(get_db)):
    db_project = services.get_project_by_name(db, pro_name = project.pro_name)
    if db_project:
        raise HTTPException(status_code = 400, detail = "Project ID already registered")
    
    return services.create_project(db = db, project = project) 



"""
        View
"""
#------------ Read by id ----------------------------------------------------------------------------------
@app.get("/projects/{pro_id}", response_model=schemas.Project, tags=["Projects"])
def read_project_by_id(pro_id: str, db: Session = Depends(get_db)):
    db_project = services.get_project_by_id(db, pro_id = pro_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project Not Found")
    return db_project



#------------ Read by Name --------------------------------------------------------------------------------
@app.get("/projects/name/{pro_name}", response_model=schemas.Project, tags=["Projects"])
def read_project_by_name(pro_name: str, db: Session = Depends(get_db)):
    db_project = services.get_project_by_name(db, pro_name = pro_name)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project Not Found")
    return db_project



#------------ Read All Projects -----------------------------------------------------------------------------
@app.get("/projects/", response_model = List[schemas.Project], tags=["Projects"])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = services.get_projects(db = db, skip = skip, limit = limit)
    return projects



"""---------------------------------------------------------------------------------------------------------------------------------------
                                                             Allocation 
---------------------------------------------------------------------------------------------------------------------------------------"""
"""
        Create
"""
@app.post("/allocation/", response_model = schemas.Allocation, tags=["Allocation"])
def create_allocation(allocation: schemas.AllocationCreate,  db: Session = Depends(get_db)):
    
    return services.create_allocation(db = db, allocation = allocation) 



"""
        View
"""
#------------ Read All Allocation -----------------------------------------------------------------------------
@app.get("/allocation/", response_model = List[schemas.Allocation], tags=["Allocation"])
def read_allocation(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    allocation = services.get_allocations(db = db, skip = skip, limit = limit)
    return allocation



#------------ Read by pro_id ---------------------------------------------------------------------------------
@app.get("/allocation/{pro_id}", response_model = List[schemas.Allocation], tags=["Allocation"])
def read_allocation_by_pro_id(pro_id: str, db: Session = Depends(get_db)):
    db_allocation = services.get_allocations_by_pro_id(db, pro_id = pro_id)
    if db_allocation == []:
        raise HTTPException(status_code=404, detail="Projects Not Found")
    return db_allocation



#------------ Read by emp_id ---------------------------------------------------------------------------------
@app.get("/allocation/emp_id/{emp_id}", response_model = List[schemas.Allocation], tags=["Allocation"])
def read_allocation_by_emp_id(emp_id: str, db: Session = Depends(get_db)):
    db_allocation = services.get_allocations_by_emp_id(db, emp_id = emp_id)
    if db_allocation == []:
        raise HTTPException(status_code=404, detail="Projects Not Found")
    return db_allocation