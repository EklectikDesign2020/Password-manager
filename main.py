# Name: password Manager 2021
#
# licence: portfolie

''' Store password and multiple user link each to a password sheet via a randomly generated key for each user '''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from cryptography.fernet import Fernet # User key encryption
from os import path
from hashlib import sha256 # Enable hash reading
from scryp import encrypt, decrypt # Scrypt not {Scrypt}
import os
import csv
import time

# Perso class
from password_user_sheet import append_user_sheet
from reg_check import  password, email_control
from create_user_sheet import user_create_csv

# Global variable toplevel()
global add_window
global log_window
global reg_window

# Window Main
root = Tk()
root.title("Password Manager V0.0.1")
# root.state('zoomed') # Fullscreen mode
root.geometry("900x600+500+300")
root.resizable(width=False,  height=False)

# Variables
username = os.getlogin() # Gets uers window profile

# Variable text / color
font = 'Myriad Pro'
font_size = 10
activebackground_color = '#2f354d'
background_button_color = '#2f354d'
text_color = "#8d8e91"
color_event = 'white'

# Variable canvas
width_top_canvas = 150
height_top_canvas = 596		

# Entitle Encode
copy_right = u"\u00A9"

# Canvas
left_side_rec = Canvas(root, width=width_top_canvas, height=height_top_canvas, bg='#2f354d')
left_side_rec.place(x=0, y=0)

# Image enter event
add_password_image_enter = PhotoImage(file="image/lock.png")
add_password_image_lab_enter = Label(root, image=add_password_image_enter, bg="#2f354d")
add_password_image_lab_enter.place(x=15, y=37)

edi_password_image_enter = PhotoImage(file="image/unlock.png")
edi_password_image_lab_enter = Label(root, image=edi_password_image_enter, bg="#2f354d")
edi_password_image_lab_enter.place(x=15, y=86)

del_password_image_enter = PhotoImage(file="image/del-lock.png")
del_password_image_lab_enter = Label(root, image=del_password_image_enter, bg="#2f354d")
del_password_image_lab_enter.place(x=12, y=187)

# Image leave event
add_password_image_leave = PhotoImage(file="image/lock-event.png")
add_password_image_lab_leave = Label(root, image=add_password_image_leave, bg="#2f354d")

edi_password_image_leave = PhotoImage(file="image/unlock-event.png")
edi_password_image_lab_leave = Label(root, image=edi_password_image_leave, bg="#2f354d")

del_password_image_leave = PhotoImage(file="image/del-lock-event.png")
del_password_image_lab_leave = Label(root, image=del_password_image_leave, bg="#2f354d")


# Event Enter (animation)
def button_event_enter(e):
	add_password.config(fg=color_event)
	add_password_image_lab_enter.place_forget()
	add_password_image_lab_leave.place(x=15, y=37)

def button_event_enter2(e):
	edit_password.config(fg=color_event)
	edi_password_image_lab_enter.place_forget()
	edi_password_image_lab_leave.place(x=15, y=86)

def button_event_enter3(e):
	delete_password.config(fg=color_event)
	del_password_image_lab_enter.place_forget()
	del_password_image_lab_leave.place(x=12, y=187)

def button_event_color_no_image(e):
	e.widget.config(fg=color_event)

# Event leave (animation)
def button_event_leave(e):
	add_password.config(fg=text_color)
	add_password_image_lab_leave.place_forget()
	add_password_image_lab_enter.place(x=15, y=37)

def button_event_leave2(e):
	edit_password.config(fg=text_color)
	edi_password_image_lab_leave.place_forget()
	edi_password_image_lab_enter.place(x=15, y=86)

def button_event_leave3(e):
	delete_password.config(fg=text_color)
	del_password_image_lab_leave.place_forget()
	del_password_image_lab_enter.place(x=12, y=187)

def delete_text(e):
	search_bar.delete(0, END)
	search_bar.config(fg='black')

