from dotenv import load_dotenv
import json
import os

from ngrok_executor import start_ngrok

load_dotenv()

WEBHOOK_HOST = start_ngrok()
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH")
WEBAPP_HOST = os.environ.get("WEBAPP_HOST")
WEBAPP_PORT = os.environ.get("WEBAPP_PORT")
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
TOKEN = os.environ.get("TOKEN")
ADMIN_ID_LIST = json.loads(os.environ.get("ADMIN_ID_LIST"))
