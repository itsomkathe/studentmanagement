import mysql.connector
def add():
	try:
		#connection established
		con=mysql.connector.connect(host="localhost",user="root",passwd="sk@12345",database="Python_Programming")
		
		#create cursor object
		cur = con.cursor()
		
		#Accept data from user 
		roll=int(input("Enter the roll number :"))
		name=input("Enter the name :")
		add=input("Enter the address :")
		per=float(input("Enter the per :"))
		
		#Insert query
		query="insert into shubham(roll,name,address,per) values (%s,%s,%s,%s)"
		data=(roll,name,add,per)
		
		#Execute query
		cur.execute(query,data)
		con.commit()
		print("Record added successfully")
	except:
		print("Exception occured in adding record ")
		con.rollback()
	con.close()

def display():
	try:
		#connection established
		con=mysql.connector.connect(host="localhost",user="root",passwd="sk@12345",database="Python_Programming")
		
		#create cursor object
		cur = con.cursor()
		
		#Execute query
		cur.execute("select * from shubham")
		
		#Display from Database
		cnt=0
		for rec in cur :
			if cnt==0:
				print("Student Information")
				print("--------------------------------------------------------")
				print("Roll\tName\t\t\tAddress\t\tPercentage")
				print("--------------------------------------------------------")
			cnt=cnt+1
			print(rec[0],"\t",rec[1],"\t\t",rec[2],"\t\t",rec[3])
		print("--------------------------------------------------------")
		print("Total Records :",cnt)
		print("--------------------------------------------------------")
	except:
		print("Exception occured in adding record ")
		con.rollback()
	con.close()		

def search():
	try:
		#connection established
		con=mysql.connector.connect(host="localhost",user="root",passwd="sk@12345",database="Python_Programming")
		
		#create cursor object
		cur = con.cursor()
		
		print("--------------------------------------------------------")
		print("Search Menu ")
		print("--------------------------------------------------------")
		print("1.By roll number ")
		print("2.By name")
		print("3.By address")
		print("4.By percentage")
		print("--------------------------------------------------------")
		ch=int(input("Enter your search choice(1-4) :"))
		print("--------------------------------------------------------")
		query=""
		data=(1,) 
		if ch==1:
			roll=int(input("Enter roll number to search record :"))
			query="select * from shubham where roll =%s"
			data=(roll,)
		elif ch==2:
			name=input("Enter name to search record :")
			query="select * from shubham where name =%s"
			data=(name,)
		elif ch==3:
			add=input("Enter address to search record :")
			query="select * from shubham where add =%s"
			data=(add,)
		elif ch==4:
			per=float(input("Enter name to search record :"))
			query="select * from shubham where per =%s"
			data=(per,)

		#Execute query
		cur.execute(query,data)
		
		#Display from Database
		cnt=0
		for rec in cur :
			if cnt==0:
				print("Student Information")
				print("--------------------------------------------------------")
				print("Roll\tName\t\t\tAddress\t\tPercentage")
				print("--------------------------------------------------------")
			cnt=cnt+1
			print(rec[0],"\t",rec[1],"\t\t",rec[2],"\t\t",rec[3])
			
		if cnt==0:
			print("Record not found in database")
		else:
			print("--------------------------------------------------------")
			print("Total Records :",cnt)
			print("--------------------------------------------------------")
	except:
		print("Exception occured in adding record ")
		con.rollback()
	con.close()
		
def update():
	try:
		#connection established
		con=mysql.connector.connect(host="localhost",user="root",passwd="sk@12345",database="Python_Programming")
		
		#create cursor object
		cur = con.cursor()

		#Accept data from user 
		roll=int(input("Enter the roll number whose record to be updated :"))
		name=input("Enter the new name :")
		add=input("Enter the new address :")
		per=float(input("Enter the new per :"))
		
		#Insert query
		query="update shubham set name =%s,address =%s,per =%s where roll =%s"
		data=(name,add,per,roll)
		
		#Execute query
		cur.execute(query,data)
		con.commit()
		print("Record updated successfully")
	except:
		print("Exception occured in adding record ")
		con.rollback()
	con.close()