def button_event_color_no_image_leave(e):
	e.widget.config(fg=text_color)


# Function
def create_user_csv():
		''' Function that sends entered info to  (create_user_sheet.py)
		see class create_user_sheet for more info  '''

		user_create_csv(reg_fname_e.get(), reg_lname_e.get(), reg_email_e.get(), reg_pass_e.get())
		reg_window.destroy()
		

def check():
	''' Function checks password and email if correct format using (reg_check.py) 
	returns bool '''

	pass_check = (password(reg_pass_e.get()))
	email_check = (email_control(reg_email_e.get()))

	if pass_check and email_check:
		create_user_csv()
	else:
		if not pass_check:
			messagebox.showwarning("Password INCORRECT", "The Password must be minimum of 8 characters long\nand contain at least 3 numbers and 5 letters.")

		else:
			messagebox.showwarning("Email INCORRECT", "\nExample (nameuser@gmail.com)")


def add_password():
	''' Add password info to csv, refresh treeview '''

	global add_window
	# Window setup
	add_window = Toplevel()
	add_window.title("Register User")
	add_window.geometry("320x450+500+300")
	add_window.resizable(width=False,  height=False)
	add_window.attributes("-topmost", True)

	# List store password
	global password_list
	password_list = []

	# Variable
	font_r = 'Microsoft Yi Baiti'
	bts_bg = 'SystemButtonFace'
	
	# Canvas
	login_can = Canvas(add_window, width=311, height=45, bg='#2f354d')
	login_can.place(x=2, y=2)

	# Funtion
	def bts_event_enter(e):
		e.widget.config(fg="#0c36c2")

	def bts_event_leave(e):
		e.widget.config(fg="black")

	def add_to_list():
		''' Creates list with entered password info, ready to be added to csv file'''
		
		if len(password_add_e.get()) == 0 and len(username_add_e.get()) == 0:
			messagebox.showwarning("Add password ERROR", f"You have NOT entered a Password or Username")
		else:
			password_encrypt = encrypt(password_add_e.get(), user_key) # Encrypt using scryp module
			password_list.append(domain_add_e.get()) 
			password_list.append(username_add_e.get())
			password_list.append(password_encrypt)
			password_list.append(id_add_e.get())

			# Empty entry box
			domain_add_e.delete(0, END)
			username_add_e.delete(0, END)
			password_add_e.delete(0, END)
			id_add_e.delete(0, END)
			id_add_e.insert(0, '0')
			append_user_sheet(password_list, user_key)
			load_file(user_key)
			password_list.clear()

	
	# GUI
		# Label
	message = Label(add_window, text="Add password account: ", font=(font_r, 23), fg=text_color,  bg=background_button_color)
	message.place(x=8, y=8)

	#messages = Label(add_window, text="INSTRUCTION\nAdd info then click add to list, once passwords entered,\n click finish to add to your account ", font=(font_r, 11), fg=text_color)
	#messages.place(x=5, y=300)

	domain_add = Label(add_window, text="Website: ", font=(font_r, 20))
	domain_add.place(x=15, y=55)

	username_add = Label(add_window, text="Username: ", font=(font_r, 20))
	username_add.place(x=15, y=130)

	password_add = Label(add_window, text="Password: ", font=(font_r, 20))
	password_add.place(x=15, y=205)

	id_parent = Label(add_window, text="AGI: ", font=(font_r, 20))
	id_parent.place(x=15, y=280) # 75px different from adove

	id_info = Label(add_window, text="*AGI = Account grouping identification. ", font=(font_r, 10))
	id_info.place(x=35, y=345) # 75px different from adove

	Label(add_window, text="___________________", font=(font_r, 20)).place(x=35, y=88)
	Label(add_window, text="___________________", font=(font_r, 20)).place(x=35, y=163)
	Label(add_window, text="___________________", font=(font_r, 20)).place(x=35, y=238)
	Label(add_window, text="___________________", font=(font_r, 20)).place(x=35, y=313) # 3px different from entry box

		# Entry box
	domain_add_e = Entry(add_window, bd=0, font=(font_r, 17), bg=bts_bg)
	domain_add_e.place(x=39, y=85)

	username_add_e = Entry(add_window, bd=0, font=(font_r, 17), bg=bts_bg)
	username_add_e.place(x=39, y=160)

	password_add_e = Entry(add_window, bd=0, font=(font_r, 17), bg=bts_bg)
	password_add_e.place(x=39, y=235)

	id_add_e = Entry(add_window, bd=0, font=(font_r, 17), bg=bts_bg)
	id_add_e.place(x=39, y=310) # 30px from Label
	id_add_e.insert(0, '0')

	add_bts = Button(add_window, text="Add Password!", bg=bts_bg, font=(font_r, 25), bd=0, command=add_to_list)
	add_bts.place(x=100, y=385)
	add_bts.bind("<Enter>", bts_event_enter)
	add_bts.bind("<Leave>", bts_event_leave)


