import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="111",
    database="Bank"
)

print("Connected Successfully!")

mycursor = conn.cursor()


def customerDetails():
    print("\nCustomer Details")

    ch = "y"

    while ch.lower() == "y":

        cname = input("Enter Customer Name: ")
        cnum = input("Enter Customer Contact Number: ")
        cadd = input("Enter Customer Address: ")
        cid = int(input("Enter Customer ID: "))
        panno = input("Enter Customer PAN No: ")
        accountno = int(input("Enter Customer Account No: "))

        sql = """
        INSERT INTO customer
        (cname,cnum,cadd,cid,panno,accountno)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (cname, cnum, cadd, cid, panno, accountno)

        mycursor.execute(sql, values)
        conn.commit()

        print("Customer Added Successfully!")

        ch = input("Do you want to add another customer? (y/n): ")

    Bankmenu()


def accountopen():
    print("\nAccount Opening")

    accountno = int(input("Enter Account Number: "))
    cid = int(input("Enter Customer ID: "))

    print("\nSelect Account Type")
    print("1. Saving Account")
    print("2. Current Account")

    cp = int(input("Enter Choice: "))

    if cp == 1:
        at = "Saving"
        amt = 2000

    elif cp == 2:
        at = "Current"
        amt = 10000

    else:
        print("Invalid Choice")
        Bankmenu()
        return

    status = "Active"

    sql = """
    INSERT INTO account
    (accountno,cid,at,amt,status)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (accountno, cid, at, amt, status)

    mycursor.execute(sql, values)
    conn.commit()

    print("Account Opened Successfully!")
    Bankmenu()


def cancel():
    print("\nDelete Account")

    accountno = int(input("Enter Account Number: "))

    sql = "UPDATE account SET status='Deleted' WHERE accountno=%s"

    mycursor.execute(sql, (accountno,))
    conn.commit()

    print("Account Deleted Successfully!")

    Bankmenu()


def displayCustomerDetails():
    print("\nCustomer Records\n")

    try:
        mycursor.execute("SELECT * FROM customer")

        records = mycursor.fetchall()

        if len(records) == 0:
            print("No Records Found")

        for row in records:
            print(row)

    except Exception as e:
        print("Error:", e)

    Bankmenu()


def Bankmenu():

    print("\n==============================")
    print("      BANK MANAGEMENT")
    print("==============================")
    print("1. Customer Detail")
    print("2. Account Opening")
    print("3. Deletion of Account")
    print("4. Display Customer Details")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customerDetails()

    elif choice == 2:
        accountopen()

    elif choice == 3:
        cancel()

    elif choice == 4:
        displayCustomerDetails()

    elif choice == 5:
        print("Thank You!")
        conn.close()
        exit()

    else:
        print("Invalid Choice")
        Bankmenu()


Bankmenu()