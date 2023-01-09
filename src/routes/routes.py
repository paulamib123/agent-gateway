from flask import request, jsonify
import logging

from src.services.agentLog import postAgentLogToDB
from src.services.validateAgentLog import validateAgentOutputSchema


REQUEST_SUCCESS_CODE = 200
SERVER_ERROR_CODE = 500
BAD_REQUEST_CODE = 400
EMPTY_JSON_ERROR = "JSON data is empty"

def registerRoutes(app, Session):
    @app.route("/", methods = ["POST"])
    def validationAPI():
        try:
            data = request.json
            result = validateAgentOutputSchema(data)

            if not data:
                return jsonify({"error" : EMPTY_JSON_ERROR}), BAD_REQUEST_CODE

            if result[1]:
                postAgentLogToDB(data, Session)
                
            return jsonify(result[0]), REQUEST_SUCCESS_CODE
        
        except ValueError as error:
            logging.exception(error)

            return jsonify({'error' : str(error)}), BAD_REQUEST_CODE
        
        except Exception as error:
            logging.exception(error)

            return jsonify({'error' : str(error)}), SERVER_ERROR_CODE