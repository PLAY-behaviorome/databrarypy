# Databrary module

# Import dependencies
import requests
import pandas
import keyring

#-----------------------------------------------------------------------------
# Access Databrary API to get current system stats
def get_db_stats(type = "all", vb = False):
	"Current stats from Databrary API"

	if (not(isinstance(type, str))):
		print("type must be a string.")
		return('')
	if (not(isinstance(vb, bool))):
		print("vb must be Boolean.")
		return('')

	stats_activity_url = "https://nyu.databrary.org/api/activity"

	if vb:
		print("Sending GET request to " + stats_activity_url + "\n")
	r = requests.get(stats_activity_url)
	
	if (r.status_code == 200):
		if (type == 'all'):
			return(r.content)
		else:
			# Convert content to data.frame
			df = pandas.read_json(r.content, typ = 'series')
			return(df)
	else:
		print("Download failed with HTTP status " + r.status_code + "\n")
		return('')

#-----------------------------------------------------------------------------
# login to Databrary
def login_db(username, vb = False, stored_credentials = False, system_credentials = True):
	"Log in to Databrary"

	# Check parameters
	if (not(isinstance(vb, bool))):
		print("vb must be Boolean.")
		return('')
	if (not(isinstance(stored_credentials, str))):
		print("stored_credentials must be Boolean.")
		return('')
	if (not(isinstance(system_credentials, str))):
		print("system_credentials must be Boolean.")
		return('')

	login_url = "https://nyu.databrary.org/api/user/login"

	if (stored_credentials):
		if(vb):
			print("Using stored credentials.")
	elif (system_credentials):
		if (username == ''):
			print("Please enter your Databrary user ID (email).")
			username <- input(prompt="User ID: ")
		if (keyring.get_keyring() != ''):
				kl = keyring.get_password("databrary", username)
				if (kl != 'None'):
					password = kl
				else:
					if (vb):
						print("No password for user: ", username, "\n")
						return('')
		else:
			if (vb):
				print("No stored credentials for user: ", username, "\n")
				return('')
	else:
		# Get login credentials
		username = input("Databrary user ID (email): ")
		pw = input("Password: ")

		# Check login credentials
		if (not(isinstance(username, str))):
			print("Account ID must be a string.")
			return('')
		if (not(isinstance(pw, str))):
			print("Password must be a string")
			return('')

	# POST request
	payload = {"email": username, "password": pw}
	r = requests.post(login_url, data = payload)

	if (r.status_code == 200):
		print("Logged in.")
		if (return_resp):
		  return(r.text)
	else:
		print("Log in failed with HTTP status " + r.status_code + "\n")
