# packages : 
Creating and using packages are covered.  
The following packages that are created and then used in main.py file are as follows : 
1. drivers
2. dictionary
3. list_custom [List comprehension]
4. loop [break, continue, range]
5. operators
6. sets
7. strings [regex library]
8. tuples   

# classes, constructors, (getters and setters), methods, private variables, __private methods, Abstraction , Type casting:
[Classes,constructors, (getters and setters), methods, Abstraction, Type casting] have been used in all the files inside packages as listed below : 
1. drivers
2. dictionary
3. list_custom [List comprehension]
4. loop [break, continue, range]
5. operators
6. sets
7. strings [regex library]
8. tuples  

# Inheritance, Polymorphism, Encapsulation, Class variables:
[Inheritance, Polymorphism, Encapsulation, Class variables] have been used in the solution.py file inside a class_oop folder :  
NOTE: class_oop is not a package it's just a folder
1. solution.py

# magic methods:
Magic methods are those methods that can't be created by us but we can use them to create some new things to meet our requirements for example creating a fraction datatype:
used in Operator package in files as listed below : 
1. fraction  
2. fraction_calculator (used this fraction datatype in here) 

# conditional statements, loops [break, range] and Exceptions: 
Conditional statements are used to drive menu driven programs
the files where conditional statements are used are listed below : 
### Stand alone files
1. main.py 
### Packages : 
A. drivers : files inside this package uses conditional statements and loops to drive the menu system :
1. driver_dictionary 
2. driver_list
3. driver_loop
4. driver_operator
5. driver_sets
6. driver_string
7. driver_tuples  
  
B. operators : files inside this package uses conditional statements and loops to drive the menu system :
1. calculator
2. fraction_calculator
3. unit_converter

# generators : 
generator folder is not a package it's a simple folder that contains some examples of generators: 
1. example_0
2. example_1
3. example_2

# args and kwargs : 
args_kwargs folder holds the programs related to args and kwargs:
args_akwargs :
1. example_0
2. example_1  
A. args  
1. example_1
2. example_2
3. example_3  
B. kwargs
1. example1
2. example2
3. example3

# decorators [@property, @classmethod, @staticmethod, @name.setter]:
decorators folders holds the files that demonstrate how to use python decorators.  
It is inside a folder called simple_folder : 
1. item
2. main
3. phone

# dictionary and dictionary comprehension :
dictionary package contains all the programs related to dictionary and dictionary comprehension :  
A. dictionary  
1. dictionary_comprehension [single and nested dictionary comprehension]

# [creating a date object, current date, date output , date formatting] dates : 
python dates are in a folder called dates inside simple_folders :  
A. simple_folders  
1. dates

# os module:
os module folder is inside simple_folders
1. change_directory
2. create_directory
3. create_multiple_directories
4. delete_directory_files
5. get_current_working_directory
6. get_os_name
7. list_files_directories
8. os_errors
10. read_write_files
11. rename_files
12. remove_files
13. check_if_path_exists
14. get_file_size

# Postgres Database : 
### create a table with a column of primary key with auto increment 
```
(normally)
CREATE TABLE YourTableName (
    id INT IDENTITY(1,1) PRIMARY KEY,
    other_column VARCHAR(255),
    another_column INT
);

(in case of postgres)
CREATE TABLE IF NOT EXISTS student (
	id SERIAL PRIMARY KEY,
	student_name VARCHAR(50),
	roll_number INT
);
```

