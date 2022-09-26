
from collections import UserDict
from gc import isenabled
import requests
import json
from json import JSONDecodeError
import sys
from LoginUI import Ui_Widget as LoginWidget
from PyQt5 import QtWidgets, QtCore, sip
from PyQt5.QtCore import pyqtSignal, QObject
from AccountUI import Ui_Widget as AccountUI
from GenPassUI import Ui_Widget as GenPassUI
from NuclearUI import Ui_Widget as NukeUI
from PassResetUI import Ui_Widget as PassResetUI
from PassResetSentUI import Ui_Widget as PassResetSentUI
from VerifyEmailUI import Ui_Widget as VerifyEmailUI
from SettingsUI import Ui_Widget as SettingsUI
from CreateAccountUI import Ui_Widget as CreateAccountUI
from NewStoreUI import Ui_Widget as NewStoreUI
from password_generation import *
import DB_Functions as DB
from DB_Functions import *


class CreateAccountWindow(QtWidgets.QMainWindow, CreateAccountUI): 
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        self.setupUi(self)

class AccountsWindow(QtWidgets.QMainWindow, AccountUI):
    def __init__(self):
        super(AccountsWindow, self).__init__()
        self.setupUi(self)
        self.closeProtocol = Cleanup()
    
    def closeEvent(self, event):
        self.closeProtocol.signal.emit()

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

class Comm(QObject):
    accsignal = pyqtSignal()
    settsignal = pyqtSignal()

