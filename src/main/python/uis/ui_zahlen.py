from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAction, QMenu, QPushButton, QHeaderView
from core import c_nanoAPI as nanoApi


class Ui_Zahlen(QTableWidget):
    def setupTable(self,personenManager):
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Foren-Nick","Nano-Nick","Roman"])
        self.horizontalHeader().setStretchLastSection(True)
        self.setRowCount(len(personenManager.persons))
        i=0
        for key in personenManager.persons:
            self.setItem(i, 0, QTableWidgetItem(personenManager.persons[key].nick))
            self.setItem(i, 1, QTableWidgetItem(personenManager.persons[key].nanoNick))
            if personenManager.persons[key].romanTitel:
                self.setItem(i, 2, QTableWidgetItem(personenManager.persons[key].romanTitel))
            else:
                loadRomanButton=QPushButton()
                loadRomanButton.setText("Roman laden")
                loadRomanButton.clicked.connect(lambda a,n=i: self.reloadRoman(n))
                self.setCellWidget(i, 2,loadRomanButton)
            i+=1

    def contextMenuEvent(self, event):
        self.contextMenu = QMenu(self)
        reloadAction = QAction('Lade Roman', self)
        row=self.rowAt(event.pos().y())
        reloadAction.triggered.connect(lambda: self.reloadRoman(row))
        self.contextMenu.addAction(reloadAction)
        removePersonAction = QAction("Person entfernen", self)
        removePersonAction.triggered.connect(lambda: self.removePerson(row))
        self.contextMenu.addAction(removePersonAction)
        self.contextMenu.popup(QCursor.pos())

    def removePerson(self,row):
        nick = self.item(row, 0).text()
        self.removeRow(row)
        #TODO: Person auch aus Personenmangager entfernen und löschen
        #Todo: Sicherheitsabfrage

    def reloadRoman(self, row):
        nick=self.item(row,0).text()
        nanoNick=self.item(row,1).text()
        print("Lade Roman von: "+nick)
        print(nanoApi.api.getId(nanoNick))


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