def delete():
	try:
		#connection established
		con=mysql.connector.connect(host="localhost",user="root",passwd="sk@12345",database="Python_Programming")
		
		#create cursor object
		cur = con.cursor()

		#Accept data from user 
		roll=int(input("Enter the roll number whose record to be delete :"))
		
		#Insert query
		query="delete from shubham  where roll =%s"
		data=(roll,)
		
		#Execute query
		cur.execute(query,data)
		con.commit()
		print("Record deleted successfully")
	except:
		print("Exception occured in adding record ")
		con.rollback()
	con.close()		
		
def sort():
	try:
		#connection established
		con=mysql.connector.connect(host="localhost",user="root",passwd="sk@12345",database="Python_Programming")
		
		#create cursor object
		cur = con.cursor()
		
		print("--------------------------------------------------------")
		print("Sort Menu ")
		print("--------------------------------------------------------")
		print("1.By roll number in ascending order ")
		print("2.By name in ascending order")
		print("3.By address in ascending order")
		print("4.By percentage in ascending order")
		print("5.By roll number in descending order")
		print("6.By name in descending order")
		print("7.By address in descending order")
		print("8.By percentage in descending order")
		print("--------------------------------------------------------")
		ch=int(input("Enter your search choice(1-8) :"))
		print("--------------------------------------------------------")
		query="" 
		if ch==1:
			roll=int(input("Enter roll number to search record :"))
			query="select * from shubham order by roll asc"
		elif ch==2:
			name=input("Enter name to search record :")
			query="select * from shubham order by name asc"
		elif ch==3:
			add=input("Enter address to search record :")
			query="select * from shubham order by add asc"
		elif ch==4:
			per=float(input("Enter name to search record :"))
			query="select * from shubham order by per asc"
		elif ch==5:
			roll=int(input("Enter roll number to search record :"))
			query="select * from shubham order by roll desc"
		elif ch==6:
			name=input("Enter name to search record :")
			query="select * from shubham order by name desc"
		elif ch==7:
			add=input("Enter address to search record :")
			query="select * from shubham order by add desc"
		elif ch==8:
			per=float(input("Enter name to search record :"))
			query="select * from shubham order by per desc"
		#Execute query
		cur.execute(query)
		
		#Display from Database
		cnt=0
		for rec in cur :
			if cnt==0:
				print("Student Information")
				print("--------------------------------------------------------")
				print("Roll\tName\t\t\tAddress\t\tPercentage")
				print("--------------------------------------------------------")
			cnt=cnt+1
			print(rec[0],"\t",rec[1],"\t\t",rec[2],"\t\t",rec[3])
			
		if cnt==0:
			print("Record not found in database")
		else:
			print("--------------------------------------------------------")
			print("Total Records :",cnt)
			print("--------------------------------------------------------")
	except:
		print("Exception occured in adding record ")
		con.rollback()
	con.close()		

while(True):
	print("--------------------------------------------------------")
	print("Menu")
	print("1.Add record")
	print("2.Display record")
	print("3.Search record")
	print("4.Update record")
	print("5.Delete record")
	print("6.Sort record")
	print("7. Exit")
	print("--------------------------------------------------------")
	choice = int(input("Enter your choice(1-7) :"))
	print("--------------------------------------------------------")
	if(choice==1):
		add()
	elif(choice==2):
		display()
	elif(choice==3):
		search()
	elif(choice==4):
		update()
	elif(choice==5):
		delete()
	elif(choice==6):
		sort()
	elif(choice==7):
		exit()
	else:
		print("Invalid Choice")
	ch =input("Do you want to continue (Yes/No) :")
	if ch=='no':
		break;
