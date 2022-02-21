import os
import time
import logging
from logging.handlers import RotatingFileHandler

SESSION_NAME = os.environ.get("SESSION_NAME", "ADV-Auto-Filter-Bot-V2")
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
WORKERS = int(os.environ.get("WORKERS", "200"))
PLUGINS = dict(os.environ.get("PLUGINS", {"root": "bot/plugins"}))
SLEEP_THRESHOLD = int(os.environ.get("SLEEP_THRESHOLD", "10"))
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
SESSION_STRING = os.environ.get("SESSION_STRING", "")
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
