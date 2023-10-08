from kivy.core.window import Window
from kivymd.app import MDApp
import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
import sqlite3 as sql
from kivymd.toast import toast
from kivy import platform
from contextlib import closing
from sql_definitions import InsertStudentsData, convertToBinaryData, InsertAdminData, InsertStaffData
from login_spec import login_configurations, login_configurations_admin, login_configurations_staff


numbers = ["1","2","3","4","5","6","7","8","9","0"]
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]




class WindowManager(ScreenManager):
	pass

class StaffDashboard(MDScreen):
	pass

class AdminDashboard(MDScreen):
	pass

class SplashScreen(MDScreen):
	pass

class StudentLogin(MDScreen):
	def toast_up(self, text='', duration=2.5):
		if platform == 'android':
			toast(text=text, gravity=80, length_long=duration)
		else:
			toast(text=text, duration=duration)

	def check_authentication(self):
		self.authenticated = False
		unique_id = self.admission_number.text
		unique_key = self.student_pin.text
		self.add_no_confirmed = False
  
		db_passkeys = []
		db_id = []
    

		break_out1 = False
		break_out2 = False


		if unique_id != "":
			for alp in alphabets:
				if break_out1:
					break
				elif alp not in unique_id:
					for num in unique_id:
						if break_out1:
							break
						elif num not in numbers:
							print("The admission number is meant to be numeric characters only")
							self.toast_up("Numeric characters only")
							self.add_no_confirmed = False
							break_out1 = True
							break
						elif len(unique_id) < 3 or len(unique_id) > 3:
							print("Admission number is 3-digits")
							self.toast_up("Admission number is 3-digits")
							break_out1 = True
						
						else:
							if unique_key != "":
								for alp in alphabets:
									if break_out2:
										break
									elif alp not in unique_key:
										for num in unique_id:
											if break_out2:
												break
											if num not in numbers:
												print("Numeric Characters Only")
												self.toast_up("Numeric Characters Only")
												break_out2 = True

											elif len(unique_key) < 6 or len(unique_key) > 6:
												print("Access key is a 6-digits pin")
												self.toast_up("Access key is a 6-digits pin")
												break_out2 = True

											else:
												self.add_no_confirmed = True
												print("Input Type Validated !!!\n")

												break_out2 = True


												#======== Check For Sql DataSet=======#

							else:
								print("please enter your pin")
								self.toast_up("please enter your pin")

				else:
					print("Field is meant to be only numbers")
					self.toast_up("Field is meant to be only numbers")
		else:
			print("Admission Field is empty")
			self.toast_up("Admission Field is empty")

		if self.add_no_confirmed == True:
			# InsertStudentsData("Sanusi Ridwan", f"{unique_id}", "SS3B", 16, "images/passport.jpg", True, f"{unique_key}")

			print("Nice admission format")
			
			sqliteConnection = sql.connect('DataBase/AccountLogin.db')
			cursor = sqliteConnection.cursor()
			print("Connected to SQLite\n")

		
			c = cursor.execute("""Select * from AccountLogin""")
			print(c)
			if c != "":
				break_out_match = False
				for i in c:
					if break_out_match:
						break
					number_to_match = i[2]
					key_to_match = i[7]
     
					db_passkeys.append(key_to_match)
					db_id.append(number_to_match)
     
				print(db_id); print(db_passkeys)
	
				unique_id = int(unique_id)
				unique_key = int(unique_key)

				if unique_id not in db_id:
					print("Admission Number does not exist")
					self.toast_up("Admission Number does not exist")

				else:
					if unique_key not in db_passkeys:
						print("Pin does not exist")
						self.toast_up("Pin does not exist")
					else:
						check = cursor.execute(f"SELECT security_pin from AccountLogin where admission_number = {unique_id}")
						pn = ""
						for i in check:
							pn+=str(i[0])
						check = int(pn)
						if check != unique_key:
							print("Account details does not match")
							self.toast_up("Account details does not match")
						elif check == unique_key:
							print("Login Successfully")
							self.toast_up("Login Successfully")

							login_configurations(unique_id, unique_key)
							break_out_match = True
							self.authenticated = True
						
			else:
				print("Database Table is empty")
				self.toast_up("Database Table is empty")

			cursor.close()
			sqliteConnection.close()

		else:
			pass


