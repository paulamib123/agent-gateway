import os
import logging

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s: %(message)s")