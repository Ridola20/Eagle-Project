import sqlite3 as sql
from contextlib import closing

def All(unique_id, unique_key):
	All_List = []

	try:
		with closing(sql.connect ('DataBase/AccountLogin.db')) as con:
			with closing(con.cursor()) as cur:
				c = cur.execute(f"Select * from AccountLogin where security_pin = {unique_key} and admission_number = {unique_id}")
				for i in c:
					All_List.append(i[0])
					All_List.append(i[1])
					All_List.append(i[2])
					All_List.append(i[3])
					All_List.append(i[4])
					All_List.append(i[5])
					All_List.append(i[6])
					All_List.append(i[7])
					All_List.append(i[8])

					return All_List

	except Exception as e:
		print(f"error: {e}")

	finally:
		print("\nDatabase disconnected...\n")



def All_admin(unique_key):
	All_List = []

	try:
		with closing(sql.connect ('DataBase/AccountLogin.db')) as con:
			with closing(con.cursor()) as cur:
				c = cur.execute(f"Select * from AdminLogin where security_pin = {unique_key}")
				for i in c:
					All_List.append(i[0])
					All_List.append(i[1])
					All_List.append(i[2])
					All_List.append(i[3])
					All_List.append(i[4])

					return All_List

	except Exception as e:
		print(f"error: {e}")
		
	finally:
		print("\nDatabase disconnected...\n")



def All_staff(unique_id, unique_key):
	All_List = []

	try:
		with closing(sql.connect ('DataBase/AccountLogin.db')) as con:
			with closing(con.cursor()) as cur:
				c = cur.execute(f"Select * from StaffLogin where security_pin = {unique_key} and staff_id = {unique_id}")
				for i in c:
					All_List.append(i[0])
					All_List.append(i[1])
					All_List.append(i[2])
					All_List.append(i[3])
					All_List.append(i[4])
					All_List.append(i[5])
					All_List.append(i[6]) 
					All_List.append(i[7]) 

					return All_List

	except Exception as e:
		print(f"error: {e}")

	finally:
		print("\nDatabase disconnected...\n")

