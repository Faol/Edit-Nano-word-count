from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from core import login


class MainActions(object):
    def __init__(self,mainWindow,appctxt):
        # Login Aktion
        self.login_action = QAction(QIcon(appctxt.get_resource('Symbols/lock-unlock.png')), "Login", mainWindow)
        self.login_action.setCheckable(False)
        self.login_action.triggered.connect(lambda: login.open_login_dialog(mainWindow))
        self.login_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))

        self.logout_action = QAction(QIcon(appctxt.get_resource('Symbols/lock.png')), "Logout", mainWindow)
        self.logout_action.setCheckable(False)
        self.logout_action.triggered.connect(login.logout)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.login_action.setStatusTip(_translate("MainActions","In Nano Seite einloggen."))
        self.login_action.setText(_translate("MainActions","Login"))
        self.logout_action.setStatusTip(_translate("MainActions","Aus Nano Seite ausloggen."))
        self.logout_action.setText(_translate("MainActions", "Logout"))