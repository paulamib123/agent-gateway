import jsonschema
import uuid
import json
import logging

from src.config.definitions import ROOT_DIR

VALIDATION_SUCCESS_MESSAGE = "Validation Successful"
VALIDATION_ERROR_CODE = 400
PATH = "../../data/"
SCHEMA_PATH = ROOT_DIR + "/schema/agentOutputSchema.json"


def validateAgentOutputSchema(deviceData):
    try:
        message, isValid = validateJSON(deviceData)

        if not isValid:
            return (message, False)

        schema = readJSON(SCHEMA_PATH)
        validator = jsonschema.Draft7Validator(schema)

        errors = getValidationSchemaErrors(validator, deviceData)
        
        if not errors:
            result = {"message" : VALIDATION_SUCCESS_MESSAGE}
            return (result, True)
        else:
            return (errors, False)
        
    except jsonschema.ValidationError as validationError:
        logging.error("Validation Error")
        return {"error" : validationError}


def validateJSON(deviceData):
    keys = ["OperatingSystem", "Release", "Version", "Machine", 
            "Processor", "Hostname", "IPAddr", "MAC"]
            
    for key in keys:
        if deviceData.get(key) is None:
            logging.error("{} field is missing or empty".format(key))
            return ({"error" : "{} field is missing or empty".format(key)}, False)
    
    logging.debug("All compulsory JSON fields exist")
    return ({}, True)


def getValidationSchemaErrors(validator, deviceData):
    errors = []
    validationErrors = sorted(validator.iter_errors(deviceData), key=lambda error: error.path)

    if not validationErrors:
        logging.debug("Schema matched perfectly")
        return errors

    for error in validationErrors:
    
        errorDetails = { 
            "property" : error.path[0], 
            "message" : error.message, 
            "expectedFormat" : error.schema,
            "errorCode": VALIDATION_ERROR_CODE
        }
        errors.append(errorDetails)

    logging.debug("Found errors while validating schema")
    return errors


def readJSON(fileName):
    with open(fileName) as file:
        data = json.load(file)

    return data


def writeJSON(data):
     with open(PATH + "output-" + str(uuid.uuid4()) + ".json", "w") as file:
            file.write(json.dumps(data))