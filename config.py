from urllib.parse import quote_plus
import os
from dotenv import load_dotenv
load_dotenv()

password=quote_plus(os.getenv("PASSWORD"))
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@localhost:5432/etdb'.format(password)
SQLALCHEMY_TRACK_MODIFICATIONS= False