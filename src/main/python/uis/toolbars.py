from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def setupMainToolbar(mainActions):
    toolbar=QToolBar("Main Toolbar")
    toolbar.setObjectName("Main Toolbar")
    toolbar.setIconSize(QSize(16, 16))  # groeße der Icons in der Toolbar muss festgelegt werden
    toolbar.addAction(mainActions.login_action)
    toolbar.addAction(mainActions.logout_action)
    return toolbar