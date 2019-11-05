from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
import sys

from core import c_nanoAPI as nanoApi
from core.c_person import PersonManager
from uis.ui_main_window import Ui_MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    # --------------------------------
    # bei Programmstart
    # --------------------------------
    personenManager = PersonManager(nanoApi.api)
    personenManager.addTest("Faol", "faol", 1)
    personenManager.addTest("Janika", "winged_charly", 2)


    class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            self.setupUi(self, personenManager,appctxt)
            # gibt dem Fenster einen Titel


    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)