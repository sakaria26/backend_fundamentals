"""
Connecting to a Relational Database
"""

import pyodbc

connection = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}', server='PRIMEPC\SQLEXPRESS', database='res_system')

cursor = connection.cursor()

choice = input("Select a Option \n(1) Query Data from the database \n(2) Insert Data into the database \nOption: ")

if choice == "1":
    # Reading Data

    READ_QUERY = """
    select * from restaurant;
    """

    cursor.execute(READ_QUERY)

    records = cursor.fetchall()
    for record in records:
        print(f"{record.id}\t{record.restaurant_name}\t{record.phone_number}")
elif choice == "2":
    # Creating Data

    title = input("Enter the title of the Reservation: ")
    reservation_date = input("Enter the date of the Reservation: ")
    start_time = input("Enter the starting time of the Reservation: ")
    party_size = int(input("Enter the size of the Reservation Party: "))
    contact_number = input("Enter the contact number of the Reservation: ")
    table_number = input("Enter the table of the Reservation: ")
    restaurant_id = 100
    waiter_id = 100

    CREATE_QUERY = """
    insert into reservation
    (title, reservation_date, start_time, party_size, contact_number, table_number, restaurant_id, waiter_id) output inserted.id
    values (?, ?, ?, ?, ?, ?, ?, ?);
    """

    cursor.execute(
        CREATE_QUERY,
        title,
        reservation_date,
        start_time,
        party_size,
        contact_number,
        table_number,
        restaurant_id,
        waiter_id
    )

    resultId = cursor.fetchval()
    print(f"Inserted Reservation ID : {resultId}")
    connection.commit()