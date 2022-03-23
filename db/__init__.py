import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

engine = sqlalchemy.create_engine(os.environ.get('DATABASE'))
Session = sessionmaker(bind=engine)














#engine = sqlalchemy.create_engine('sqlite:///database.db')  tÄMÄ VIETY .ENV
engine = sqlalchemy.create_engine(os.)

Session = sessionmaker(bind=engine)