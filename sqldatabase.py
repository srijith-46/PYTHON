import mysql.connector
class EMPLOYEE:
	def __init__(self):
		self.db=mysql.connector.connect(host="localhost",user="root",password="Dumma12@",auth_plugin="mysql_native_password",database="employee")
		self.cur=self.db.cursor()
		self.createtable()
	def createtable(self):
		query=""" CREATE TABLE IF NOT EXISTS emp(slno INT PRIMARY KEY,name VARCHAR(25),address VARCHAR(50),empcode VARCHAR(10),dob DATE,age INT,mobile INT,status INT,des VARCHAR(20) )"""
		self.cur.execute(query)
		self.db.commit()
		print("Table added.")
	def insert(self,slno,name,address,empcode,dob,age,mobile,status,des):
		query=""" INSERT INTO emp(slno,name,address,empcode,dob,age,mobile,status,des) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) """
		values=(slno,name,address,empcode,dob,age,mobile,status,des)
		self.cur.execute(query,values)
		self.db.commit()
		print("record added")
	def show(self):
		self.cur.execute("SELECT * FROM emp")
		rows=self.cur.fetchall()
		for r in rows:
			print(r)
	def modify(self,des,slno):
		query=""" UPDATE emp SET des=%s WHERE slno=%s """
		values=(des,slno)
		self.cur.execute(query,values)
		print("record modified")
	def delete(self,slno):
		query="""DELETE FROM emp WHERE slno=%s """
		values=(slno,)
		self.cur.execute(query,values)
		print("record deleted")
d=EMPLOYEE()
while True:
	print("\n1.Add Row\n2.Update row\n3.Delete row\n4.Display All\n5.Exit")
	ch=input("Enter your choice:")
	if(ch=='1'):
		slno=int(input("Enter slno:"))
		name=input("Enter name:")
		address=input("Enter address:")
		empcode=input("Enter empcode:")
		dob=input("Enter DOB:")
		age=int(input("Enter age:"))
		mobile=int(input("Enter mobile phone number:"))
		status=int(input("Enter status:"))
		des=input("Enter designation:")
		d.insert(slno,name,address,empcode,dob,age,mobile,status,des)
		print("Table added")
	elif(ch=='4'):
                d.show()
	elif(ch=='2'):
		slno=int(input("Enter slno:"))
		des=input("Enter new  designation:")
		d.modify(des,slno)
	elif(ch=='3'):
		slno=int(input("Enter slno whose table will be deleted:"))
		d.delete(slno)
	elif(ch=='5'):
		break
	else:
		print("Enter correct option")
