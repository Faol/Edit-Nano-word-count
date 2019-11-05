from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core import login
from uis import toolbars
import uis.actions as actions
from uis.toolbars import setupMainToolbar
from uis.ui_personen import Ui_Personen
from uis.ui_zahlen import Ui_Zahlen


class Ui_MainWindow(object):
    def setupUi(self, mainWindow,personenManager,appctxt):
        mainWindow.setObjectName("Main Window")

        # Body des Programmes im Moment nur ein Hallo World label
        #TODO Sinnvollen Body schreiben
        self.tabWidget =QTabWidget()
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.setCentralWidget(self.tabWidget)  # erzeugt Widget in der Mitte des Fensters. In diesem Fall das Label
        #Erstellt Personen-Tab
        self.personenTab = Ui_Personen(self)
        self.personenTab.setObjectName("PersonenTab")
        self.personenTab.setupTable()
        self.tabWidget.addTab(self.personenTab, "Infos")

        self.zahlenTab = Ui_Personen(self)
        self.zahlenTab.setupTable()
        self.tabWidget.addTab(self.zahlenTab, "Zahlen")

        mainActions=actions.MainActions(self,appctxt)
        # erstellt die Toolbar
        main_toolbar=setupMainToolbar(mainActions)
        self.addToolBar(main_toolbar)

        # erstellt Statusbar in einer Zeile, auch zweizeilig ware moeglich
        self.setStatusBar(QStatusBar(self))

        # erstellt ein menu
        menu = self.menuBar()

        #Hauptmenu
        main_menu = menu.addMenu("NaNoStatistics")
        main_menu.addAction(mainActions.login_action)
        main_menu.addAction(mainActions.logout_action)
        #main_menu.addSeparator()
        #TODO: submenu durch sinnvolles Menu ersetzen oder loeschen
        file_submenu = main_menu.addMenu("Submenu")
        #file_submenu.addAction(self.logout_action)

        self.retranslateUi(mainWindow)
    def reloadTab(self,tabname):
        self.findChild(QTableWidget, tabname).reloadTable()
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","NaNo Statistik"))