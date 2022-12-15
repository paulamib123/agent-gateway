import os
import sys
from dotenv import load_dotenv

load_dotenv()

credentials = {
    "username" : 
        os.getenv("DATABASE_USERNAME"),
    "password" : 
        os.getenv("DATABSE_PASSWORD"),
    "host" : 
        os.getenv("DATABSE_HOST"),
    "port" :
        os.getenv("DATABSE_PORT"),
    "database" :
        os.getenv("DATABASE_NAME")
}


def validateCredentials(credentials):

    flag = False

    for key, value in credentials.items():
        if value is None:
            flag = True
            print(f'{key} variable is not defined\n')
    
    if flag:
        sys.exit("Exited")

validateCredentials(credentials)

uri = "postgresql://{username}:{password}@{host}:{port}/{database}".format(**credentials)
uri = uri.replace('"', '')

