# Databrary module

# Import dependencies
import requests
import pandas

#-----------------------------------------------------------------------------
# Access Databrary API to get current system stats
def get_db_stats(type = "all", vb = False):
	"Current stats from Databrary API"

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

#-----------------------------------------------------------------------------
# login to Databrary
def login_db(vb = False, return_resp = True):

	login_url = "https://nyu.databrary.org/api/user/login"

	email = input("Account id (email): ")
	pw = input("Password: ")
	payload = {"email": email, "password": pw}

	r = requests.post(login_url, data = payload)

	if (r.status_code == 200):
		print("Logged in.")
		if (return_resp):
		  return(r.text)
	else:
		print("Log in failed with HTTP status " + r.status_code + "\n")
