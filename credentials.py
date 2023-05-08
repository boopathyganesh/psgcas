from google.oauth2.credentials import Credentials
import json

with open('client_secret_232998573646-2fgvp7bcc924hq58ms5k739e91j8tavb.apps.googleusercontent.com.json', 'r') as f:
    data = json.load(f)

credentials = Credentials.from_authorized_user_info(info=data)
