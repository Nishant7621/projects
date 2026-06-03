import mysql.connector
try:
    con = mysql.connector.connect(
        host="localhost",
        user="pythonuser",
        password="111",
        database="company_db"
    )

    cur = con.cursor()
    print("Database Connected Successfully!")

except mysql.connector.Error as err:
    print("Database Connection Error:", err)
    exit()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    salary FLOAT,
    joining_date DATE
)
""")

con.commit()

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        emp_name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        if salary < 0:
            print("Salary cannot be negative!")
            return

        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")

        sql = """
        INSERT INTO employees
        VALUES(%s,%s,%s,%s,%s)
        """

        values = (emp_id, emp_name, department, salary, joining_date)

        cur.execute(sql, values)
        con.commit()

        print("Employee Added Successfully!")

    except mysql.connector.IntegrityError:
        print("Employee ID already exists!")

    except Exception as e:
        print("Error:", e)


def view_employees():

    cur.execute("SELECT * FROM employees")

    records = cur.fetchall()

    if len(records) == 0:
        print("No Employee Records Found")
        return

    print("\nEmployee Records")
    print("-" * 70)

    for row in records:
        print(row)


def search_employee():

    print("\n1. Search by ID")
    print("2. Search by Name")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        emp_id = int(input("Enter Employee ID: "))

        cur.execute(
            "SELECT * FROM employees WHERE emp_id=%s",
            (emp_id,)
        )

    elif choice == 2:

        name = input("Enter Employee Name: ")

        cur.execute(
            "SELECT * FROM employees WHERE emp_name=%s",
            (name,)
        )

    else:
        print("Invalid Choice")
        return

    record = cur.fetchall()

    if record:
        for row in record:
            print(row)
    else:
        print("Employee Not Found")


def update_employee():

    emp_id = int(input("Enter Employee ID to Update: "))

    cur.execute(
        "SELECT * FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    record = cur.fetchone()

    if not record:
        print("Employee Not Found")
        return

    print("\n1. Update Name")
    print("2. Update Department")
    print("3. Update Salary")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        name = input("Enter New Name: ")

        cur.execute(
            "UPDATE employees SET emp_name=%s WHERE emp_id=%s",
            (name, emp_id)
        )

    elif choice == 2:

        dept = input("Enter New Department: ")

        cur.execute(
            "UPDATE employees SET department=%s WHERE emp_id=%s",
            (dept, emp_id)
        )

    elif choice == 3:

        salary = float(input("Enter New Salary: "))

        if salary < 0:
            print("Salary cannot be negative!")
            return

        cur.execute(
            "UPDATE employees SET salary=%s WHERE emp_id=%s",
            (salary, emp_id)
        )

    else:
        print("Invalid Choice")
        return

    con.commit()

    print("Record Updated Successfully!")


def delete_employee():

    emp_id = int(input("Enter Employee ID to Delete: "))

    cur.execute(
        "SELECT * FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    record = cur.fetchone()

    if not record:
        print("Employee Not Found")
        return

    cur.execute(
        "DELETE FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    con.commit()

    print("Employee Deleted Successfully!")


def reports():

    print("\n===== REPORTS =====")

    # Total Employees
    cur.execute("SELECT COUNT(*) FROM employees")
    total = cur.fetchone()[0]

    print("Total Employees =", total)

    # Highest Salary Employee
    cur.execute("""
    SELECT *
    FROM employees
    WHERE salary=
    (SELECT MAX(salary) FROM employees)
    """)

    record = cur.fetchone()

    if record:
        print("\nHighest Salary Employee")
        print(record)

    # Department Wise Count
    print("\nEmployees Department Wise")

    cur.execute("""
    SELECT department, COUNT(*)
    FROM employees
    GROUP BY department
    """)

    data = cur.fetchall()

    for dept, count in data:
        print(dept, "=", count)


while True:

    print("\n")
    print("===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Reports")
    print("7. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_employee()

        elif choice == 2:
            view_employees()

        elif choice == 3:
            search_employee()

        elif choice == 4:
            update_employee()

        elif choice == 5:
            delete_employee()

        elif choice == 6:
            reports()

        elif choice == 7:
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please Enter Valid Number")


cur.close()
con.close()