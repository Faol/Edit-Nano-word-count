from core import exceptions
from core import c_nanoAPI as nanoApi


#---------------------------------------------------------------------------------
#Personenklasse enthaelt alle Personen, die im Personenmanager hinzugefuegt wurden
#---------------------------------------------------------------------------------
class Person(object):
    def __init__(self,nanoNick,nanoId,romanTitel=None,romanId=None,challengeId=None):
        self.nanoNick=nanoNick #NaNoNick
        self.nanoId=nanoId #Id aus dem NaNo, auch allgemeine Id
        self.romanTitel=romanTitel
        self.romanId=romanId
        self.challengeId=challengeId
        

class PersonManager(object):
    person_ID=1
    def __init__(self,api):
        self.api=api
        self.persons={}
        self.personNick={}
        self.activePerson=None
    def insertPerson(self,person):
        self.persons[person.nanoId]=person
        self.personNick[person.nanoNick]=person
    def addNew(self,nanoNick):
        id = self.api.getId(nanoNick)
        if id:
            self.insertPerson(Person(nanoNick,id))
            return True
        else:
            return False
    def addTest(self,nanoNick,id):
        self.insertPerson(Person(nanoNick, id))
    def setActivePerson(self,nanoNick):
        print("Active Person= "+nanoNick)
        if nanoNick in self.personNick:
            self.activePerson=self.personNick[nanoNick]
        else:
            if self.addNew(nanoNick):
                self.activePerson=self.personNick[nanoNick]

personenManager = PersonManager(nanoApi.api)