def edit_password():
	try:
		csv_file_pass.close()

		global edit_window
		global data_csv
		# Window setup
		edit_window = Toplevel()
		edit_window.title("Register User")
		edit_window.geometry("320x450+500+300")
		edit_window.resizable(width=False,  height=False)
		edit_window.attributes("-topmost", True)

		# List store password
		global data_csv
		data_csv = []

		# Variable
		font_r = 'Microsoft Yi Baiti'
		bts_bg = 'SystemButtonFace'
		id = int(search_bar.get())

		
		# Canvas
		login_can = Canvas(edit_window, width=311, height=45, bg='#2f354d')
		login_can.place(x=2, y=2)

		# Funtion
		def bts_event_enter(e):
			e.widget.config(fg="#0c36c2")

		def bts_event_leave(e):
			e.widget.config(fg="black")


		def modify_csv():
				password_encrypt = encrypt(password_edit_e.get(), user_key)
				data_csv[id][0] = domain_edit_e.get()
				data_csv[id][1] = username_edit_e.get()
				data_csv[id][2] = password_encrypt
				data_csv[id][3] = account_group_id_e.get()

				r = open(f"C:/csv/{user_key}.csv", 'w', newline='')
				reader = csv.writer(r)
				reader.writerows(data_csv)
				r.close()
				load_file(user_key)
				# Empty entry box
				domain_edit_e.delete(0, END)
				username_edit_e.delete(0, END)
				password_edit_e.delete(0, END)
				
				data_csv.clear()


		
		# GUI
			# Label
		message_edit = Label(edit_window, text="Edit password INFO: ", font=(font_r, 23), fg=text_color,  bg=background_button_color)
		message_edit.place(x=8, y=8)

		domain_edit = Label(edit_window, text="Website: ", font=(font_r, 20))
		domain_edit.place(x=15, y=55)

		username_edit = Label(edit_window, text="Username: ", font=(font_r, 20))
		username_edit.place(x=15, y=130)

		password_edit = Label(edit_window, text="Password: ", font=(font_r, 20))
		password_edit.place(x=15, y=205)

		id_parent = Label(edit_window, text="AGI: ", font=(font_r, 20))
		id_parent.place(x=15, y=280) # 75px different from adove

		account_group_id = Label(edit_window, text="*AGI = Account grouping identification. ", font=(font_r, 10))
		account_group_id.place(x=35, y=345) # 75px different from adove

		Label(edit_window, text="___________________", font=(font_r, 20)).place(x=35, y=88)
		Label(edit_window, text="___________________", font=(font_r, 20)).place(x=35, y=163)
		Label(edit_window, text="___________________", font=(font_r, 20)).place(x=35, y=238)
		Label(edit_window, text="___________________", font=(font_r, 20)).place(x=35, y=313) # 3px different from entry box

			# Entry box
		domain_edit_e = Entry(edit_window, bd=0, font=(font_r, 17), bg=bts_bg)
		domain_edit_e.place(x=39, y=85)

		username_edit_e = Entry(edit_window, bd=0, font=(font_r, 17), bg=bts_bg)
		username_edit_e.place(x=39, y=160)

		password_edit_e = Entry(edit_window, bd=0, font=(font_r, 17), bg=bts_bg)
		password_edit_e.place(x=39, y=235)

		account_group_id_e = Entry(edit_window, bd=0, font=(font_r, 17), bg=bts_bg)
		account_group_id_e.place(x=39, y=310) # 30px from Label

		edit_bts = Button(edit_window, text="Edit Account!", bg=bts_bg, font=(font_r, 25), bd=0, command=modify_csv)
		edit_bts.place(x=100, y=385)
		edit_bts.bind("<Enter>", bts_event_enter)
		edit_bts.bind("<Leave>", bts_event_leave)

		r = open(f"C:/csv/{user_key}.csv", 'r')
		reader = csv.reader(r)

		for row in reader:
			data_csv.append(row)


		# Data list index variable
		dom = data_csv[id][0]
		user = data_csv[id][1]
		password = data_csv[id][2]
		agi = data_csv[id][3]

		decrypted = decrypt(password, user_key)

		domain_edit_e.insert(0, dom)
		username_edit_e.insert(0, user)
		password_edit_e.insert(0, decrypted)
		account_group_id_e.insert(0, agi)
	except Exception as error:
		messagebox.showinfo("Missing AGI", "Please enter an AGI of account you like to modify.")
		edit_window.destroy()


