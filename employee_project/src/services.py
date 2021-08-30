
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas


"""-----------------------------------------------------------------------------------------------------------------------------------------------------
                                        Employees
-----------------------------------------------------------------------------------------------------------------------------------------------------"""


"""
        Read
"""
def  get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()



def get_employee_by_id(db: Session, id: str):
    return db.query(models.Employee).filter(models.Employee.id == id).first()



def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()
 


"""
        Create 
"""
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        id = employee.id,
        f_name = employee.f_name,
        l_name = employee.l_name,
        nic = employee.nic,
        phone = employee.phone
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee



"""-----------------------------------------------------------------------------------------------------------------------------------------------------
                                        Project
-----------------------------------------------------------------------------------------------------------------------------------------------------"""

  
"""
        Read 
"""
def get_project(db: Session, pro_id: int ):
    return db.query(models.Project).filter(models.Project.pro_id == pro_id).first()



def get_project_by_name(db: Session, pro_name: str ):
    return db.query(models.Project).filter(models.Project.pro_name == pro_name).first()



def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()



"""
        Create 
"""
def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(pro_name = project.pro_name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project



"""-----------------------------------------------------------------------------------------------------------------------------------------------------
                                        Allocations
-----------------------------------------------------------------------------------------------------------------------------------------------------"""


"""
        Read 
"""
def get_allocations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Allocation).offset(skip).limit(limit).all()



"""
        Create 
"""
def create_allocation(db: Session, allocation: schemas.AllocationCreate):
    db_allocation = models.Allocation(
        pro_id = allocation.pro_id,
        emp_id = allocation.emp_id,
        as_from = allocation.as_from,
        as_to = allocation.as_to
        )
    db.add(db_allocation)
    db.commit()
    db.refresh(db_allocation)
    return db_allocation