### create a table with a column of primary key and foreign key
```
CREATE TABLE parent_table (
    parent_id SERIAL PRIMARY KEY,
    parent_name VARCHAR(100)
);

CREATE TABLE child_table (
    child_id SERIAL PRIMARY KEY,
    child_name VARCHAR(100),
    parent_id INT REFERENCES parent_table(parent_id)
);
```
### alter an existing table to add a constraint in a column
```
CREATE TABLE IF NOT EXISTS student_profile (
	id SERIAL PRIMARY KEY,
	student_pk INT REFERENCES student(id),
	address VARCHAR(255),
	phone_number BIGINT
);

INSERT INTO student_profile(student_pk, address, phone_number) VALUES
(1,'Lucknow',8887634464),
(2,'Chandigarh',9451907083),
(3,'Kolkata',9451907102),
(4,'Chennai',8004224178),
(5,'Mumbai',8896298052);
ALTER TABLE student_profile
ADD CONSTRAINT unique_student_pk UNIQUE (student_pk);
```
### stodred procedures
```
/*
table (parent table) with auto-increment primary key column
create, insert and select all 
*/
CREATE TABLE IF NOT EXISTS student (
	id SERIAL PRIMARY KEY,
	student_name VARCHAR(50),
	roll_number INT
);
/*
CREATE a stored procedure for student table
INSERT , SELECT_ALL, UPDATE, DELETE
*/
CREATE OR REPLACE PROCEDURE insert_student(
	IN student_name_var VARCHAR(50),
	IN roll_number_var INT
)
LANGUAGE SQL
AS $$
INSERT INTO student(student_name, roll_number) VALUES
(student_name_var, roll_number_var);
$$;

CREATE OR REPLACE PROCEDURE select_all_student()
	RETURNS TABLE(id int, student_name VARCHAR(50), roll_number = INT)
LANGUAGE SQL
AS $$
SELECT * FROM student;
$$;

CREATE OR REPLACE PROCEDURE update_student(
	IN id_var INT,
	IN student_name_var VARCHAR(50),
	IN roll_number_var INT
)
LANGUAGE SQL
AS $$
UPDATE student SET student_name = student_name_var , roll_number = roll_number_var WHERE id = id_var;
$$;

CREATE OR REPLACE PROCEDURE delete_student(
	IN id_var INT
)
LANGUAGE SQL
AS $$
DELETE FROM student WHERE id = id_var;
$$
/*
CALL stored procedures for student table
INSERT , SELECT_ALL, UPDATE, DELETE
*/
CALL insert_student('Dynamite', 911);
CALL update_student(7,'Kombat', 365);
CALL delete_student(7);

CALL select_all_student(); --The stored procedures in postgres do not return a table It only happen in Microsoft SQL
SELECT * FROM student;
```
### Use triggers and carry out calculations via trigger functions
create a table named student_marks:  
```
CREATE TABLE IF NOT EXISTS student_marks (
	id SERIAL PRIMARY KEY,
	student_pk INT REFERENCES student(id),
	maths NUMERIC(10,2),
	physics NUMERIC(10,2),
	chemistry NUMERIC(10,2),
	english NUMERIC(10,2),
	hindi NUMERIC(10,2),
	computer NUMERIC(10,2),
	total NUMERIC(10,2),
	percentage NUMERIC(10,2)
    );
```  
#### Before insert Trigger (before insert operation)
trigger to detect the insert operation on student_marks table  
```
CREATE TRIGGER calculate_marks_and_percentage
BEFORE INSERT ON student_marks
FOR EACH ROW
EXECUTE FUNCTION calculate_total_and_percentage();
```  
trigger function to calculate the total and percentage of the marks present in a student_marks table  
```
CREATE OR REPLACE FUNCTION calculate_total_and_percentage()
RETURNS TRIGGER AS $$
BEGIN
    NEW.total := NEW.maths + NEW.physics + NEW.chemistry + NEW.english + NEW.hindi + NEW.computer;
    NEW.percentage := (NEW.total / 600) * 100; -- Assuming total marks for all subjects is 600
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```  
Explaination :  
```CREATE OR REPLACE FUNCTION calculate_total_and_percentage()```  
This line initiates the creation or replacement of a PostgreSQL function named calculate_total_and_percentage(). Functions in PostgreSQL are named blocks of code that perform a specific task when called.

```RETURNS TRIGGER AS $$```  
This line specifies that the function returns a TRIGGER. In PostgreSQL, a trigger is a set of actions that are automatically performed when certain database events occur on a specified table or view.

```BEGIN ... END;```  
This block encapsulates the main body of the function. All the actions that the function performs are contained within this block.

```NEW.total := NEW.maths + NEW.physics + NEW.chemistry + NEW.english + NEW.hindi + NEW.computer;```  
This line calculates the total marks obtained by adding the marks obtained in various subjects. The keyword NEW refers to the new row that triggered the function. This function seems to be designed to be used as an insert or update trigger, calculating the total marks whenever a new row is inserted or updated in the table.

