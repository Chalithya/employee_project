from datetime import date
from  typing import Optional, List
from pydantic import  BaseModel
from sqlalchemy.sql.expression import true




""" ------------------------------------------------------------------
            This is Employee Schema
    ----------------------------------------------------------------"""
class EmployeeBase(BaseModel):
    id: str
    f_name: str
    l_name: str
    nic: str
    phone: str
  


class EmployeeCreate(EmployeeBase):
    pass



class Employee(EmployeeBase):
    emp_id: int
# -----------Add correct data type for image----------------------------
    # emp_image: bytes

    class Config:
        orm_mode = True



""" ------------------------------------------------------------------
            This is Project Schema
    ----------------------------------------------------------------"""
class ProjectBase(BaseModel):
    pro_name: str



class ProjectCreate(ProjectBase):
    pass



class Project(ProjectBase):
    pro_id: int

    class Config:
        orm_mode = True


""" ------------------------------------------------------------------
            This is Allocation Schema
    ----------------------------------------------------------------"""
class AllocationBase(BaseModel):
    pro_id: int
    # emp_id: List[Employee] = [] this or the following ?
    emp_id: int
    as_from: date
    as_to: date



class AllocationCreate(AllocationBase):
    pass



class Allocation(AllocationBase):
    id: int

    class Config:
        orm_mode = True