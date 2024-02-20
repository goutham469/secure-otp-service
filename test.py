import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()

print(os.getenv("SENDER_MAIL"))
print(os.getenv("SENDER_KEY"))