-- Creating Database
CREATE DATABASE employee_database;

USE employee_database;

-- employee table-----------------------------------------------------------
CREATE TABLE employee_table(
	emp_id		int	 			NOT NULL	IDENTITY(1,1)	PRIMARY KEY,
	id			char(25)		NOT NULL,
	f_name		varchar(50)		NOT NULL,
	l_name		varchar(50)		NOT NULL,
	nic			varchar(15)		NOT NULL,
	phone		varchar(15)		NOT NULL,
	emp_image	varbinary(max)	

);

-- project Table-----------------------------------------------------------
CREATE TABLE project_table(	
	pro_id		int				NOT NULL	IDENTITY(1,1)	PRIMARY KEY,
	pro_name	varchar(50)		NOT NULL,
);


-- allocation Table to combine assigned employees to projects--------------
CREATE TABLE allocation_table(
	id			int				NOT NULL	IDENTITY(1,1)	PRIMARY KEY,
	pro_id		int				NOT NULL	FOREIGN KEY	REFERENCES project_table(pro_id),
	emp_id		int				NOT NULL	FOREIGN KEY	REFERENCES employee_table(emp_id),
	as_from		date			NOT NULL,
	as_to		date			NOT NULL,
);

