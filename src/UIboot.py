from collections import UserDict
from gc import isenabled
from json import JSONDecodeError
import sys
from LoginUI import Ui_Widget as LoginWidget
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from AccountsUI import Ui_Widget as AccountUI
from GenPassUI import Ui_Widget as GenPassUI
from NuclearUI import Ui_Widget as NukeUI
from SettingsUI import Ui_Widget as SettingsUI
from CreateAccountUI import Ui_Widget as CreateAccountUI
from NewStoreUI import Ui_Widget as NewStoreUI
import pyrebase
from password_generation import *


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
  'databaseURL': "https://porcupass-1d1cb-default-rtdb.firebaseio.com"
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

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

class AddStoreWindow(QtWidgets.QMainWindow, NewStoreUI):
    def __init__(self):
        super(AddStoreWindow, self).__init__()
        self.setupUi(self)

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
        self.UserInfo = firebase.database()
        self._userid = ""
        self.username = ""
        
    @property
    def userid(self):
        return self._userid
    @userid.setter
    def userid(self, new):
        self._userid = new
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, new):
        self._username = new

    def close_screens(self, current):
        if (self.HomeScreen != current and self.HomeScreen.isVisible()):
            self.HomeScreen.hide()
        elif (self.genpass != current and self.genpass.isVisible()):
            self.genpass.hide()
        elif (self.settings != current and self.settings.isVisible()):
            self.settings.hide()
        elif (self.nukeopt != current and self.nukeopt.isVisible()):
            self.nukeopt.hide()


    def Enter_clicked(self):
        email = self.loginscreen.LoginUser.toPlainText()
        password = self.loginscreen.LoginPassword.toPlainText()
        user = auth.sign_in_with_email_and_password(email,password)
        LoginVerified = True
        if LoginVerified :
            self.HomeScreen = AccountsWindow()
            self.loginscreen.hide()
            self.HomeScreen.show()
            self.genpass = GenPassWindow()
            self.settings = SettingsWindow()
            self.nukeopt = NukeWindow()
            userinf = auth.get_account_info(user['idToken'])
            self.userid = userinf['users'][0]['localId']
            self.username = self.UserInfo.child("users").get()
            
            for user in self.username.each():
                try:
                    if user.val()['userinfo']['UID'] == self.userid:
                        self.username = user.key()
                except (KeyError):
                    pass

            
          
            self.HomeScreen.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.HomeScreen.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.HomeScreen.Nuke_Button.clicked.connect(self.Nuke_Clicked)

            self.genpass.Home_Button.clicked.connect(self.Home_Clicked)
            self.genpass.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.genpass.Nuke_Button.clicked.connect(self.Nuke_Clicked)
            self.genpass.GeneratePass.clicked.connect(self.Generate_Password)

            self.settings.Home_Button.clicked.connect(self.Home_Clicked)
            self.settings.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.settings.Nuke_Button.clicked.connect(self.Nuke_Clicked)

            self.nukeopt.Home_Button.clicked.connect(self.Home_Clicked)
            self.nukeopt.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.nukeopt.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.nukeopt.pushButton.clicked.connect(self.Nuke_Info)

    
    def Create_Account_Clicked(self):
        self.CreateAccountScreen = CreateAccountWindow()
        self.CreateAccountScreen.show()
        self.loginscreen.hide()
        self.CreateAccountScreen.CreationEnter.clicked.connect(self.Account_Created)
        

    def Account_Created(self):
        self.username = (self.CreateAccountScreen.NewUser.toPlainText())
        password = self.CreateAccountScreen.NewPassword.toPlainText()
        firstname = self.CreateAccountScreen.FirstName.toPlainText()
        lastname = self.CreateAccountScreen.LastName.toPlainText()
        email = self.CreateAccountScreen.NewEmail.toPlainText()

        newuser = auth.create_user_with_email_and_password(email,password)
        self.loginscreen.show()
        self.CreateAccountScreen.hide()

        userinf = auth.get_account_info(newuser['idToken'])
        userid = userinf['users'][0]['localId']
       

        data = {self._username: {"userinfo" : {"firstname" : firstname, "lastname": lastname, "email" : email, "UID": userid}}}
        try:
            self.UserInfo.child("users").update(data, newuser['idToken'])    
        except (JSONDecodeError):
            print("unsuccessful")

    def Generate_Password(self):
        if self.genpass.SaveGenPassSet.isChecked():
            data = {"Capatilization": self.genpass.CapPass.isChecked(), "Numerical": self.genpass.NumericPass.isChecked(), "SpecChar" : self.genpass.SpecCharPass.isChecked(), "CharLim" : int(self.genpass.PassCharLim.toPlainText())}
            self.UserInfo.child("users").child(self.username).child("PasswordSettings").update(data)
        self.genpass.GenPassOut.setPlainText(passwordGenerator(self.genpass.NumericPass.isChecked(), self.genpass.SpecCharPass.isChecked(), False, self.genpass.CapPass.isChecked(), self.genpass.PassCharLim.toPlainText()))

    def Add_Store_Clicked(self):
        self.AddStoreScreen = AddStoreWindow()
        self.AddStoreScreen.show()
        self.HomeScreen.hide()
        self.AddStoreScreen.pushButton.clicked.connect(self.Store_Added)

    def Store_Added(self):
        self.HomeScreen.show()
        self.AddStoreScreen.hide()

    def Add_Store_Enter_Clicked(self):
        self.addstorescreen.hide()
        self.HomeScreen.show()
        
    def Home_Clicked(self):
        self.close_screens(self.HomeScreen)
        self.HomeScreen.show()


    def Settings_Clicked(self):
        accountinfo = QtWidgets.QWidget()
        emailInfo = QtWidgets.QWidget()
        passwordInfo = QtWidgets.QWidget()
        nameInfo = QtWidgets.QWidget()
        self.settings.changeEmail = QtWidgets.QPushButton("Change Email")
        self.settings.changePassword = QtWidgets.QPushButton("Change Password")
        self.settings.changeName = QtWidgets.QPushButton("Change Name")
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(QtWidgets.QLabel("Email: {}"))
        hLayout.addWidget(self.settings.changeEmail)
        emailInfo.setLayout(hLayout)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(QtWidgets.QLabel("Password: {}"))
        hLayout.addWidget(self.settings.changePassword)
        passwordInfo.setLayout(hLayout)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(QtWidgets.QLabel("Name: {}"))
        hLayout.addWidget(self.settings.changeName)
        nameInfo.setLayout(hLayout)
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addWidget(emailInfo)
        vLayout.addWidget(passwordInfo)
        vLayout.addWidget(nameInfo)
        accountinfo.setLayout(vLayout)
        newItem = QtWidgets.QTreeWidgetItem()
        self.settings.SettingsTree.addTopLevelItem(newItem)
        self.settings.SettingsTree.setItemWidget(newItem,0,accountinfo)

        
        
        self.close_screens(self.settings)
        self.settings.show()
        
    
    def GenPass_Clicked(self):
        self.close_screens(self.genpass)
        self.genpass.show()

    def Nuke_Clicked(self):
        self.close_screens(self.nukeopt)
        self.nukeopt.show()
        
    
    def Nuke_Info(self):
        self.UserInfo.child("users").child(self.username).remove()
        auth.delete_user_account(auth.current_user['idToken'])
        
    
      
    


            

app = QtWidgets.QApplication(sys.argv)
ui = MyWindow()
sys.exit(app.exec_())

