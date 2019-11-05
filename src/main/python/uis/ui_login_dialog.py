# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QDialogButtonBox, QCheckBox, QMessageBox

from core import login
from core.c_settings import settings


class Ui_LoginDialog(object):
    def setupUi(self, Dialog):
        # Einstellungen Dialogbox
        Dialog.setObjectName("Login-Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(366, 233)
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(True)
        #Einstellungen allgemeines Layout
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        #Beschreibender Text
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        #Benutzernamen Eingabefeld
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("username")
        if settings.saveLogin:
            self.lineEdit.setText(settings.benutzername)
        self.verticalLayout.addWidget(self.lineEdit)
        #Passwort-Eingabefeld
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setClearButtonEnabled(False)
        if settings.saveLogin:
            self.lineEdit_2.setText(settings.password)
        self.lineEdit_2.setObjectName("password")
        self.verticalLayout.addWidget(self.lineEdit_2)
        #Logindaten speichern Checkbox
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setChecked(settings.saveLogin)
        self.checkBox.setObjectName("saveLogin")
        self.verticalLayout.addWidget(self.checkBox)
        #Autologin checkbox
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setChecked(settings.autoLogin)
        self.checkBox_2.setObjectName("autoLogin")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        #Cancel und Login-Button
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Login-Dialog", "NaNo-Login"))
        self.label.setText(_translate("Login-Dialog", "Gibt hier deine NaNo-Login-Daten an."))
        self.lineEdit.setPlaceholderText(_translate("Login-Dialog", "NaNo-Benutzername"))
        self.lineEdit_2.setPlaceholderText(_translate("Login-Dialog", "NaNo-Password", "Password"))
        self.checkBox.setText(_translate("Login-Dialog", "Login Daten speichern"))
        self.checkBox_2.setText(_translate("Login-Dialog", "Beim nächsten öffnen einloggen"))
        self.buttonBox.button(QDialogButtonBox.Ok).setText(_translate("Login-Dialog", "Login"))
    def get_username(self):
        return self.findChild(QLineEdit, "username").text()
    def get_password(self):
        return self.findChild(QLineEdit, "password").text()
    def getSaveLoginState(self):
        return self.findChild(QCheckBox,"saveLogin").isChecked()
    def getAutoLoginState(self):
        return self.findChild(QCheckBox,"autoLogin").isChecked()

    @staticmethod
    def loginErrorMessageRetry(msg):
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Login Error")
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setEscapeButton(QMessageBox.Cancel)
        msgBox.accepted.connect(login.retry_login_dialog)
        msgBox.rejected.connect(lambda: None)
        msgBox.exec_()

    @staticmethod
    def loginErrorMessage(msg):
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Login Error")
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.setEscapeButton(QMessageBox.Ok)
        msgBox.accepted.connect(lambda: None)
        msgBox.exec_()
