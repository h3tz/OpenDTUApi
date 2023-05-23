import requests
from requests.auth import HTTPBasicAuth

class opendtuapi:

    def __init__(self, ip, username, password, serial):
        self.dtuUrl = ip
        self.dtuUser = username
        self.dtuPassword = password
        self.dtuSerial = serial

    def __getHoymilesIndex(self, responce):
        for idx, mydtu in enumerate(responce["inverters"]):
            if mydtu["serial"] == self.dtuSerial:
                break
        return idx

    def __getACElement(self,element):
        try:
            status = self.getlivestatus()
            myelement = status["AC"]["0"][element]["v"]
            return round(myelement, 3)
        except:
            return 0

    def __getDCElement(self,element, inputIndex):
        try:
            status = self.getlivestatus()
            myelement = status["DC"][str(inputIndex - 1)][element]["v"]
            return round(myelement, 3)
        except:
            return 0

    def getlivestatus(self):
        urlToRequest = f"http://{self.dtuUrl}/api/livedata/status"
        resp = requests.get(url=urlToRequest)
        decoded = resp.json()
        indexDtu = self.__getHoymilesIndex(decoded)
        return decoded["inverters"][indexDtu]

    def getACPower(self):
        return self.__getACElement("Power")

    def getACVoltage(self):
        return self.__getACElement("Voltage")

    def getACCurrent(self):
        return self.__getACElement("Current")

    def getACFreq(self):
        return self.__getACElement("Frequency")

    def getACReactivePower(self):
        return self.__getACElement("ReactivePower")

    def getACYieldDay(self):
        return self.__getACElement("YieldDay")

    def getACEfficience(self):
        return self.__getACElement("Efficiency")

    def getDCPower(self, inputIndex):
        return self.__getDCElement("Power",inputIndex)

    def getDCVoltage(self, inputIndex):
        return self.__getDCElement("Voltage",inputIndex)

    def getDCCurrent(self, inputIndex):
        return self.__getDCElement("Current",inputIndex)

    def getTemp(self):
        try:
            status = self.getlivestatus()
            return status["INV"]["0"]["Temperatur"]["v"]
        except:
            return 0

    def isproducing(self):
        try:
            status = self.getlivestatus()
            return status[self.hoymilesCount ]["producing"]
        except:
            return False

    def setLimit(self, setAbsolutWatt):
        try:
            status = self.getlivestatus()
            try:
                r = requests.post(
                    url=f'http://{self.dtuUrl}/api/limit/config',
                    data=f'data={{"serial":"{self.dtuSerial}", "limit_type":0, "limit_value":{setAbsolutWatt}}}',
                    auth=HTTPBasicAuth(self.dtuUser, self.dtuPassword),
                    headers={'Content-Type': 'application/x-www-form-urlencoded'}
                )
            except:
                return True
        except:
            return False

    def hasRadioProblems(self):
        try:
            status = self.getlivestatus()
            return status["hints"]["radio_problem"]
        except:
            return True