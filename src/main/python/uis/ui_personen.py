from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAction, QMenu, QPushButton, QHeaderView
from core import c_nanoAPI as nanoApi
from core.c_person import personenManager


class Ui_Personen(QTableWidget):
    def setupTable(self):
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Nano-Nick","Nano-ID","Roman-Id","Roman"])
        self.horizontalHeader().setStretchLastSection(True)
        self.setRowCount(1)
        if personenManager.activePerson:
            item=QTableWidgetItem(personenManager.activePerson.nanoNick)
            self.setItem(0, 0, item)
            item=QTableWidgetItem(personenManager.activePerson.nanoId)
            self.setItem(0, 1, item)
            if personenManager.activePerson.romanTitel:
                item = QTableWidgetItem(personenManager.activePerson.romanId)
                self.setItem(0, 2, item)
                item = QTableWidgetItem(personenManager.activePerson.romanTitel)
                self.setItem(0, 3, item)
            else:
                item = QTableWidgetItem()
                self.setItem(0, 2, item)
                loadRomanButton=QPushButton()
                loadRomanButton.setText("Roman laden")
                loadRomanButton.clicked.connect(lambda a,n=0: self.reloadRoman(n))
                self.setCellWidget(0, 3,loadRomanButton)
            self.setEditTriggers(QTableWidget.NoEditTriggers)
    def reloadTable(self):
        if personenManager.activePerson:
            item=QTableWidgetItem(personenManager.activePerson.nanoNick)
            self.setItem(0, 0, item)
            item=QTableWidgetItem(personenManager.activePerson.nanoId)
            self.setItem(0, 1, item)
            if personenManager.activePerson.romanTitel:
                item = QTableWidgetItem(str(personenManager.activePerson.romanId))
                self.setItem(0, 2, item)
                self.setCellWidget(0, 3, None)
                item = QTableWidgetItem(personenManager.activePerson.romanTitel)
                self.setItem(0, 3, item)
            else:
                item = QTableWidgetItem()
                self.setItem(0, 2, item)
                loadRomanButton=QPushButton()
                loadRomanButton.setText("Roman laden")
                loadRomanButton.clicked.connect(lambda a,n=0: self.reloadRoman(n))
                self.setCellWidget(0, 3,loadRomanButton)
            self.setEditTriggers(QTableWidget.NoEditTriggers)

    def contextMenuEvent(self, event):
        self.contextMenu = QMenu(self)
        reloadAction = QAction('Lade Roman', self)
        row=self.rowAt(event.pos().y())
        reloadAction.triggered.connect(lambda: self.reloadRoman(row))
        self.contextMenu.addAction(reloadAction)
        #removePersonAction = QAction("Person entfernen", self)
        #removePersonAction.triggered.connect(lambda: self.removePerson(row))
        #self.contextMenu.addAction(removePersonAction)
        self.contextMenu.popup(QCursor.pos())

    def removePerson(self,row):
        nick = self.item(row, 0).text()
        self.removeRow(row)
        #TODO: Person auch aus Personenmangager entfernen und löschen
        #Todo: Sicherheitsabfrage

    def reloadRoman(self, row):
        nanoNick=self.item(row,1).text()
        print("Lade Roman von: "+nanoNick)
        personenManager.activePerson.romanId,personenManager.activePerson.romanTitel,personenManager.activePerson.challengeId=(nanoApi.api.getRoman(personenManager.activePerson.nanoId))
        self.reloadTable()



        #todo:Roman laden Funktion schreiben
    def addPerson(self,person):
        i=self.rowCount()
        self.insertRow(i)
        self.setItem(i, 0, QTableWidgetItem(person.nick))
        self.setItem(i, 1, QTableWidgetItem(person.nanoNick))
        self.setItem(i, 2, QTableWidgetItem(person.romanTitel))
    def sizeHint(self):
        horizontal = self.horizontalHeader()
        vertical = self.verticalHeader()
        frame = self.frameWidth() * 2
        return QSize(horizontal.length() + vertical.width() + frame, vertical.length() + horizontal.height() + frame+40)