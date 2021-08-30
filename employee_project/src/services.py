
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import asc, or_
from sqlalchemy.sql.functions import mode
from . import models, schemas


"""-----------------------------------------------------------------------------------------------------------------------------------------------------
                                        Employees
-----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""
        Read
"""
#------------ Read by emp_id------------------------------------------------------------------------------------------
def  get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()



#------------ Read by id-----------------------------------------------------------------------------------------------
def get_employee_by_id(db: Session, id: str):
    return db.query(models.Employee).filter(models.Employee.id == id).first()



#------------ Read by name---------------------------------------------------------------------------------------------
def get_employee_by_name(db: Session, name: str):
    return db.query(models.Employee).filter(or_(models.Employee.f_name == name, models.Employee.l_name == name)).all()



#------------ Read all employees---------------------------------------------------------------------------------------
def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).order_by(asc(models.Employee.emp_id)).offset(skip).limit(limit).all()
 


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
#------------ Read by pro_id-------------------------------------------------------------------------------------
def get_project_by_id(db: Session, pro_id: int ):
    return db.query(models.Project).filter(models.Project.pro_id == pro_id).first()



#------------ Read by pro_name-----------------------------------------------------------------------------------
def get_project_by_name(db: Session, pro_name: str ):
    return db.query(models.Project).filter(models.Project.pro_name == pro_name).first()



#------------ Read all Projects----------------------------------------------------------------------------------
def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).order_by(asc(models.Project.pro_id)).offset(skip).limit(limit).all()



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
#------------ Read by pro_ID------------------------------------------------------------------------------------
def get_allocations_by_pro_id(db: Session, pro_id: str ):
    return db.query(models.Allocation).filter(models.Allocation.pro_id == pro_id).all()



#------------ Read by emp_id------------------------------------------------------------------------------------
def get_allocations_by_emp_id(db: Session, emp_id: str ):
    return db.query(models.Allocation).filter(models.Allocation.emp_id == emp_id).all()



#------------ Read all Projects----------------------------------------------------------------------------------
def get_allocations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Allocation).order_by(models.Allocation.id).offset(skip).limit(limit).all()



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

