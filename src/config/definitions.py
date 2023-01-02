import os
import logging

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s:%(levelname)s: %(message)s")