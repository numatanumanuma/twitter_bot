import os
from dotenv import load_dotenv

load_dotenv()

TW_CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY')
TW_CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET')
TW_TOKEN = os.environ.get('TW_TOKEN')
TW_TOKEN_SECRET = os.environ.get('TW_TOKEN_SECRET')
