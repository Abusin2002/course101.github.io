import mysql.connector 
conn=mysql.connector.connect(host='localhost',port='3306',user='root',password='jnpw7708',database='abu')
 
cursor=conn.cursor()
selectquery='select * from employee'

cursor.execute(selectquery)

records=cursor.fetchall()

print('Total row count is : ',cursor.rowcount)


print('Employee Details;')

for row in records:
    print('EmpID; ',row[0])
    print('Name: ',row[1])
    print('EmpAge: ',row[2])
    print('EmpRole: ',row[3])
    print()

cursor.close()
conn.close()
