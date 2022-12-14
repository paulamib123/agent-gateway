from flask import Flask, request, make_response, jsonify
from validateAgentOutputAPI.services.validateAgentOutputService import validateAgentOutput, writeJSON

REQUEST_SUCCESS_CODE = 200
SERVER_ERROR_CODE = 500
SERVER_ERROR_MESSAGE = "Server Error"

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def validateAPI():
    #try:
        data = request.json
        message = validateAgentOutput(data)
    
        if message[1]:
            writeJSON(data)
            
        return jsonify(message[0]), REQUEST_SUCCESS_CODE
    # except:
    #     error = { "message" : SERVER_ERROR_MESSAGE }
    #     return jsonify(error), SERVER_ERROR_CODE

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
