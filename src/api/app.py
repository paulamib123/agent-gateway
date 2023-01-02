from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import logging

from src.config.dbConfig import uri
from src.routes.routes import registerRoutes


engine = create_engine(uri, pool_size=10)

logging.info("Connected to Database")

Session = sessionmaker(bind = engine)

def appConfig():
    app = Flask(__name__)
    return app

app = appConfig()
registerRoutes(app, Session)

if __name__ == "__main__": 
    host = "0.0.0.0"
    port = 5000   
    app.run(host=host, port=port, debug=True)
    
