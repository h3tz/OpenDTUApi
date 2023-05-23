import requests
from requests.auth import HTTPBasicAuth

class opendtuapi:

    def __init__(self, ip, username, password, serial):
        self.dtuUrl = ip
        self.dtuUser = username
        self.dtuPassword = password
        self.dtuSerial = serial

    def __getHoymilesIndex(self):
        status = f"http://{self.dtuUrl}/api/livedata/status"

    def getlivestatus(self):
        urlToRequest = f"http://{self.dtuUrl}/api/livedata/status"
        resp = requests.get(url=urlToRequest)
        return resp.json()

    def getCurrentWatt(self):
        try:
            status = self.getlivestatus()
            ret =status["inverters"][self.hoymilesCount ]["AC"]["0"]["Power"]["v"]
            ret = round(ret, 2)
            return ret
        except:
            return 0

    def getInverterTemp(self):
        try:
            status = self.getlivestatus()
            ret =status["inverters"][self.hoymilesCount ]["INV"]["0"]["Temperatur"]["v"]
            return ret
        except:
            return 0

    def isproducing(self):
        try:
            status = self.getlivestatus()
            return status["inverters"][self.hoymilesCount ]["producing"]
        except:
            return False

    def setLimit(self, setpoint):
        try:
            status = self.getlivestatus()


            try:
                r = requests.post(
                    url=f'http://{self.dtuUrl}/api/limit/config',
                    data=f'data={{"serial":"114184403178", "limit_type":0, "limit_value":{setpoint}}}',
                    auth=HTTPBasicAuth(self.dtuUser, self.dtuPassword),
                    headers={'Content-Type': 'application/x-www-form-urlencoded'}
                )
            except:
                print('Fehler beim Senden der Konfiguration')
        except:
            return 0

    def getLimit(self):
        try:
            status = self.getlivestatus()
            return status["inverters"][self.hoymilesCount]["limit_absolute"]
        except:
            return 0

    def hasRadioProblems(self):
        try:
            status = self.getlivestatus()
            return status["hints"]["radio_problem"]
        except:
            return True

    def getModuleWatt(self, index):
        try:
            status = self.getlivestatus()
            return status["inverters"][self.hoymilesCount ]["DC"][str(index-1)]["Power"]["v"]
        except:
            return 0