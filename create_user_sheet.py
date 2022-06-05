''' Encryptes password, create key, writes all the user info to the UserSheet.csv
for further login'''

from os import path
from tkinter import messagebox
from hashlib import sha256
from cryptography.fernet import Fernet
import csv
import os

username = os.getlogin()
def user_create_csv(fname, lname,  email ,password):
	key = Fernet.generate_key()
	password_encode = sha256(password.encode('ascii')).hexdigest()
	if len(fname) == 0:
		messagebox.showwarning("Missig info", "Register denied, missing information.")
	else:
			
			# UserSheet
		    if path.exists(f"C:/csv/UserSheet.csv"):
		        with open(f"C:/csv/UserSheet.csv", "a", newline='') as csvfile:
		            filewriter = csv.writer(csvfile)
		            filewriter.writerow([fname.capitalize(), lname.capitalize(), email, password_encode, key])

		        # User password sheet,with unique key
		        if not path.exists(f"C:/csv/{key}.csv"):
		        	with open(f"C:/csv/{key}.csv", "w", encoding='utf-8') as create_file:
		        		created_file = csv.writer(create_file)
		        		created_file.writerow(['Domain', 'User', 'Password', 'Assign AGI'])

		    else:
		    	# UserSheet
		        with open(f"C:/csv/UserSheet.csv", "w", newline='', encoding='utf-8') as csvfile:
		            filewriter = csv.writer(csvfile)
		            filewriter.writerow(['First-name', 'Last-name', 'Email', 'Password', 'Code Verification'])
		            filewriter.writerow([fname.capitalize(), lname.capitalize(), email, password_encode, key])
		        # User password sheet,with unique key
		        with open(f"C:/csv/{key}.csv", "w") as create_file:
		        	created_file = csv.writer(create_file)
		        	created_file.writerow(['Domain', 'User', 'Password', 'Assign AGI'])

       

