from typing import Dict, List
import logging

from src.models.agentLogs import AgentLogs

class AgentLog():

    def __init__(self, log: Dict[str, str]):
        self.operatingSystem: str = log.get("OperatingSystem")
        self.release: str = log.get("Release")
        self.version: str = log.get("Version")
        self.machine: str = log.get("Machine")
        self.processor: str = log.get('Processor')
        self.hostname: str = log.get('Hostname')
        self.ip4: str = log.get('IPAddr')
        self.mac: str = log.get('MAC')
        self.potentiallyUnwantedSoftwares: List[str] = self.setEmptyToNull('PotentialyUnwantedSoftware', log)
        self.runningProcesses: List[str] = self.setEmptyToNull('RunningProcesses', log)
        self.firewallStatus: str = self.setEmptyToNull('FirewallStatus', log)
        self.usbStatus: str = self.setEmptyToNull('USBStatus', log)
    
    def setEmptyToNull(self, key, log):
        value = log.get(key)
        return None if not value else value

    def createDBObject(self, jsonData):
        
        Agentlog = AgentLogs(
            os = self.operatingSystem,
            release = self.release,
            version = self.version,
            machine = self.machine,
            processor = self.processor,
            hostname = self.hostname,
            ip4 = self.ip4,
            mac = self.mac,
            potentially_unwanted_softwares = self.potentiallyUnwantedSoftwares,
            running_process = self.runningProcesses,
            firewall_status = self.firewallStatus,
            usb_status = self.usbStatus,
            json_data = jsonData
        )
        
        logging.debug("Created Agent Log Object for database")

        return Agentlog


def postAgentLogToDB(deviceData, Session):
    agentLog = AgentLog(deviceData)

    logDBObject = agentLog.createDBObject(deviceData)
    
    session = Session()

    session.add(logDBObject)
    logging.info("Added Agent Log with MAC Address {} to database".format(agentLog.mac))

    session.commit()
    logging.info("Committed Agent Log with MAC Address {} to database".format(agentLog.mac))


    