```NEW.percentage := (NEW.total / 600) * 100;```  
This line calculates the percentage of marks obtained by dividing the total marks by the maximum possible marks (in this case, 600) and then multiplying by 100 to convert it into a percentage.

```RETURN NEW;```  
This line indicates that the function should return the modified row (NEW) after the calculations are done. This is important for trigger functions, as it allows the modified row to be written back to the table after any necessary modifications.

```$$ LANGUAGE plpgsql;```  
This line concludes the function definition. The $$ is a delimiter that marks the beginning and end of the function's body. LANGUAGE plpgsql specifies that the function is written in PL/pgSQL, which is a procedural language extension for PostgreSQL.  

Now if we insert something in the table then the total marks and percentage will be calculated before the insert operation takes place in the database  
```
INSERT INTO student_marks (student_pk, maths ,physics ,chemistry ,english ,hindi ,computer ) VALUES
(1,99,97,95,80,92,100),
(2,85,89,75,72,84,70),
(3,60,55,65,80,76,92),
(4,55,40,40,32,60,85),
(5,100,100,100,32,90,100);

SELECT * FROM student_marks
```  
output:  
![](postgres_database/related_images/result_1_for_triggers_with_procedures.png)  

### create a TRIGGER FUNCTION to count all the rows in the student table and call that trigger function after the insert operation (after insert operation)
```
/* TRIGGER FUNCTION */
CREATE OR REPLACE FUNCTION total_students()
RETURNS TRIGGER AS $$
DECLARE
    total_rows INTEGER;
BEGIN
    -- Count the number of rows in the student table
    SELECT count(*) INTO total_rows FROM student;
    
    -- Display the count
    RAISE NOTICE 'Number of rows in student table: %', total_rows;
    
    RETURN NULL; -- Return NULL to indicate that the trigger is done
END;
$$ LANGUAGE plpgsql;
```
Explanation : 
```CREATE OR REPLACE FUNCTION count_student_rows()```  
This line initiates the creation or replacement of a PostgreSQL function named count_student_rows().
```RETURNS TRIGGER AS $$```  
This line specifies that the function returns a TRIGGER. In PostgreSQL, a trigger function is invoked automatically when a specified event occurs on a table, and it can perform actions based on that event.
```DECLARE total_rows INTEGER;```  
This line declares a local variable named total_rows of type INTEGER. This variable will store the count of rows in the student table.
```BEGIN ... END;```  
This block encapsulates the main body of the function. All the actions that the function performs are contained within this block.
```SELECT count(*) INTO total_rows FROM student;```  
This line executes a SQL query to count the number of rows in the student table and stores the result in the total_rows variable. The count(*) function returns the number of rows in the specified table.
```RAISE NOTICE 'Number of rows in student table: %', total_rows;```  
This line raises a notice message, displaying the count of rows in the student table. The % acts as a placeholder for the value of the total_rows variable, which will be dynamically inserted into the notice message.
```RETURN NULL;```  
This line returns NULL to indicate that the trigger function has completed its execution. Since this trigger function is designed to be an AFTER trigger (i.e., it doesn't modify the data being inserted or updated), it returns NULL.
```$$ LANGUAGE plpgsql;```  
This line concludes the function definition. The $$ is a delimiter that marks the beginning and end of the function's body. LANGUAGE plpgsql specifies that the function is written in PL/pgSQL, which is a procedural language extension for PostgreSQL.
#### RAISE : 
The RAISE statement is similar to a print statement. It's primarily used for debugging purposes or to provide informational messages during the execution of functions, triggers, or procedures.  
There are several variants of the RAISE statement:

```RAISE NOTICE```: This variant is commonly used to display informational messages. These messages are displayed in the PostgreSQL log if the logging configuration includes the LOG_NOTICE level. They are also displayed to the client if the client has enabled verbose messages.

```RAISE WARNING```: This variant is used to display warning messages. These messages are displayed similarly to RAISE NOTICE, but at a higher level of severity.

```RAISE EXCEPTION```: This variant is used to raise an exception. It can be used to abort the execution of a function, trigger, or procedure and report an error to the client.

```RAISE DEBUG```: This variant is used to display debug messages. These messages are displayed in the PostgreSQL log if the logging configuration includes the LOG_DEBUG level.  

```
/* TRIGGER (after insert operation) */
CREATE TRIGGER after_insert_student
	AFTER INSERT ON student
	FOR EACH STATEMENT
	EXECUTE FUNCTION total_students();
/* USING STORED PROCEDURE TO INSERT A STUDENT IN student table */
CALL insert_student('Dynamite', 911);
```  
This trigger will get activated after the insert operation is complete.
### CREATE a trigger that prints the entire table after the insert operation is complete .CREATE a trigger function that selects all rows of the table and prints it (after insert operation)
```
/* TRIGGER FUNCTION */
CREATE OR REPLACE FUNCTION print_student()
RETURNS TRIGGER AS $$
	DECLARE
    student_record student%ROWTYPE; -- Define a record variable to hold a single row of the student table
BEGIN
    -- Print the contents of the student table
    RAISE NOTICE 'Contents of student table after insert:';
    FOR student_record IN SELECT * FROM student LOOP
        RAISE NOTICE 'id: %, student_name: %, roll_number: %', student_record.id, student_record.student_name, student_record.roll_number;
    END LOOP;
    
    RETURN NULL; -- Return NULL to indicate that the trigger is done
END;
$$ LANGUAGE plpgsql;
```
explanation : 
```CREATE OR REPLACE FUNCTION print_student()```:  
This line initiates the creation or replacement of a PostgreSQL function named print_student().
```RETURNS TRIGGER AS $$```:  
This line specifies that the function returns a TRIGGER. In PostgreSQL, a trigger function is invoked automatically when a specified event occurs on a table, and it can perform actions based on that event.
```DECLARE student_record student%ROWTYPE;```:  
This line declares a local variable named student_record of type student%ROWTYPE. The %ROWTYPE is a special data type in PostgreSQL that represents a whole row of a table. So, student_record will hold a single row from the student table.
```BEGIN ... END;```:  
This block encapsulates the main body of the function. All the actions that the function performs are contained within this block.
```RAISE NOTICE 'Contents of student table after insert:';```:  
This line raises a notice message indicating that the contents of the student table are about to be printed.
```FOR student_record IN SELECT * FROM student LOOP```:  
This line initiates a loop that iterates over each row in the student table. The SELECT * FROM student query fetches all rows from the student table, and the loop iterates over each of these rows.
```RAISE NOTICE 'id: %, student_name: %, roll_number: %', student_record.id, student_record.student_name, student_record.roll_number;```:  
Within the loop, this line raises a notice message for each row in the student table. It displays the id, student_name, and roll_number fields of the current row using the values stored in the student_record variable.
```RETURN NULL;```:  
This line returns NULL to indicate that the trigger function has completed its execution. Since this trigger function is designed to be an AFTER trigger, it doesn't need to return any data to the caller.
```$$ LANGUAGE plpgsql;```:  
This line concludes the function definition. The $$ is a delimiter that marks the beginning and end of the function's body. LANGUAGE plpgsql specifies that the function is written in PL/pgSQL, which is a procedural language extension for PostgreSQL.

```
/* TRIGGER (after insert operation) */
CREATE TRIGGER display_student_table_after_insert
AFTER INSERT ON student
FOR EACH STATEMENT
EXECUTE FUNCTION print_student();
```
calling stored procedure to insert a row.  
```
/* USING STORED PROCEDURE TO INSERT A STUDENT IN student table */
CALL insert_student('Dynamite', 911);
```
output:  
```
NOTICE: Contents of student table after insert: NOTICE: id: 1, student_name: Rollex, roll_number: 997 
NOTICE: id: 2, student_name: Ballistic, roll_number: 1000 NOTICE: id: 3, student_name: Barbatos, roll_number: 117 
NOTICE: id: 4, student_name: Barricade, roll_number: 247 NOTICE: id: 5, student_name: Bullet, roll_number: 567 
NOTICE: id: 9, student_name: Dynamite, roll_number: 911 NOTICE: id: 10, student_name: Dynamite, roll_number: 911 
NOTICE: id: 11, student_name: Dynamite, roll_number: 911
```


