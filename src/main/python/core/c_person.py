from core import exceptions


#---------------------------------------------------------------------------------
#Personenklasse enthaelt alle Personen, die im Personenmanager hinzugefuegt wurden
#---------------------------------------------------------------------------------
class Person(object):
    def __init__(self,nick,nanoNick,nanoId,romanTitel=None,romanId=None):
        self.nick=nick #Forennick
        self.nanoNick=nanoNick #NaNoNick
        self.nanoId=nanoId #Id aus dem NaNo, auch allgemeine Id
        self.romanTitel=romanTitel
        self.romanId=romanId
        

class PersonManager(object):
    person_ID=1
    def __init__(self,api):
        self.api=api
        self.persons={}
        self.personNick={}
    def insertPerson(self,person):
        self.persons[person.nanoId]=person
        self.personNick[person.nick]=person
    def addNew(self,forenNick,nanoNick):
        try:
            id=self.api.getId(nanoNick)
            
            self.insertPerson(Person(forenNick,nanoNick,id))
        except exceptions.AuthError as error:
            print(error)
        except exceptions.apiLoadingError as error:
            print(error)
    def addTest(self,forenNick,nanoNick,id):
        self.insertPerson(Person(forenNick, nanoNick, id))