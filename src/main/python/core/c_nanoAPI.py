import requests
from PyQt5.QtWidgets import QMessageBox
from urllib3.exceptions import NewConnectionError
from requests.exceptions import ConnectionError

from core import exceptions, login
import json


class NanoApi(object):
    def __init__(self, auth=None):
        self.auth = auth

    # ---------------------------------------------------------------
    # erstellt Nano Authentifizierungs-Token und gibt dieses zurück
    # ---------------------------------------------------------------
    def sign_in(self, username, password):
        sign_in = {"identifier": username, "password": password}
        try:
            response = requests.post("https://api.nanowrimo.org/users/sign_in", json=sign_in)
            if response:
                msg = "Login successful"
                #print(msg)
                self.auth = {"Authorization": response.json()["auth_token"]}
                return True, msg,0
            elif response.status_code == 401:
                msg = "Wrong username/password. Try again."
                #print(msg)
                return False,msg,1
            elif response.status_code == 404:
                msg = "Login page not found! Please contact me!"
                print(msg)
                return False, msg,2
            else:
                msg = "Error: Please try again later! (Status Code:" + str(response.status_code) + ")"
                #print(msg)
                return False, msg,2
        except ConnectionError:
            msg="No internet connection. Try again."
            return False,msg,1

    # setzt auth
    def logout(self):
        self.auth = None

    def getId(self, nanoNick):
        gotId=False
        if self.auth:
            response = requests.get("https://api.nanowrimo.org/users/" + nanoNick, headers=self.auth)
            if response:
                msg="Id abgerufen"
                gotId=True
            elif response.status_code == 401:
                msg = "Login abgelaufen. Bitte erneut einloggen."
                self.apiErrorMessageLogin(msg)
            elif response.status_code == 404:
                msg = "User "+nanoNick+ " existiert nicht."
                self.apiErrorMessage(msg)
            else:
                msg = "Error: Please try again later! (Status Code:" + str(response.status_code) + ")"
                self.apiErrorMessage(msg)
        else:
            msg="Du bist nicht eingeloggt. Bitte erst einloggen."
            self.apiErrorMessageLogin(msg)
        return gotId

    def fileFromAPI(self, url, speicherort):
        if self.auth:
            response = requests.get(url, headers=self.auth)
            if response:
                with open(speicherort + ".json", 'w') as outfile:
                    json.dump(response.json(), outfile)
            else:
                raise exceptions.apiLoadingError("Loading data from NaNo-Api failed. Try again later")
        else:
            raise exceptions.AuthError("Authentification failed. Login first.")

    def apiErrorMessageLogin(self,msg):
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Api Error")
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.setEscapeButton(QMessageBox.Cancel)
        msgBox.accepted.connect(login.retry_login_dialog)
        msgBox.rejected.connect(lambda: None)
        msgBox.exec_()
    def apiErrorMessage(self,msg):
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Api Error")
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.setEscapeButton(QMessageBox.Ok)
        msgBox.accepted.connect(lambda: None)
        msgBox.exec_()



api = NanoApi()
