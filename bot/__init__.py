import os
import time
import logging
from logging.handlers import RotatingFileHandler

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DB_URI = os.environ.get("DB_URI", "")
SESSION_STRING = os.environ.get("SESSION_STRING", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "1790509785"))
SESSION = os.environ.get("SESSION", "ADV-Auto-Filter-Bot-V2")
SLEEP_THRESHOLD = int(os.environ.get("SLEEP_THRESHOLD"))
VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