def delete_password():
	try:
		# List store password
		global data_csv
		global id
		data_csv = []

		id = int(search_bar.get())

		def delete_csv_row():
			choice = messagebox.askokcancel("DELETE DATA", f"Are you sure you like to delete the data - {data_csv[id]}?")

			if choice == 0:
				messagebox.showinfo("Delete cancel", "No data has been deleted")
				search_bar.get().delete(0, END)
			else:

				del data_csv[id]

				r = open(f"C:/csv/{user_key}.csv", 'w', newline='')
				reader = csv.writer(r)
				reader.writerows(data_csv)
				r.close()
				load_file(user_key)
				messagebox.showinfo("Delete", "Row deleted")
				search_bar.get().insert(0, '0')

			
		r = open(f"C:/csv/{user_key}.csv", 'r')
		reader = csv.reader(r)

		for row in reader:
			data_csv.append(row)

		delete_csv_row()
	except Exception as error:
		if id == "":
			messagebox.showinfo("Missing AGI", "Please enter an AGI of account you like to modify.")
	
	
def load_file(filename_key):
	global idd
	''' Load correct file, attach to user key '''
	global csv_file_pass
	
	my_tree.pack(ipady=450, ipadx=100)
	x = my_tree.get_children()
	for item in x:
		my_tree.delete(item)
	with open(f"C:/csv/{filename_key}.csv") as csv_file_pass:
		reader = csv.DictReader(csv_file_pass)
		count = 1
	
		for row in reader: # Go through row by title
			domain = row['Domain']
			user = row['User']
			password_dec = row['Password']
			iid = row['Assign AGI']
			decrypted = decrypt(password_dec, filename_key)
			if iid == '0':
				my_tree.insert(parent='', iid=count, index='end', text=count, value=(domain, user, decrypted, iid))
				count += 1
			else:
				my_tree.insert(parent=iid, iid=count, index='end', text=count, value=(domain, user, decrypted, iid))
				count += 1


