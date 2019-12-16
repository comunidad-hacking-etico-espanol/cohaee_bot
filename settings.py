import os
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

# env
load_dotenv(verbose=True)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_LIST = os.getenv("ADMIN_LIST").split(",")

# gdrive
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gdrive.json', scope)
GOOGLE_CLIENT = gspread.authorize(creds)

