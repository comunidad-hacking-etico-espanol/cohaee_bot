import os
import logging
from dotenv import load_dotenv

# env
load_dotenv(verbose=True)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_LIST = os.getenv("ADMIN_LIST").split(",")
CHAT_LIST = os.getenv("CHAT_LIST").split(",")

# const
F_HORA = '%H:%M:%S'
F_FECHA = '%d/%m/%Y'
F_FECHAHORA = '%d/%m/%Y %H:%M:%S'

#config
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
