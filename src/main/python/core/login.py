from PyQt5.QtWidgets import QDialog


from core.c_settings import settings
from uis import ui_login_dialog
from uis.ui_login_dialog import Ui_LoginDialog
from core import c_nanoAPI as nanoApi

class Login_dialog(QDialog, Ui_LoginDialog):
    def __init__(self,*args,**kwargs):
        super(Login_dialog,self).__init__(*args,**kwargs)
        self.setupUi(self)

def open_login_dialog(mainWindow):
    dlg=Login_dialog()
    if dlg.exec_():
        successful, msg, errorCode = nanoApi.api.sign_in(dlg.get_username(),dlg.get_password())
        settings.saveLogin=dlg.getSaveLoginState()
        if dlg.getSaveLoginState():
            settings.benutzername=dlg.get_username()
            settings.password=dlg.get_password()
        else:
            settings.benutzername =None
            settings.password =None
        settings.autoLogin=dlg.getAutoLoginState()
        settings.saveSettings()
        if successful:
            print(nanoApi.api.auth)
            mainWindow.reloadTab("PersonenTab")
            nanoApi.api.fileFromAPI("https://api.nanowrimo.org/users/917128/project-challenges", "project_challenges_faol2")
        else:
            if errorCode==1:
                Ui_LoginDialog.loginErrorMessageRetry(msg)
            else:
                Ui_LoginDialog.loginErrorMessage(msg)
    else:
        pass

def retry_login_dialog():
    open_login_dialog(True)

def logout(s):
    nanoApi.api.logout()
    print(nanoApi.api.auth)