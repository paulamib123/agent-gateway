import os
import logging

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
LOG_DIR = os.path.realpath(os.path.join(ROOT_DIR, '..')) + "/logs"



logging.basicConfig(filename=LOG_DIR + "/api.log", level=logging.INFO, format="%(asctime)s:%(levelname)s: %(message)s")