class MainScreen(MDScreen):
	pass

class NavScreen(MDScreen):
	pass

class AdminLogin(MDScreen):
	def toast_up(self, text='', duration=2.5):
		if platform == 'android':
			toast(text=text, gravity=80, length_long=duration)
		else:
			toast(text=text, duration=duration)

	def check_authentication(self):
		self.authenticated = False
		unique_key = self.admin_pin.text
		self.add_p_confirmed = False
  
		db_passkeys = []

		break_out1 = False
		break_out2 = False


		
		if unique_key != "":
			for alp in alphabets:
				if break_out2:
					break
				elif alp not in unique_key:

					if len(unique_key) < 6 or len(unique_key) > 6:
						print("Access key is a 6-digits pin")
						self.toast_up("Access key is a 6-digits pin")
						break_out2 = True

					else:
						self.add_p_confirmed = True
						print("Input Type Validated !!!\n")

						break_out2 = True
				elif alp in unique_key:
					print("Numeric Characters Only")
					self.toast_up("Numeric Characters Only")
					break_out2 = True


							#======== Check For Sql DataSet=======#

		else:
			print("please enter your pin")
			self.toast_up("please enter your pin")

		if self.add_p_confirmed == True:
			# InsertAdminData("Sanusi Ridwan Olaoluwa", "Developer", "images/passport.jpg", f"{unique_key}")
			
			sqliteConnection = sql.connect('DataBase/AccountLogin.db')
			cursor = sqliteConnection.cursor()
			print("Connected to SQLite\n")

		
			c = cursor.execute("""Select * from AdminLogin""")
			print(c)
			if c != "":
				break_out_match = False
				for i in c:
					if break_out_match:
						break

					key_to_match = i[4]
     
					db_passkeys.append(key_to_match)
     
				print(db_passkeys)
	
				unique_key = int(unique_key)

				if unique_key not in db_passkeys:
					print("Pin does not exist")
					self.toast_up("Pin does not exist")
				else:
					check = cursor.execute(f"SELECT security_pin from AdminLogin")
					pn = []
					for i in check:
						pn.append(i[0])
					print(pn)
					if unique_key not in pn:
						print("Account details does not match")
						self.toast_up("Account details does not match")
					elif unique_key in pn:
						print("Login Successfully")
						self.toast_up("Login Successfully")

						login_configurations_admin(unique_key)
						break_out_match = True
						self.authenticated = True
					
			else:
				print("Database Table is empty")
				self.toast_up("Database Table is empty")

			cursor.close()
			sqliteConnection.close()

		else:
			pass


