''' Check regex for email and password count '''

import re

def password(passw):

	count_digit = 0
	count_letter = 0
	for x in passw:
		if x.isdigit():
			count_digit += 1
		else:
			count_letter += 1
	return count_digit > 2 and count_letter > 4


def email_control(email):

    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # Example email@email.com or email.email@email.com
    if not re.search(regex_email, email):
        return False
    else:
        return True

