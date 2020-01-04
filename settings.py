import os
import gspread, logging
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from funciones import *

# env
load_dotenv(verbose=True)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_LIST = os.getenv("ADMIN_LIST").split(",")

F_HORA = '%H:%M:%S'
F_FECHA = '%d/%m/%Y'
F_FECHAHORA = '%d/%m/%Y %H:%M:%S'

# gdrive
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gdrive.json', scope)
GOOGLE_CLIENT = gspread.authorize(creds)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