def login_account():
	''' Uses the csv usersheet and compare user email and associated password '''

	log_window.lift()
	global login_statues
	global user_key
	global user_name


	# Variable	
	data =[]
	password_encode = sha256(log_pass_e.get().encode('ascii')).hexdigest()

	if path.exists(f"C:/csv/UserSheet.csv"):
			with open(f"C:/csv/UserSheet.csv", 'r') as csv_user:
				reader = csv.reader(csv_user)

				for row in reader:
					data.append(row) # Append user sheet in data.list()
					
				last_name = [x[1] for x in data] # Search by index in data.list() 
				email_log = [x[2] for x in data] # Search by index in data.list() 
				password_log = [x[3] for x in data] # Search by index in data.list() 
				key = [x[4] for x in data] # Search by index in data.list() 
				
				if log_email_e.get() in email_log: # If log_email_e.get is in data.list() index email_log variable
					for k in range (0, len(email_log)):
						if email_log[k] == log_email_e.get() and password_log[k] == password_encode:
							user_key = (key[k])
							user_name = (last_name[k])
							left_side_rec.delete(login_statue)
							login_statues = left_side_rec.create_text(75, 500, text=f"Active as {user_name}", font=(font, 10), fill='green')
							log_window.destroy()	
							load_file(user_key)
							add_password.config(state='normal')
							edit_password.config(state='normal')
							delete_password.config(state='normal')

						else:
							incorrect = Label(log_window, text='*password INCORRECT.',font=('Microsoft Yi Baiti', 10),fg='red')
							incorrect.place(x=77, y=268)		
				else:
					messagebox.showwarning("ACCESS DENIED", f"Email is not find - Email enter: {log_email_e.get()}")


def log_out():
	''' Log out function, close csv file, reset user_[x] variable '''
	global user_key
	try:
		user_name = '00'
		user_key = '00'
		x = my_tree.get_children()
		for item in x:
			my_tree.delete(item)

		left_side_rec.delete(login_statues)
		ogin_statue = left_side_rec.create_text(75, 500, text=f"Not log-in {user_name}", font=(font, 10), fill='red')
		add_password.config(state='disable')
		edit_password.config(state='disable')
		delete_password.config(state='disable')
	except Exception as error:
		messagebox.showwarning("Log-Out ERROR", f"No user loged in - {error}")


def log_in():
	''' Graphic interface for login and password entry box '''
	global log_window
	global log_pass_e
	global log_email_e

	if not path.exists(f"C:/csv/UserSheet.csv"):
		messagebox.showwarning("log_in ERROR", "No user sheet find, please register first")
	else:
		# Window setup
		log_window = Toplevel()
		log_window.title("Log-IN")
		log_window.geometry("320x450+500+300")
		log_window.resizable(width=False,  height=False)
		log_window.attributes("-topmost", True)

		

		# Variable
		font_r = 'Microsoft Yi Baiti'
		bts_bg = 'SystemButtonFace'
		
		# Canvas
		login_can = Canvas(log_window, width=311, height=45, bg='#2f354d')
		login_can.place(x=2, y=2)

		# Funtion
		def bts_event_enter(e):
			login_bts.config(fg="#0c36c2")

		def bts_event_leave(e):
			login_bts.config(fg="black")

		# GUI
			# Label
		message = Label(log_window, text="Login to Account: ", font=(font_r, 23), fg=text_color,  bg=background_button_color)
		message.place(x=8, y=8)

		log_email = Label(log_window, text="Email: ", font=(font_r, 20))
		log_email.place(x=40, y=115)

		reg_pass = Label(log_window, text="Password: ", font=(font_r, 20))
		reg_pass.place(x=40, y=190)

		Label(log_window, text="___________________", font=(font_r, 20)).place(x=77, y=147)
		Label(log_window, text="___________________", font=(font_r, 20)).place(x=77, y=233)

			# Entry box
		log_email_e = Entry(log_window, bd=0, font=(font_r, 17), bg=bts_bg)
		log_email_e.place(x=80, y=145)
	 	
		log_pass_e = Entry(log_window, bd=0, font=(font_r, 17), bg=bts_bg, show="*")
		log_pass_e.place(x=80, y=230)


		login_bts = Button(log_window, text="Login", bg=bts_bg, font=(font_r, 35), bd=0, command=login_account)
		login_bts.place(x=155, y=375)
		login_bts.bind("<Enter>", bts_event_enter)
		login_bts.bind("<Leave>", bts_event_leave)



