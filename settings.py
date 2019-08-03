import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_LIST     = os.getenv("ADMIN_LIST").split()
DB_FILENAME    = os.getenv("DB_FILENAME")
