from dotenv import load_dotenv 
import os 
from pathlib import Path 

load_dotenv() 
USER_PATH = Path(os.getenv(
    'USER_PATH' 
))

SERVICE_PATH = Path(os.getenv(
    'SERVICE_PATH'
))

PASSWORD = os.getenv("PASSWORD")