def create_user():
	''' Function that ask user for registation info. '''

	global reg_window
	# Window setup
	reg_window = Toplevel()
	reg_window.title("Register User")
	reg_window.geometry("320x450+500+300")
	reg_window.resizable(width=False,  height=False)
	reg_window.attributes("-topmost", True)

	global reg_fname_e
	global reg_pass_e
	global reg_lname_e
	global reg_email_e

	# Variable
	font_r = 'Microsoft Yi Baiti'
	bts_bg = 'SystemButtonFace'
	
	# Canvas
	login_can = Canvas(reg_window, width=311, height=45, bg='#2f354d')
	login_can.place(x=2, y=2)

	# Funtion
	def bts_event_enter(e):
		register_bts.config(fg="#0c36c2")

	def bts_event_leave(e):
		register_bts.config(fg="black")

	# GUI
		# Label
	message = Label(reg_window, text="Create Account: ", font=(font_r, 23), fg=text_color,  bg=background_button_color)
	message.place(x=8, y=8)

	reg_fname = Label(reg_window, text="First name: ", font=(font_r, 20))
	reg_fname.place(x=15, y=55)

	reg_lname = Label(reg_window, text="Last name: ", font=(font_r, 20))
	reg_lname.place(x=15, y=130)

	reg_email = Label(reg_window, text="Email: ", font=(font_r, 20))
	reg_email.place(x=15, y=205)
	regex_email = Label(reg_window, text="*Enter valid Email.", font=(font_r, 10))
	regex_email.place(x=35, y=270)

	reg_pass = Label(reg_window, text="Password: ", font=(font_r, 20))
	reg_pass.place(x=15, y=285)
	regex_pass = Label(reg_window, text="*Password must contain 3 numbers and 5 letters min.", font=(font_r, 10))
	regex_pass.place(x=35, y=350)

	Label(reg_window, text="___________________", font=(font_r, 20)).place(x=35, y=88)
	Label(reg_window, text="___________________", font=(font_r, 20)).place(x=35, y=163)
	Label(reg_window, text="___________________", font=(font_r, 20)).place(x=35, y=238)
	Label(reg_window, text="___________________", font=(font_r, 20)).place(x=35, y=318)

		# Entry box
	reg_fname_e = Entry(reg_window, bd=0, font=(font_r, 17), bg=bts_bg)
	reg_fname_e.place(x=39, y=85)

	reg_lname_e = Entry(reg_window, bd=0, font=(font_r, 17), bg=bts_bg)
	reg_lname_e.place(x=39, y=160)

	reg_email_e = Entry(reg_window, bd=0, font=(font_r, 17), bg=bts_bg)
	reg_email_e.place(x=39, y=235)
 	
	reg_pass_e = Entry(reg_window, bd=0, font=(font_r, 17), bg=bts_bg, show="*")
	reg_pass_e.place(x=39, y=315)


	register_bts = Button(reg_window, text="Register", bg=bts_bg, font=(font_r, 35), bd=0, command=check)
	register_bts.place(x=155, y=375)
	register_bts.bind("<Enter>", bts_event_enter)
	register_bts.bind("<Leave>", bts_event_leave)


# GUI 

	# Frame
tree_frame = LabelFrame(root, padx=15, pady=15)
tree_frame.pack(padx=(150, 0), pady=15)

# TREEVIEW and STYLE ttk
my_tree = ttk.Treeview(tree_frame)
style = ttk.Style()
   # Define columns
