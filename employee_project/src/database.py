from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import pymssql


# mssql+pymssql://<username>:<password>@<freetds_name>/?charset=utf8
# SQLALCHEMY_DATABASE_URL = "mssql+pymssql://FLOKI:@postgresserver/employee_database"

SQLALCHEMY_DATABASE_URL = "mssql+pymssql://FLOKI/employee_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()