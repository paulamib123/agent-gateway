import os
import logging
from datetime import datetime
from pytz import timezone, utc


def customTime(*args):
        utc_dt = utc.localize(datetime.utcnow())
        my_tz = timezone("Asia/Calcutta")
        converted = utc_dt.astimezone(my_tz)
        return converted.timetuple()

logging.Formatter.converter = customTime

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
LOG_DIR = os.path.realpath(os.path.join(ROOT_DIR, '..')) + "/logs"


logging.basicConfig(filename=LOG_DIR + "/api.log", 
                            level=logging.INFO, 
                            format="%(asctime)s:%(levelname)s: %(message)s",
                            datefmt='%Y-%m-%d %H:%M:%S')
       
logging.info("Logger Configured And Started")