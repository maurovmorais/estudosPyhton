import os
from dotenv import load_dotenv

load_dotenv()


database_infos ={ 
    'database': os.environ['DATABASE'],
    'port': os.environ['PORT'],
    'user': os.environ['USERNAMEDB'],
    'password': os.environ['PASSWORD']
}