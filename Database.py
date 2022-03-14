from mariadb import connect

if __name__ == '__main__':
    user=input("Enter username: ")
    password=input("Enter password: ")
    db=input("Enter database name: ")
    connection=connect(user=user,password=password,db=db)
    cursor=connection.cursor()

    #Creating table Student.
    cursor.execute("CREATE TABLE Student(RollNo INT,Name VARCHAR(20), CLASS INT(2),SECTION VARCHAR(1))")

    #Adding a column contact int(10) to table Student.
    cursor.execute("ALTER TABLE Student ADD COLUMN CONTACT INT(10)")

    #Inserting data into table Student.
    while(True):
        rollno=int(input("Enter roll number: "))
        name=input("Enter name: ")
        class_=int(input("Enter class: "))
        section=input("Enter section: ")
        contact=int(input("Enter contact: "))
        cursor.execute("INSERT INTO Student VALUES(%d,'%s',%d,'%s',%d)",(rollno,name,class_,section,contact))
        print("Data inserted successfully.")
        choice=input("Do you want to continue? (y/n): ")
        if(choice=='n'):
            break
    connection.commit()

    #Searching a record from table Student.
    name=input("Enter name: ")
    cursor.execute("SELECT * FROM Student WHERE Name='%s'",(name))
    row=cursor.fetchone()
    if(row==None):
        print("Record not found.")
    else:
        print("Record found.")

    #Displaying the record.
    print("RollNo: ",row[0])
    print("Name: ",row[1])
    print("Class: ",row[2])
    print("Section: ",row[3])
    print("Contact: ",row[4])

    #Displaying all the records.
    cursor.execute("SELECT * FROM Student")
    rows=cursor.fetchall()
    for row in rows:
        print("RollNo: ",row[0])
        print("Name: ",row[1])
        print("Class: ",row[2])
        print("Section: ",row[3])
        print("Contact: ",row[4])
        print("----------------------------------")

