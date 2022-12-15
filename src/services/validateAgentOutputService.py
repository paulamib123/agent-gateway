import json
import jsonschema
import uuid

from src.models.agentLogs import AgentLogs

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


def createAgentLogObject(deviceData, jsonData):
    operatingSystem = deviceData['OperatingSystem']
    release = deviceData['Release']
    version = deviceData['Version']
    machine = deviceData['Machine']
    processor = deviceData['Processor']
    hostname = deviceData['Hostname']
    ipAddr = deviceData['IPAddr']
    mac = deviceData['MAC']
    installedSoftware = deviceData['InstalledSoftware']
    runningProcesses = deviceData['RunningProcesses']
    firewallStatus = deviceData['FirewallStatus']
    usbStatus = deviceData['USBStatus']
    
    log = AgentLogs(
        os = operatingSystem,
        release = release,
        version = version,
        machine = machine,
        processor = processor,
        hostname = hostname,
        ip4 = ipAddr,
        mac = mac,
        installed_software = installedSoftware,
        running_process = runningProcesses,
        firewall_status = firewallStatus,
        usb_status = usbStatus,
        json_data = jsonData
    )

    return log


def postAgentLog(deviceData, db):
    jsonData = json.dumps(deviceData)

    log = createAgentLogObject(deviceData, jsonData)

    db.session.add(log)
    db.session.commit()


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

    

