import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv('EMAIL')
MY_PASSWORD = os.getenv('PASSWORD')