class Cleanup(QObject):
    signal = pyqtSignal()

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.loginscreen = LoginWindow()
        self.loginscreen.show()
        self.loginscreen.LoginEnter.clicked.connect(self.Enter_clicked)
        self.loginscreen.CreateNewUser.clicked.connect(self.Create_Account_Clicked)
        #self.UserInfo = firebase.database()
        self._userid = ""
        self._username = ""
        self.newLayoutV = QtWidgets.QVBoxLayout()
        self.newLayoutG = QtWidgets.QHBoxLayout()
        self.mainLayoutV = QtWidgets.QVBoxLayout()
        self.mainLayoutG = QtWidgets.QHBoxLayout()
       
    def closeEvent(self, event):
        self.stream.close_streams()
        self.genpass.close()
        self.settings.close()
        self.nukeopt.close()
        event.accept()   


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
    
        
    def accstream_handler(self, message):
        if message["event"] == "patch":
            newaccount = list(message["data"].keys())[0]
            print(newaccount)
            self.account_widgetsG = self.account_widgetsV = []
            newg = QtWidgets.QPushButton(newaccount)
            newv = QtWidgets.QPushButton(newaccount)
            newv.clicked.connect(lambda:self.accountPopup(newaccount.val()))
            newg.clicked.connect(lambda:self.accountPopup(newaccount.val()))
            self.account_widgetsG.append(newg)
            self.account_widgetsV.append(newv)

            
            accounts = DB.get_accounts(self.username)
            try:
                for account in accounts.each():
                    self.newG = QtWidgets.QPushButton(account.key())
                    self.newG.clicked.connect(lambda:self.accountPopup(account.val()))
                    self.newV = QtWidgets.QPushButton(account.key())
                    self.newV.clicked.connect(lambda:self.accountPopup(account.val()))
                    self.account_widgetsG.append(self.newG)
                    self.account_widgetsV.append(self.newV)
            except(TypeError): pass

            self.guiupdate.accsignal.emit()

    
    def clearLayout(self, layout):
         if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        self.clearLayout(item.layout())
                
        

    def settstream_handler(self, message):
        pass
    def errorWindow(self,errormessage, window):
        errordict = {"EMAIL_EXISTS":"This email is already in use",
                     "MISSING_PASSWORD":"Please enter a password",
                     "MISSING_FIRSTNAME": "Please enter a firstname",
                     "MISSING_LASTNAME": "Please enter a lastname",
                     "MISSING_USERNAME": "Please enter a username",
                     "INVALID_EMAIL": "Please ennter a valid email adress",
                     "MISSING_EMAIL": "Please enter an email adress",
                     "INVALID_PASSWORD": "Pleasse enter a valid password",
                     "EMAIL_NOT_FOUND": "Email was not found",
                     "WEAK_PASSWORD : Password should be at least 6 characters": "Password must be at leat 6 characters"}
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
            self.user = DB.DB_Login(email, password)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            self.errorWindow(error, self.loginscreen)
            return
                
        LoginVerified = True
        if LoginVerified :

            self.userid, self.username = DB.get_id_and_username(self.user['idToken'])

            self.stream = startStream(self.accstream_handler, self.settstream_handler, self.username)


            self.HomeScreen = AccountsWindow()
            self.HomeScreen.closeProtocol.signal.connect(self.close)

            self.guiupdate = Comm()
            self.guiupdate.accsignal.connect(self.createAccountDisplay)

            self.createAccountDisplay()

            self.HomeScreen.scrollAreaWidgetContents.setLayout(self.mainLayoutG)
            self.HomeScreen.AccountsHolder.hide()
            self.HomeScreen.AccountsHolder.raise_()
            self.HomeScreen.scrollAreaWidgetContents_2.setLayout(self.mainLayoutV)
            self.HomeScreen.AccountsHolder2.stackUnder(self.HomeScreen.AccountsHolder)
            self.HomeScreen.AccountsHolder2.hide()

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
            self.nukeopt.pushButton.clicked.connect(lambda:DB.nuke_info(self.user['idToken'], self.username))


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

        accounts = get_accounts(self.username)
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

        self.clearLayout(self.newLayoutG)
        self.clearLayout(self.newLayoutV)
        
        self.clearLayout(self.mainLayoutG)
        self.clearLayout(self.mainLayoutV)

        

        self.newLayoutG = QtWidgets.QGridLayout()
        self.newLayoutV = QtWidgets.QVBoxLayout()
        rowcount = colcount = 0
        for item in self.account_widgetsG:
            if colcount <=3:
                self.newLayoutG.addWidget(item, rowcount, colcount)
                colcount += 1
            else:
                colcount = 0
                rowcount += 1
                self.newLayoutG.addWidget(item, rowcount, colcount)
                colcount += 1

        for item in self.account_widgetsV:
            self.newLayoutV.addWidget(item)

        self.mainLayoutG.insertLayout(0,self.newLayoutG)
        self.mainLayoutV.insertLayout(0,self.newLayoutV)

    def Create_Account_Clicked(self):
        self.CreateAccountScreen = CreateAccountWindow()
        self.CreateAccountScreen.show()
        self.loginscreen.hide()
        self.CreateAccountScreen.CreationEnter.clicked.connect(self.Account_Created)
        
    def accountPopup(self, account):
        pass

    def Account_Created(self):
        newusername = self.CreateAccountScreen.NewUser.toPlainText()
        if newusername == "":
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
            newuser = DB.create_new_user(email,password)
        except (requests.HTTPError, KeyError) as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            self.errorWindow(error, self.CreateAccountScreen)
            return
        self.loginscreen.show()
        self.CreateAccountScreen.hide()

        self.userid, self.username = DB.get_id_and_username(newuser['idToken'])
        
       

        data = {newusername: {"userinfo" : {"firstname" : firstname, "lastname": lastname, "email" : email, "UID": self.userid}}}
        try:
            DB.update_user_info(data, newuser['idToken'])    
        except (JSONDecodeError):
            print("unsuccessful")

        verify_email(newuser["idToken"])

    def Generate_Password(self):
        if self.genpass.SaveGenPassSet.isChecked():
            data = {"loweronly": self.genpass.LowerPass.isChecked(), "Capatilization": self.genpass.CapPass.isChecked(), "Numerical": self.genpass.NumericPass.isChecked(), "SpecChar" : self.genpass.SpecCharPass.isChecked(), "CharLim" : int(self.genpass.PassCharLim.value())}
            DB.save_password_settings(data, self.username, self.user['idToken'])
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
        DB.add_store(data, self.user['idToken'], self.username)
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

