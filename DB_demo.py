import sqlite3
from Employee import Employee
conn =sqlite3.connect('employee.db')
c=conn.cursor()
# c.execute("""CREATE TABLE employee(
#         first text,
#         last text,
#         pay integer
#         )""")
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES(:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})
def emp_last_name(lastname):
    c.execute("SELECT * from employee where last=:last",{'last':lastname})
    print(c.fetchall())
def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employee set pay=:pay where first=:first and last=:last""",{'first':emp.first,'last':emp.last,'pay':pay})
def del_emp(emp):
    with conn:
        c.execute("DELETE from employee where first=:first and last=:last",{'first':emp.first,'last':emp.last})
emp_1=Employee('Bhuvi','Kumar',30000)
emp_2=Employee('Jasprit','Bumrah',40000)
#
# c.execute("INSERT INTO employee VALUES(?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))
# c.execute("INSERT INTO employee VALUES(:first,:last,:pay)",{'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})

# c.execute("SELECT * from employee where last=?",(emp_2.last,))
# conn.commit()
# c.execute("SELECT * from employee where last=:last",{'last':'Vijay'})
# conn.commit()
# print(c.fetchall())
# conn.commit()
# insert_emp(emp_2)
# emp_last_name('Bumrah')
# update_pay(emp_2,80000)
emp_last_name('Kumar')
# del_emp(emp_1)
conn.close()
