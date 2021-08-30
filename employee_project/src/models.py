from sqlalchemy import ForeignKey, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base





""" -------------------------------------------------------------
    Employee Model
---------------------------------------------------------------"""
class Employee(Base): 
    __tablename__ = "employee_table"

    emp_id = Column(Integer, primary_key = True, index = True)
    id = Column(String, unique = True, index = True )
    f_name = Column(String, index = True)
    l_name = Column(String, index = True)
    nic = Column(String,unique = True, index = True)
    phone = Column(String,unique = True, index = True)
# ----------add a image datatype to the below column---------------------
    emp_image =  Column()

    allocation = relationship("Allocation", back_populates = "employee")



""" -------------------------------------------------------------
    Project Model
---------------------------------------------------------------"""
class Project(Base):
    __tablename__ = "project_table"

    pro_id =  Column(Integer, primary_key = True, index = True)
    # id = Column(String, unique = True, index = True)
    pro_name = Column(String, unique = True, index = True)

    allocation = relationship("Allocation", back_populates = "project")



""" -------------------------------------------------------------
    Allocation Model
---------------------------------------------------------------"""
class  Allocation(Base):
    __tablename__ = "allocation_table"

    id = Column(Integer, primary_key = True, index = True)
    pro_id = Column(Integer,  ForeignKey("project_table.pro_id"))
    emp_id = Column(Integer, ForeignKey("employee_table.emp_id"))
    as_from = Column(Date)
    as_to = Column(Date)

    employee = relationship("Employee", back_populates = "allocation")
    project = relationship("Project", back_populates = "allocation")


