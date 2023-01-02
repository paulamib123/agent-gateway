import os
import sys
from dotenv import load_dotenv
import logging

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
            logging.error('enviornment variable {} is not defined'.format(key))
    
    if flag:
        sys.exit("Exited")

validateCredentials(credentials)

uri = "postgresql://{username}:{password}@{host}:{port}/{database}".format(**credentials)
uri = uri.replace('"', '')

