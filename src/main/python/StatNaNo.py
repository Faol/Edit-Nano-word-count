#import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


from core import c_nanoAPI as nanoApi
from core.c_person import PersonManager
from uis.ui_main_window import Ui_MainWindow
from core.c_settings import settings
#--------------------------------
# bei Programmstart
#--------------------------------
personenManager=PersonManager(nanoApi.api)
personenManager.addTest("Faol","faol",1)
personenManager.addTest("Janika","winged_charly",2)


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.setupUi(self,personenManager)
        #gibt dem Fenster einen Titel



window = MainWindow()
window.show()


#--------------------------------
# test code
#--------------------------------


#personenManager.addNew("Faol","faol")
#personenManager.addNew("Janika","winged_charly")
#personenManager.addNew("Kraehe","kraehe")

#nanoApi.api.fileFromAPI("https://api.nanowrimo.org/projects/2005394","project_Jen")
#nanoApi.api.fileFromAPI("https://api.nanowrimo.org/project-challenges/1547715/project-sessions","project_kraehe")


#print(personenManager.persons)
#print(vars(personenManager.persons["669340"]))

print("Done")