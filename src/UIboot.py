import sys
from LoginUI import Ui_Widget as LoginWidget
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Main_WindowUI import Ui_Widget as MainUI
from AccountsUI import Ui_Widget as AccountUI
from GenPassUI import Ui_Widget as GenPassUI
from NuclearUI import Ui_Widget as NukeUI
from SettingsUI import Ui_Widget as SettingsUI
from CreateAccountUI import Ui_Widget as CreateAccountUI
import pyrebase

# Your web app's Firebase configuration
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  'apiKey': "AIzaSyA1NFf0XKFE3ItD3M5LYMGv3FKbm2mQwSs",
  'authDomain': "porcupass-1d1cb.firebaseapp.com",
  'projectId': "porcupass-1d1cb",
  'storageBucket': "porcupass-1d1cb.appspot.com",
  'messagingSenderId': "798965436291",
  'appId': "1:798965436291:web:9b33dedac329461f3670b6",
  'measurementId': "G-SBBX0HG3XR",
  'databaseURL': ""
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class MainWindow(QtWidgets.QMainWindow, MainUI):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

class CreateAccountWindow(QtWidgets.QMainWindow, CreateAccountUI):
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        self.setupUi(self)

class AccountsWindow(QtWidgets.QMainWindow, AccountUI):
    def __init__(self):
        super(AccountsWindow, self).__init__()
        self.setupUi(self)

class GenPassWindow(QtWidgets.QMainWindow, GenPassUI):
    def __init__(self):
        super(GenPassWindow, self).__init__()
        self.setupUi(self)

    def Generate_Password(self):
        FakePassword = ''
        if self.NumericPass.isChecked():
            FakePassword += "numerical "
        if self.CapPass.isChecked():
            FakePassword += "capatilization "
        if self.SpecCharPass.isChecked():
            FakePassword += "special characters "
        FakePassword += "{} characters".format(self.PassCharLim.toPlainText())
        self.GenPassOut.setPlainText(FakePassword)

class NukeWindow(QtWidgets.QMainWindow, NukeUI):
    def __init__(self):
        super(NukeWindow, self).__init__()
        self.setupUi(self)

class LoginWindow(QtWidgets.QMainWindow, LoginWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

class SettingsWindow(QtWidgets.QMainWindow, SettingsUI):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.loginscreen = LoginWindow()
        self.loginscreen.show()
        self.loginscreen.LoginEnter.clicked.connect(self.Enter_clicked)
        self.loginscreen.CreateNewUser.clicked.connect(self.Create_Account_Clicked)
      
    def close_screens(self, current):
        if (self.HomeScreen != current and self.HomeScreen.isVisible()):
            self.HomeScreen.hide()
        elif (self.accounts != current and self.accounts.isVisible()):
            self.accounts.hide()
        elif (self.genpass != current and self.genpass.isVisible()):
            self.genpass.hide()
        elif (self.settings != current and self.settings.isVisible()):
            self.settings.hide()
        elif (self.nukeopt != current and self.nukeopt.isVisible()):
            self.nukeopt.hide()


    def Enter_clicked(self):
        email = self.loginscreen.LoginUser.toPlainText()
        password = self.loginscreen.LoginPassword.toPlainText()
        auth.create_user_with_email_and_password(email,password)
        LoginVerified = True
        if LoginVerified :
            self.HomeScreen = MainWindow()
            self.loginscreen.hide()
            self.HomeScreen.show()
            self.accounts = AccountsWindow()
            self.genpass = GenPassWindow()
            self.settings = SettingsWindow()
            self.nukeopt = NukeWindow()
            
            self.HomeScreen.Accounts_Button.clicked.connect(self.Accounts_Clicked)
            self.HomeScreen.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.HomeScreen.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.HomeScreen.Nuke_Button.clicked.connect(self.Nuke_Clicked)

            self.accounts.Home_Button.clicked.connect(self.Home_Clicked)
            self.accounts.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.accounts.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.accounts.Nuke_Button.clicked.connect(self.Nuke_Clicked)

            self.genpass.Home_Button.clicked.connect(self.Home_Clicked)
            self.genpass.Accounts_Button.clicked.connect(self.Accounts_Clicked)
            self.genpass.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.genpass.Nuke_Button.clicked.connect(self.Nuke_Clicked)
            self.genpass.GeneratePass.clicked.connect(self.genpass.Generate_Password)

            self.settings.Home_Button.clicked.connect(self.Home_Clicked)
            self.settings.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.settings.Accounts_Button.clicked.connect(self.Accounts_Clicked)
            self.settings.Nuke_Button.clicked.connect(self.Nuke_Clicked)

            self.nukeopt.Home_Button.clicked.connect(self.Home_Clicked)
            self.nukeopt.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.nukeopt.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.nukeopt.Accounts_Button.clicked.connect(self.Accounts_Clicked)
    
    def Create_Account_Clicked(self):
        self.CreateAccountScreen = CreateAccountWindow()
        self.CreateAccountScreen.show()
        self.loginscreen.hide()
        self.CreateAccountScreen.CreationEnter.clicked.connect(self.Account_Created)

    def Account_Created(self):
        self.loginscreen.show()
        self.CreateAccountScreen.hide()
            

    def Accounts_Clicked(self):
        self.close_screens(self.accounts)
        self.accounts.show()
        

    def Home_Clicked(self):
        self.close_screens(self.HomeScreen)
        self.HomeScreen.show()


    def Settings_Clicked(self):
        self.close_screens(self.settings)
        self.settings.show()
        
    
    def GenPass_Clicked(self):
        self.close_screens(self.genpass)
        self.genpass.show()

    def Nuke_Clicked(self):
        self.close_screens(self.nukeopt)
        self.nukeopt.show()

            

app = QtWidgets.QApplication(sys.argv)
ui = MyWindow()
sys.exit(app.exec_())

