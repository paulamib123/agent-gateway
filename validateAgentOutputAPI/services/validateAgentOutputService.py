import json
import jsonschema
import uuid

VALIDATION_SUCCESS_MESSAGE = "Validation Successful"
VALIDATION_ERROR_CODE = 400
PATH = "../../data/"

def readJSON(fileName):
    with open(fileName) as file:
        data = json.load(file)

    return data

def writeJSON(data):
     with open(PATH + "output-" + str(uuid.uuid4()) + ".json", "w") as file:
            file.write(json.dumps(data))

def getValidationErrors(validator, deviceData):
    errors = []
    validationErrors = sorted(validator.iter_errors(deviceData), key=lambda error: error.path)

    if not validationErrors:
        return errors

    for error in validationErrors:
    
        errorDetails = { 
            "property" : error.path[0], 
            "message" : error.message, 
            "expectedFormat" : error.schema,
            "errorCode": VALIDATION_ERROR_CODE
        }
        errors.append(errorDetails)

    return errors
       

def validateAgentOutput(deviceData):
    try:
        schema = readJSON("../schema/agentOutputSchema.json")
        validator = jsonschema.Draft7Validator(schema)

        errors = getValidationErrors(validator, deviceData)
        
        if not errors:
            result = { "message" : VALIDATION_SUCCESS_MESSAGE }
            return (result, True)
        else:
            return (errors, False)
        
    except jsonschema.ValidationError as validationError:
        error = {"message": validationError}
        return error

    
