import json
import os

class Settings(object):
    def __init__(self,saveLogin=False, benutzer="",pw="",autoLogin=False):
        self.__saveLogin=saveLogin
        self.__autoLogin=autoLogin
        self.__benutzername=benutzer
        self.__password=pw
        self.changes=False
        self.loadSettings()
    def saveSettings(self):
        if self.changes:
            with open('settings.json', 'w', encoding='utf-8') as f:
                json.dump(vars(self), f, ensure_ascii=False, indent=4)
    def loadSettings(self):
        if os.path.isfile('settings.json'):
            with open('settings.json', 'r', encoding='utf-8') as f:
                self.__dict__ = json.load(f)
        changes=False

    @property
    def saveLogin(self):
        return self.__saveLogin
    @saveLogin.setter
    def saveLogin(self,saveLogin):
        if self.saveLogin!=saveLogin:
            self.__saveLogin = saveLogin
            self.changes=True
    @property
    def autoLogin(self):
        return self.__autoLogin
    @autoLogin.setter
    def autoLogin(self,autoLogin):
        if self.autoLogin!=autoLogin:
            self.__autoLogin = autoLogin
            self.changes=True
    @property
    def benutzername(self):
        return self.__benutzername
    @benutzername.setter
    def benutzername(self,benutzername):
        if self.benutzername!=benutzername:
            self.changes = True
            self.__benutzername = benutzername


    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        if self.password!=password:
            self.__password = password
            self.changes=True


settings=Settings()