class StaffLogin(MDScreen):
	def toast_up(self, text='', duration=2.5):
		if platform == 'android':
			toast(text=text, gravity=80, length_long=duration)
		else:
			toast(text=text, duration=duration)

	def check_authentication(self):
		self.authenticated = False
		unique_id = self.staff_id.text
		unique_key = self.staff_pin.text
		self.add_no_confirmed = False
  
		db_passkeys = []
		db_id = []
    

		break_out1 = False
		break_out2 = False


		if unique_id != "":
			for alp in alphabets:
				if break_out1:
					break
				elif alp not in unique_id:
					for num in unique_id:
						if break_out1:
							break
						elif num not in numbers:
							print("The staff id is meant to be numeric characters only")
							self.toast_up("Numeric characters only")
							self.add_no_confirmed = False
							break_out1 = True
							break
						elif len(unique_id) < 3 or len(unique_id) > 3:
							print("Staff id is a 3-digits character")
							self.toast_up("Staff id is a 3-digits character")
							break_out1 = True
						
						else:
							if unique_key != "":
								for alp in alphabets:
									if break_out2:
										break
									elif alp not in unique_key:
										for num in unique_id:
											if break_out2:
												break
											if num not in numbers:
												print("Numeric Characters Only")
												self.toast_up("Numeric Characters Only")
												break_out2 = True

											elif len(unique_key) < 6 or len(unique_key) > 6:
												print("Access key is a 6-digits pin")
												self.toast_up("Access key is a 6-digits pin")
												break_out2 = True

											else:
												self.add_no_confirmed = True
												print("Input Type Validated !!!\n")

												break_out2 = True


												#======== Check For Sql DataSet=======#

							else:
								print("please enter your pin")
								self.toast_up("please enter your pin")

				else:
					print("Field is meant to be only numbers")
					self.toast_up("Field is meant to be only numbers")
		else:
			print("Identity Field is empty")
			self.toast_up("Identity Field is empty")

		if self.add_no_confirmed == True:
			# InsertStaffData("Sanusi Ridwan Ayomide", "HOD of technology department", "images/passport.jpg", f"{unique_key}", "Tech Affairs", "Male", f"{unique_id}")

			print("Nice admission format")
			
			sqliteConnection = sql.connect('DataBase/AccountLogin.db')
			cursor = sqliteConnection.cursor()
			print("Connected to SQLite\n")

		
			c = cursor.execute("""Select * from StaffLogin""")
			print(c)
			if c != "":
				break_out_match = False
				for i in c:
					if break_out_match:
						break
					number_to_match = i[7]
					key_to_match = i[4]
     
					db_passkeys.append(key_to_match)
					db_id.append(number_to_match)
     
				print(db_id); print(db_passkeys)
	
				unique_id = int(unique_id)
				unique_key = int(unique_key)

				if unique_id not in db_id:
					print("Staff id does not exist")
					self.toast_up("Staff id does not exist")

				else:
					if unique_key not in db_passkeys:
						print("Pin does not exist")
						self.toast_up("Pin does not exist")
					else:
						check = cursor.execute(f"SELECT security_pin from StaffLogin where staff_id = {unique_id}")
						pn = ""
						for i in check:
							pn+=str(i[0])
						check = int(pn)
						if check != unique_key:
							print("Account details does not match")
							self.toast_up("Account details does not match")
						elif check == unique_key:
							print("Login Successfully")
							self.toast_up("Login Successfully")

							login_configurations_staff(unique_id, unique_key)
							break_out_match = True
							self.authenticated = True
						
			else:
				print("Database Table is empty")
				self.toast_up("Database Table is empty")

			cursor.close()
			sqliteConnection.close()

		else:
			pass


class MyApp(MDApp):
	last_album_image = "child.JPG"

	def build(self):

		sqliteConnection = sql.connect('DataBase/AccountLogin.db')
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite\n")

		cursor.execute("""CREATE TABLE if not exists AccountLogin(student_id integer primary key AUTOINCREMENT, name text NOT NULL, admission_number int not null, class varchar(255) not null, age int not null, visuals BLOB, passed_out boolean not null, security_pin int not null, gender varchar(25) not null)""")

		cursor.execute("""CREATE TABLE if not exists AdminLogin(admin_id integer primary key AUTOINCREMENT, name text NOT NULL, position varchar(255) not null, visuals BLOB, security_pin int not null)""")

		cursor.execute("""CREATE TABLE if not exists StaffLogin(personal_id integer primary key AUTOINCREMENT, name text NOT NULL, position varchar(255) not null, visuals BLOB, security_pin int not null, subjects not null, gender varchar(25) not null, staff_id int not null)""")


		cursor.close()
		sqliteConnection.close()




		Window.size = [410, 745]

		self.school_name = "Eagle School"
		self.school_logo = "images/eagle_full_clr.png"
		self.school_motto = "Culture Of Excellence"

		kv_files = ["init_login.kv", "admin_login.kv", "splashscreen.kv", "staff_login.kv", "main_dash.kv", "nav_screen.kv", "admin_dashboard.kv", "staff_dashboard.kv"]

		for i in kv_files:
			Builder.load_file("KV_Files/" + i)

		#storing screen manager in a list
		screens = [
			SplashScreen(name="splashscreen"),
			AdminDashboard(name="admindashboard"),
			StaffDashboard(name="staffdashboard"),
			StudentLogin(name="studentlogin"),
			AdminLogin(name="adminlogin"),
			StaffLogin(name="stafflogin"),
			MainScreen(name="dashboard"),
			NavScreen(name="nav_screen")
		]

		global wm
		self.wm = WindowManager(transition = SlideTransition())
		for screen in screens:
			self.wm.add_widget(screen)

		self.wm.current = "adminlogin"

		return self.wm

	# def on_start(self):
	# 	Clock.schedule_once(self.sl, 10)

	def sl(self, *args):
		self.change_screen("studentlogin")

	def change_screen(self, name_of_screen):
		self.wm.current = f"{name_of_screen}"


if __name__ == '__main__':
	MyApp().run()