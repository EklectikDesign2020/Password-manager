''' Append password to users password sheet'''

from os import path
from tkinter import messagebox

import csv
import os

username = os.getlogin()

def append_user_sheet(password_list, filename_name_key):

	if len(password_list) == 0:
		messagebox.showwarning("Missig info", "Adding Password denied, missing information.")
	else:
		
		    if path.exists(f"C:/csv/{filename_name_key}.csv"):
		        with open(f"C:/csv/{filename_name_key}.csv", "a", newline='') as csvfile:
		            filewriter = csv.writer(csvfile) 
		            filewriter.writerow(password_list)
		            csvfile.close()
		    else:
		    	messagebox.showwarning("Non User", "No User is loged in.")


       

