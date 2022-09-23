from collections import UserDict
from gc import isenabled
import requests
import json
from json import JSONDecodeError
import sys
from LoginUI import Ui_Widget as LoginWidget
from PyQt5 import QtWidgets, QtCore
from AccountUI import Ui_Widget as AccountUI
from GenPassUI import Ui_Widget as GenPassUI
from NuclearUI import Ui_Widget as NukeUI
from SettingsUI import Ui_Widget as SettingsUI
from CreateAccountUI import Ui_Widget as CreateAccountUI
from NewStoreUI import Ui_Widget as NewStoreUI
from PassResetUI import Ui_Widget as PassResetUI
from PassResetSentUI import Ui_Widget as PassResetSentUI
from VerifyEmailUI import Ui_Widget as VerifyEmailUI
from DB_Functions import *
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

class PassResetWindow(QtWidgets.QMainWindow, PassResetUI):
     def __init__(self):
        super(PassResetWindow, self).__init__()
        self.setupUi(self)

class PassResetSentWindow(QtWidgets.QMainWindow, PassResetSentUI):
     def __init__(self):
        super(PassResetSentWindow, self).__init__()
        self.setupUi(self)

class VerifyEmailWindow(QtWidgets.QMainWindow, VerifyEmailUI):
     def __init__(self):
        super(VerifyEmailWindow, self).__init__()
        self.setupUi(self)

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.loginscreen = LoginWindow()
        self.password_reset_screen = PassResetWindow()
        self.password_reset_sent_screen = PassResetSentWindow()
        self.email_verify_screen = VerifyEmailWindow()
        self.loginscreen.show()
        self.loginscreen.LoginEnter.clicked.connect(self.Enter_clicked)
        self.loginscreen.CreateNewUser.clicked.connect(self.Create_Account_Clicked)
        self.loginscreen.PassReset.clicked.connect(self.PassReset_Clicked)
        self.password_reset_screen.pushButton.clicked.connect(self.SendReset_Clicked)
        self.UserInfo = firebase.database()
        self._userid = ""
        self.username = ""
        self.EmailVerified = False
        
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

    def errorWindow(self,errormessage, window):
        errordict = {"EMAIL_EXISTS":"This email is already in use",
                     "MISSING_PASSWORD":"Please enter a password",
                     "MISSING_FIRSTNAME": "Please enter a firstname",
                     "MISSING_LASTNAME": "Please enter a lastname",
                     "MISSING_USERNAME": "Please enter a username",
                     "INVALID_EMAIL": "Please ennter a valid email adress",
                     "MISSING_EMAIL": "Please enter an email adress",
                     "INVALID_PASSWORD": "Pleasse enter a valid password",
                     "EMAIL_NOT_FOUND": "Email was not found"}
        q = QtWidgets.QMessageBox()
        q.setWindowTitle("Error Occured")
        q.setText(errordict[errormessage])
        finish = q.exec_()

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
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            self.errorWindow(error, self.loginscreen)
            return
        userinfo = auth.get_account_info(user['idToken'])
        self.EmailVerified = userinfo['users'][0]['emailVerified']

        LoginVerified = True
        if LoginVerified and self.EmailVerified:

            userinf = auth.get_account_info(user['idToken'])
            self.userid = userinf['users'][0]['localId']
            self.username = self.UserInfo.child("users").get()
            
            for user in self.username.each():
                try:
                    if user.val()['userinfo']['UID'] == self.userid:
                        self.username = user.key()
                except (KeyError):
                    pass

            self.HomeScreen = AccountsWindow()
            accounts = self.UserInfo.child("users").child(self.username).child("Accounts").get()
            
            self.account_widgetsG = []
            self.account_widgetsV = []
            try:
                for account in accounts.each():
                    self.newG = QtWidgets.QPushButton(account.key())
                    self.newG.clicked.connect(lambda:self.accountPopup(account.val()))
                    self.newV = QtWidgets.QPushButton(account.key())
                    self.newV.clicked.connect(lambda:self.accountPopup(account.val()))
                    self.account_widgetsG.append(self.newG)
                    self.account_widgetsV.append(self.newV)
            except(TypeError): pass
            self.createAccountDisplay()
            
            if self.HomeScreen.AccountsGridV.isChecked(): 
                self.HomeScreen.AccountsHolder.show()
                self.HomeScreen.AccountsHolder.raise_()
            else: 
                self.HomeScreen.AccountsHolder2.show()
                self.HomeScreen.AccountsHolder2.raise_()
            self.loginscreen.hide()
            self.HomeScreen.show()
            self.genpass = GenPassWindow()
            self.settings = SettingsWindow()
            self.nukeopt = NukeWindow()
            self.AddStoreScreen = AddStoreWindow()
          
            self.HomeScreen.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.HomeScreen.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.HomeScreen.Nuke_Button.clicked.connect(self.Nuke_Clicked)
            self.HomeScreen.AccountsGridV.stateChanged.connect(self.gridChecked)
            self.HomeScreen.AccountVertV.stateChanged.connect(self.vertChecked)
            self.HomeScreen.commandLinkButton.clicked.connect(self.Add_Store_Clicked)

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
        else:
            self.email_verify_screen.show()


    def gridChecked(self):
        if self.HomeScreen.AccountsGridV.isChecked(): 
            self.HomeScreen.AccountVertV.setCheckState(False)
            self.HomeScreen.AccountsHolder2.hide()
            self.HomeScreen.AccountsHolder.show()


    
    def vertChecked(self):
        if self.HomeScreen.AccountVertV.isChecked(): 
            self.HomeScreen.AccountsGridV.setCheckState(False)
            self.HomeScreen.AccountsHolder.hide()
            self.HomeScreen.AccountsHolder2.show()

    def createAccountDisplay(self):
        
        newLayoutG = QtWidgets.QGridLayout()
        newLayoutV = QtWidgets.QVBoxLayout()
        rowcount = colcount = 0
        for item in self.account_widgetsG:
            if colcount <=3:
                newLayoutG.addWidget(item, rowcount, colcount)
                colcount += 1
            else:
                colcount = 0
                rowcount += 1
                newLayoutG.addWidget(item, rowcount, colcount)
                colcount += 1

        for item in self.account_widgetsV:
            newLayoutV.addWidget(item)
        
        self.HomeScreen.scrollAreaWidgetContents.setLayout(newLayoutG)
        self.HomeScreen.AccountsHolder.hide()
        self.HomeScreen.AccountsHolder.raise_()
        self.HomeScreen.scrollAreaWidgetContents_2.setLayout(newLayoutV)
        self.HomeScreen.AccountsHolder2.stackUnder(self.HomeScreen.AccountsHolder)
        self.HomeScreen.AccountsHolder2.hide()

    def Create_Account_Clicked(self):
        self.CreateAccountScreen = CreateAccountWindow()
        self.CreateAccountScreen.show()
        self.loginscreen.hide()
        self.CreateAccountScreen.CreationEnter.clicked.connect(self.Account_Created)
        
    def accountPopup(self, account):
        pass
    def Account_Created(self):
        self.username = self.CreateAccountScreen.NewUser.toPlainText()
        if self.username == "":
            self.errorWindow("MISSING_USERNAME", self.CreateAccountScreen)
            return
        password = self.CreateAccountScreen.NewPassword.toPlainText()
        firstname = self.CreateAccountScreen.FirstName.toPlainText()
        if firstname == "":
            self.errorWindow("MISSING_FIRSTNAME", self.CreateAccountScreen)
            return
        lastname = self.CreateAccountScreen.LastName.toPlainText()
        if lastname == "":
            self.errorWindow("MISSING_LASTNAME", self.CreateAccountScreen)
            return
        email = self.CreateAccountScreen.NewEmail.toPlainText()

        try:
            newuser = auth.create_user_with_email_and_password(email,password)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            self.errorWindow(error, self.CreateAccountScreen)
            return
        self.loginscreen.show()
        self.CreateAccountScreen.hide()

        userinf = auth.get_account_info(newuser['idToken'])
        userid = userinf['users'][0]['localId']

        verify_email(newuser['idToken'])
        
        
        
        
        


        data = {self._username: {"userinfo" : {"firstname" : firstname, "lastname": lastname, "email" : email, "UID": userid}}}
        try:
            self.UserInfo.child("users").update(data, newuser['idToken'])    
        except (JSONDecodeError):
            print("unsuccessful")

    def Generate_Password(self):
        if self.genpass.SaveGenPassSet.isChecked():
            data = {"loweronly": self.genpass.LowerPass.isChecked(), "Capatilization": self.genpass.CapPass.isChecked(), "Numerical": self.genpass.NumericPass.isChecked(), "SpecChar" : self.genpass.SpecCharPass.isChecked(), "CharLim" : int(self.genpass.PassCharLim.value())}
            self.UserInfo.child("users").child(self.username).child("PasswordSettings").update(data)
        self.genpass.GenPassOut.setPlainText(passwordGenerator(self.genpass.NumericPass.isChecked(), self.genpass.SpecCharPass.isChecked(), self.genpass.LowerPass.isChecked(), self.genpass.CapPass.isChecked(), self.genpass.PassCharLim.value()))

    def Add_Store_Clicked(self):
        self.AddStoreScreen.show()
        self.HomeScreen.hide()
        self.AddStoreScreen.pushButton.clicked.connect(self.Store_Added)

    def Store_Added(self):
        store = self.AddStoreScreen.textEdit.toPlainText()
        storeusername = self.AddStoreScreen.textEdit_2.toPlainText()
        storepassword = self.AddStoreScreen.textEdit_3.toPlainText()
        storeemail = self.AddStoreScreen.textEdit_4.toPlainText()
        data = {store:{"Email":storeemail, "Password" : storepassword, "Username" : storeusername}}
        self.UserInfo.child("users").child(self.username).child("Accounts").update(data)
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
    
    def PassReset_Clicked(self):
            self.password_reset_screen.show()


    def SendReset_Clicked(self):
        email = self.password_reset_screen.textEdit.toPlainText()
        try:
            reset_password(email)
            self.password_reset_sent_screen.show()
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            self.errorWindow(error, self.password_reset_screen)
            return

        
        
    
        
    
      
    

app = QtWidgets.QApplication(sys.argv)
ui = MyWindow()
sys.exit(app.exec_())