my_tree["columns"] = ("Domain", "User", "Password", "Assign AGI")
   # Format columns
my_tree.column("#0", width=15, minwidth=25)
my_tree.column("Domain", width=90, anchor=W)
my_tree.column("User", width=120, anchor=W)
my_tree.column("Password", width=120, anchor=W)
my_tree.column("Assign AGI", width=50, anchor=CENTER)
   # Create heading
my_tree.heading("#0", text="AGI", anchor=W)
my_tree.heading("Domain", text="Domain", anchor=W)
my_tree.heading("User", text="User", anchor=W)
my_tree.heading("Password", text="Password", anchor=W)
my_tree.heading("Assign AGI", text="Assign AGI", anchor=CENTER)
my_tree.pack(ipady=450, ipadx=100)
# Style theme
style.theme_use('clam')
# Style Treeview
style.configure("Treeview",
	background='silver',
	foreground="black",
	fieldbackground='silver'
	)
style.map('Treeview', background=[('selected', '#2f354d')])
   # Buttons
add_password = Button(root, text="Add Password", state='disable', font=(font, font_size), fg=text_color, bd=0, bg=background_button_color, activebackground=activebackground_color, command=add_password)
left_side_rec.create_window(85, 50, window=add_password)
add_password.bind('<Enter>', button_event_enter)
add_password.bind('<Leave>', button_event_leave)

edit_password = Button(root, text="Edit Password", state='disable', font=(font, font_size), bd=0, fg=text_color, bg=background_button_color, activebackground=activebackground_color, command=edit_password)
left_side_rec.create_window(85, 100, window=edit_password)
edit_password.bind('<Enter>', button_event_enter2)
edit_password.bind('<Leave>', button_event_leave2)

delete_password = Button(root, text="Delete Password", state="disable", font=(font, font_size), fg=text_color, bd=0, bg=background_button_color, activebackground=activebackground_color, command=delete_password)
left_side_rec.create_window(92, 200, window=delete_password)
delete_password.bind('<Enter>', button_event_enter3)
delete_password.bind('<Leave>', button_event_leave3)

reg_bts = Button(root, text="Register New User", font=(font, font_size),  fg=text_color, bd=0, bg=background_button_color, activebackground=activebackground_color, command=create_user)
left_side_rec.create_window(75, 580, window=reg_bts)
reg_bts.bind('<Enter>', button_event_color_no_image)
reg_bts.bind('<Leave>', button_event_color_no_image_leave)

login_bts = Button(root, text="Log-In", font=(font, 12),  fg=text_color, bd=0, bg=background_button_color, activebackground=activebackground_color, command=log_in)
left_side_rec.create_window(35, 550, window=login_bts)
login_bts.bind('<Enter>', button_event_color_no_image)
login_bts.bind('<Leave>', button_event_color_no_image_leave)

logout_bts = Button(root, text="Log-out", font=(font, 12),  fg=text_color, bd=0, bg=background_button_color, activebackground=activebackground_color, command=log_out)
left_side_rec.create_window(110, 550, window=logout_bts)
logout_bts.bind('<Enter>', button_event_color_no_image)
logout_bts.bind('<Leave>', button_event_color_no_image_leave)

   # Entry box
search_bar = Entry(root, width=15, fg='lightgrey', font=(font, font_size))
left_side_rec.create_window(75, 150, window=search_bar)
search_bar.insert(0, "Insert AGI...")
search_bar.bind('<1>', delete_text)

   # Text on CANVAS
login_statue = left_side_rec.create_text(75, 500, text=f"Not log-in", font=(font, 10), fill='red')




# FOOTER
footer = Label(root, text=f"All CopyRight Reserved {copy_right}Yoan Tufel.",  fg=text_color,)
footer.place(x=590, y=574)
agi_leg = Label(root, text="*AGI = Account Grouping identification.",  fg=text_color)
agi_leg.place(x=250, y=574)


root.mainloop()
