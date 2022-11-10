import mysql.connector


def menu():
    print('[1] Display tables')
    print('[2] Add Instructor')
    print('[3] Display instructor classes')
    print('[4] Add a class to instructor')
    print('[5] Test')

menu()
option = int(input('What would you like to do?\n'))

def option1():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='assignment2'
    )
    cursor = db.cursor()
    table = input('What table would you like to see?\n')

    if table == 'instructor':
        cursor.execute('select * from instructor')
    elif table == 'classroom':
        cursor.execute('select * from classroom')
    elif table == 'course':
        cursor.execute('select * from course')
    elif table == 'department':
        cursor.execute('select * from department')
    elif table == 'advisor':
        cursor.execute('select * from advisor')
    elif table == 'prereq':
        cursor.execute('select * from prereq')
    elif table == 'section':
        cursor.execute('select * from section')
    elif table == 'student':
        cursor.execute('select * from student')
    elif table == 'takes':
        cursor.execute('select * from takes')
    elif table == 'teaches':
        cursor.execute('select * from teaches')
    elif table == 'time_slot':
        cursor.execute('select * from instructor')
    else:
        print('Invalid Choice. Please select a viable option.')



    for x in cursor:
        print(x)

# option1 code

def option2():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='assignment2'
    )

    cursor = db.cursor()
    ID=int(input('Enter Instructor ID\n'))
    name=input("Enter instructor name\n")
    dept_name=input("Enter Instructor Department\n")
    salary=input('Enter instructor salary\n')

    insert='INSERT INTO instructor VALUES (%s,%s,%s,%s)'

    value=(ID,name,dept_name,salary)



    cursor.execute(insert,value)

    db.commit()
    print('Your record has been added to the instructor table')

# option2 code

def option3():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='assignment2'
    )
    cursor = db.cursor()
    ID = int(input("Please Enter instructor ID:\n"))

    teaches = "SELECT course_id, ID FROM teaches where ID=%s AND semester = 'Fall' AND year = 2022"


    cursor.execute(teaches, (ID, ))
    for x in cursor:
        print(x)

# option3 code

def option4():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='assignment2'
    )
    cursor = db.cursor()

    print("First we need course Information\n")
    course_id = input("Enter course_id:\n")
    title = input("Enter course title:\n")
    dept_name = input('Enter Department Name:\n')
    budget = int(input('Enter department Budget\n'))
    credits = input("Enter Amount of Credits:\n")

    insert_course = 'INSERT INTO course VALUES (%s,%s,%s,%s)'
    course_info = (course_id, title, dept_name, credits)

    ID = input('Please enter teacher ID:')



    try:
        cursor.execute(insert_course, course_info)
    except Exception as e:
        print(e)

#option4 Code

def option5():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='assignment2'
    )
    cursor = db.cursor()
    table = int(input('Please Enter Instructor ID:\n'))
    query='select course_id from teaches'
    try:
        cursor.execute(query, (table, ))
    except Exception as e:
        print(e)




if option == 1:
    option1()
elif option == 2:
    option2()
elif option == 3:
    option3()
elif option == 4:
    option4()
elif option == 5:
    option5()
else:
    print('Invalid Choice. Please select a viable option.')









