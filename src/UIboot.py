
import base64
from collections import UserDict
from gc import isenabled
import math
import string
import requests
import json
from json import JSONDecodeError
import sys
from LoginUI import Ui_Widget as LoginWidget
from PyQt5 import QtWidgets, QtCore, sip, QtGui
from PyQt5.QtGui import QColor, QPolygon
from PyQt5.QtCore import pyqtSignal, QObject, QPoint
from AccountUI import Ui_Widget as AccountUI
from GenPassUI import Ui_Widget as GenPassUI
from NuclearUI import Ui_Widget as NukeUI
from PassResetUI import Ui_Widget as PassResetUI
from PassResetSentUI import Ui_Widget as PassResetSentUI
from VerifyEmailUI import Ui_Widget as VerifyEmailUI
from SettingsUI import Ui_Widget as SettingsUI
from CreateAccountUI import Ui_Widget as CreateAccountUI
from NewStoreUI import Ui_Widget as NewStoreUI
from AccountInfoUI import Ui_Widget as AccountDisplay
from password_generation import *
import DB_Functions as DB
from DB_Functions import *
import HIBPScraper as HIBP
from bruteForceTime import *
import pyperclip
from colour import Color
from datetime import date, datetime

class CreateAccountWindow(QtWidgets.QMainWindow, CreateAccountUI): 
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        self.setupUi(self)

class AccountsWindow(QtWidgets.QMainWindow, AccountUI):
    def __init__(self):
        super(AccountsWindow, self).__init__()
        self.setupUi(self)
        self.closeProtocol = Cleanup()
        self.moveProtocol = WidgetMoved()
        self.resizeProtocol = WidgetResized()
    
    def closeEvent(self, event):
        self.closeProtocol.signal.emit()
        event.accept()

    def resizeEvent(self, event):
        self.resizeProtocol.signal.emit()
        event.accept()

    def moveEvent(self, event):
        self.moveProtocol.signal.emit()
        event.accept()

    def getGeometry(self):
        return self.geometry()

class GenPassWindow(QtWidgets.QMainWindow, GenPassUI):
    def __init__(self):
        super(GenPassWindow, self).__init__()
        self.setupUi(self)
        self.closeProtocol = Cleanup()
        self.moveProtocol = WidgetMoved()
        self.resizeProtocol = WidgetResized()
    
    def closeEvent(self, event):
        self.closeProtocol.signal.emit()
        event.accept()

    def moveEvent(self, event):
        self.moveProtocol.signal.emit()
        event.accept()

    def resizeEvent(self, event):
        self.resizeProtocol.signal.emit()
        event.accept()

    def getGeometry(self):
        return self.geometry()

class AddStoreWindow(QtWidgets.QMainWindow, NewStoreUI):
    def __init__(self):
        super(AddStoreWindow, self).__init__()
        self.setupUi(self)

class NukeWindow(QtWidgets.QMainWindow, NukeUI):
    def __init__(self):
        super(NukeWindow, self).__init__()
        self.setupUi(self)
        self.closeProtocol = Cleanup()
        self.moveProtocol = WidgetMoved()
        self.resizeProtocol = WidgetResized()
    
    def closeEvent(self, event):
        self.closeProtocol.signal.emit()
        event.accept()

    def moveEvent(self, event):
        self.moveProtocol.signal.emit()
        event.accept()

    def resizeEvent(self, event):
        self.resizeProtocol.signal.emit()
        event.accept()

    def getGeometry(self):
        return self.geometry()

class LoginWindow(QtWidgets.QMainWindow, LoginWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

class SettingsWindow(QtWidgets.QMainWindow, SettingsUI):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)
        self.closeProtocol = Cleanup()
        self.moveProtocol = WidgetMoved()
        self.resizeProtocol = WidgetResized()
    
    def closeEvent(self, event):
        self.closeProtocol.signal.emit()

    def moveEvent(self, event):
        self.moveProtocol.signal.emit()
        event.accept()
    
    def resizeEvent(self, event):
        self.resizeProtocol.signal.emit()
        event.accept()

    def getGeometry(self):
        return self.geometry()

class AccountInfoWindow(QtWidgets.QMainWindow, AccountDisplay):
    def __init__(self, strength, status, age):
        super(AccountInfoWindow, self).__init__()
        self.setupUi(self)
        self.strength = strength
        self.status = status
        self.age = age
        
        
        self.Password_status_box.installEventFilter(self)
        self.password_strength_box.installEventFilter(self)
        self.password_age_box.installEventFilter(self)

        

    def eventFilter(self, obj, e):

        if (obj == self.Password_status_box  and e.type() == QtCore.QEvent.Paint):
            points = self.oct_coord()
            polygon = QPolygon(points)
            painter = QtGui.QPainter()
            painter.begin(obj)
            painter.setPen(QColor(0,0,0))
            painter.setBrush(QColor(self.status))
            painter.drawPolygon(polygon)
            painter.end()
            return super().eventFilter(obj, e)

        if (obj == self.password_strength_box  and e.type() == QtCore.QEvent.Paint):
            points = self.oct_coord()
            polygon = QPolygon(points)
            painter = QtGui.QPainter()
            painter.begin(obj)
            painter.setPen(QColor(0,0,0))
            painter.setBrush(QColor(self.strength))
            painter.drawPolygon(polygon)
            painter.end()
            return super().eventFilter(obj, e)

        if (obj == self.password_age_box  and e.type() == QtCore.QEvent.Paint):
            points = self.oct_coord()
            polygon = QPolygon(points)
            painter = QtGui.QPainter()
            painter.begin(obj)
            painter.setPen(QColor(0,0,0))
            painter.setBrush(QColor(self.age))
            painter.drawPolygon(polygon)
            painter.end()
            return super().eventFilter(obj, e)

        return super().eventFilter(obj, e)

    def oct_coord(self):
        height = self.password_strength_box.geometry().height() - 10
        width = self.password_strength_box.geometry().width() - 10
        r = min(height, width) / 2 
        height /= 2
        width /= 2
        points = [QPoint(int(width + r * math.cos(2 * math.pi * i/20)), int(height + r * math.sin(2 * math.pi * i/20))) for i in range(20)]
        return points

       
    

    def show_password(self, plain, obf):
        if self.label_6.text() == obf:
            self.label_6.setText(plain)
            self.repaint()
        elif self.label_6.text() == plain:
            self.label_6.setText(obf)
            self.repaint()

class Comm(QObject):
    accsignal = pyqtSignal()
    settsignal = pyqtSignal()

class Cleanup(QObject):
    signal = pyqtSignal()

class WidgetMoved(QObject):
    signal = pyqtSignal()

class WidgetResized(QObject):
    signal = pyqtSignal()


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
        self.loginscreen.PassReset.clicked.connect(self.PassReset_Clicked)
        self.password_reset_screen.sendresetButton.clicked.connect(self.SendReset_Clicked)
        self.EmailVerified = False
        self.loginscreen.show()
        self.loginscreen.setStyleSheet("background-color: #C2ADAE")
        #self.loginscreen.LoginUser.setStyleSheet("color: #FFFFFF")
        self.loginscreen.LoginEnter.clicked.connect(self.Enter_clicked)
        self.loginscreen.CreateNewUser.clicked.connect(self.Create_Account_Clicked)
        #self.UserInfo = firebase.database()
        self._userid = ""
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
    
        
    def accstream_handler(self, message):
        if message["event"] == "patch" or "delete":
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
                
    def window_concurrency(self, widget):
        window = widget.getGeometry()

        widgets = [self.HomeScreen, self.settings, self.genpass, self.nukeopt]
        
        for i in widgets:
            if i != widget:
                i.setGeometry(window)

            

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
        self.genpass.GenPassOut.clear()
        if (self.HomeScreen != current and self.HomeScreen.isVisible()):
            self.HomeScreen.hide()
        elif (self.genpass != current and self.genpass.isVisible()):
            self.genpass.hide()
        elif (self.settings != current and self.settings.isVisible()):
            self.settings.hide()
        elif (self.nukeopt != current and self.nukeopt.isVisible()):
            self.nukeopt.hide()
        elif (self.newacc != current and self.newacc.isVisible()):
            self.newacc.close()


    def Enter_clicked(self):
        #email = self.loginscreen.LoginUser.toPlainText()
        email = self.loginscreen.LoginUser.text()
        password = self.loginscreen.LoginPassword.text()
        try:
            self.user = DB.DB_Login(email, password)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            self.errorWindow(error, self.loginscreen)
            return
        
        self.userid, self.EmailVerified = DB.get_id_and_verify(self.user['idToken'])
        
        LoginVerified = True
        if LoginVerified and self.EmailVerified:

            self.stream = startStream(self.accstream_handler, self.settstream_handler, self.userid, self.user['idToken'])


            self.HomeScreen = AccountsWindow()
            self.HomeScreen.setStyleSheet("background: #6A4F50")
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
            self.loginscreen.LoginUser.clear()
            self.loginscreen.LoginPassword.clear()
            self.HomeScreen.show()
            self.genpass = GenPassWindow()
            self.settings = SettingsWindow()
            self.nukeopt = NukeWindow()
            self.AddStoreScreen = AddStoreWindow()

            self.AddStoreScreen.setStyleSheet("background: #C2ADAE")

            self.create_gradients()

          
            self.HomeScreen.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.HomeScreen.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.HomeScreen.Nuke_Button.clicked.connect(self.Nuke_Clicked)
            self.HomeScreen.AccountsGridV.stateChanged.connect(self.gridChecked)
            self.HomeScreen.AccountVertV.stateChanged.connect(self.vertChecked)
            self.HomeScreen.commandLinkButton.clicked.connect(self.Add_Store_Clicked)
            self.HomeScreen.moveProtocol.signal.connect(lambda:self.window_concurrency(self.HomeScreen))
            self.HomeScreen.resizeProtocol.signal.connect(lambda:self.window_concurrency(self.HomeScreen))

            self.genpass.Home_Button.clicked.connect(self.Home_Clicked)
            self.genpass.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.genpass.Nuke_Button.clicked.connect(self.Nuke_Clicked)
            self.genpass.GeneratePass.clicked.connect(self.Generate_Password)
            self.genpass.closeProtocol.signal.connect(self.close)
            self.genpass.moveProtocol.signal.connect(lambda:self.window_concurrency(self.genpass))
            self.genpass.resizeProtocol.signal.connect(lambda:self.window_concurrency(self.genpass))

            self.settings.Home_Button.clicked.connect(self.Home_Clicked)
            self.settings.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.settings.Nuke_Button.clicked.connect(self.Nuke_Clicked)
            self.settings.closeProtocol.signal.connect(self.close)
            self.settings.moveProtocol.signal.connect(lambda:self.window_concurrency(self.settings))
            self.settings.resizeProtocol.signal.connect(lambda:self.window_concurrency(self.settings))

            self.nukeopt.Home_Button.clicked.connect(self.Home_Clicked)
            self.nukeopt.GenPass_Button.clicked.connect(self.GenPass_Clicked)
            self.nukeopt.Settings_Button.clicked.connect(self.Settings_Clicked)
            self.nukeopt.NUKEBUTTON.clicked.connect(lambda:DB.nuke_info(self.user['idToken'], self.userid))
            self.nukeopt.closeProtocol.signal.connect(self.close)
            self.nukeopt.moveProtocol.signal.connect(lambda:self.window_concurrency(self.nukeopt))
            self.nukeopt.resizeProtocol.signal.connect(lambda:self.window_concurrency(self.nukeopt))

        else:
            self.email_verify_screen.show()

    def gridChecked(self):
        if self.HomeScreen.AccountsGridV.isChecked(): 
            self.HomeScreen.AccountVertV.setCheckState(False)
            self.HomeScreen.AccountsHolder2.hide()
            self.HomeScreen.AccountsHolder.show()

    def create_gradients(self):
        self.ageGradient = list(x.hex for x in list(Color("green").range_to(Color("red"), 5)))
        self.strengthGradient = list(x.hex for x in list(Color("red").range_to(Color("green"), 6)))
        self.hibpGradient = list(x.hex for x in list(Color("green").range_to(Color("red"), 4)))
    
    def vertChecked(self):
        if self.HomeScreen.AccountVertV.isChecked(): 
            self.HomeScreen.AccountsGridV.setCheckState(False)
            self.HomeScreen.AccountsHolder.hide()
            self.HomeScreen.AccountsHolder2.show()

    def createAccountDisplay(self):

        accounts = get_accounts(self.userid, self.user['idToken'])
        self.account_widgetsBG = QtWidgets.QButtonGroup()
        self.account_widgetsVG = QtWidgets.QButtonGroup()
        self.account_widgetsG = []
        self.account_widgetsV = []
        c = 0
        try:
            for account in accounts.each():
                newG = QtWidgets.QPushButton(account.key())
                newG.setStyleSheet("background: #7FB4E9")
                newV = QtWidgets.QPushButton(account.key(), objectName = account.key())
                newV.setStyleSheet("background: #7FB4E9")
                self.account_widgetsG.append(newG)
                self.account_widgetsV.append(newV)
                self.account_widgetsBG.addButton(newG, c)
                self.account_widgetsVG.addButton(newV, c)
                c+= 1
        except(TypeError): pass 

        self.account_widgetsBG.idClicked.connect(self.accountPopup)
        self.account_widgetsVG.idClicked.connect(self.accountPopup)

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
        self.CreateAccountScreen.setStyleSheet("background: #C2ADAE")
        self.loginscreen.hide()
        self.CreateAccountScreen.CreationEnter.clicked.connect(self.Account_Created)

    def hibpScore(self, hibp):
        if hibp == 0: score = 0
        elif hibp == 1: score = 1
        elif hibp < 5: score = 2
        else: score = 3
        return score

    def pStrength(self, password):
        strength = 0
        specialcharacters= set(string.punctuation)
        if any(x.isupper() for x in password): strength += 1
        if any(x.islower() for x in password): strength += 1
        if any(x.isdigit() for x in password): strength += 1
        if any(x in specialcharacters for x in password): strength += 1
        if len(password) < 5: strength -= 2
        if len(password) > 15: strength += 1

        if strength < 0: strength = 0

        return strength


    def time_from(self, thenstring):
        now = datetime.now()
        then = datetime.strptime(thenstring, "%y %m %d")
        age = now - then
        return age

    def age_score(self, age):
        years = math.floor(age.days / 365)
        months = (age.days - (years*365)) / 30

        if years >= 2: return 4
        elif years == 1:
            if months > 6: return 3
            else: return 2
        else:
            if months > 6 : return 1
            else: return 0

    def updatePassword(self, name):
        text, ok = QtWidgets.QInputDialog().getText(self, "Update Password", "New Password:", QtWidgets.QLineEdit.Normal)
        if ok and text:
            now = date.today().strftime("%y %m %d")
            update_password(self.userid, name, self.user['idToken'], text, now)
            q = QtWidgets.QMessageBox()
            q.setWindowTitle("Password Changed")
            q.setText("Window closing, please reopen to see reflected changes.")
            finish = q.exec_()
            self.newacc.close()
            self.HomeScreen.show()
        else: return

    def delete_Store(self, account):
        q = QtWidgets.QMessageBox()
        q.setWindowTitle("Delete Account")
        q.setText("Are you sure you want to delete this account? Deleted accounts cannot be recovered.")
        q.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        finish = q.exec_()
        if finish == QtWidgets.QMessageBox.Ok:
            delete_store(self.userid, account, self.user['idToken'])
            self.newacc.close()
            self.HomeScreen.show()
        else : return
        
    def accountPopup(self, id):
        name = self.account_widgetsBG.button(id).text()
     
        newaccinfo = get_new_account(name, self.userid, self.user['idToken'])
       
        email= newaccinfo.val()['Email']
        username = newaccinfo.val()['Username']
        creation_date = newaccinfo.val()['Created_On']
        password = decrypt_password(self.userid, name, self.user['idToken'])
        decrypt_cleanup(self.userid, name, self.user['idToken'])
        age = self.time_from(creation_date)
        agescore = self.age_score(age)
        hiddenPassword = "\u2022" * len(password)
        self.HIBPS = int(HIBP.HIBP(password))
        self.bftime = BFtime(password)
        status = self.hibpScore(self.HIBPS)
        strength = self.pStrength(password)
        years = math.floor(age.days/365)
        months = math.floor((age.days - years * 365)/30)

        if(strength == 0): self.newacc = AccountInfoWindow(self.strengthGradient[strength], self.hibpGradient[status], self.ageGradient[agescore])
        else: self.newacc = AccountInfoWindow(self.strengthGradient[strength-1], self.hibpGradient[status], self.ageGradient[agescore])
       
        
        self.newacc.setCentralWidget(self.newacc.widget)
           
        self.newacc.time_to_crack.setText(self.bftime)
        self.newacc.Password_status_box.setText("Password Breaches:\n{}".format(self.HIBPS))
        self.newacc.password_strength_box.setText("Strength Score:\n{}/5".format(strength))
        self.newacc.password_age_box.setText("Password Age:\n {} years, {} months".format(years, months))
        self.newacc.Password_status_box.setAlignment(QtCore.Qt.AlignCenter)
        self.newacc.password_strength_box.setAlignment(QtCore.Qt.AlignCenter)

        self.newacc.StoreName.setText(name)
        self.newacc.label_4.setText(email)
        self.newacc.label_5.setText(username)
        self.newacc.label_6.setText(hiddenPassword)
        self.newacc.showPassword.clicked.connect(lambda:self.newacc.show_password(password, hiddenPassword))
        self.newacc.copyPassword.clicked.connect(lambda:pyperclip.copy(password))
        self.newacc.copyUsername.clicked.connect(lambda:pyperclip.copy(username))
        self.newacc.update_password.clicked.connect(lambda:self.updatePassword(name))
        self.newacc.storeDelete.clicked.connect(lambda:self.delete_Store(name))
        self.newacc.password_strength_box.repaint()
        self.newacc.Password_status_box.repaint()
        self.newacc.password_strength_box.show()
        self.newacc.Password_status_box.show()
        self.newacc.show()
        self.HomeScreen.hide()
        self.newacc.pushButton.clicked.connect(self.Home_Clicked)
       

    
       

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

        self.userid, self.EmailVerified = DB.get_id_and_verify(newuser['idToken'])
        
       
        hasKey = False
        data = {self.userid: {"userinfo" : {"firstname" : firstname, "lastname": lastname, "email" : email, 'hasKey' : hasKey}}}
        try:
            DB.update_user_info(data, newuser['idToken'])    
        except (JSONDecodeError):
            print("unsuccessful")

        verify_email(newuser["idToken"])

    def Generate_Password(self):
        if self.genpass.SaveGenPassSet.isChecked():
            data = {"loweronly": self.genpass.LowerPass.isChecked(), "Capatilization": self.genpass.CapPass.isChecked(), "Numerical": self.genpass.NumericPass.isChecked(), "SpecChar" : self.genpass.SpecCharPass.isChecked(), "CharLim" : int(self.genpass.PassCharLim.value())}
            DB.save_password_settings(data, self.userid, self.user['idToken'])
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
        today = date.today()
        creation_date = today.strftime("%y %m %d")
        isEncrypted = False
        data = {store:{"Email":storeemail, "Password" : storepassword, "Username" : storeusername, 'Created_On': creation_date, 'isEncrypted' : isEncrypted}}
        DB.add_store(data, self.user['idToken'], self.userid)
        self.HomeScreen.show()
        self.AddStoreScreen.hide() 
        self.AddStoreScreen.textEdit.clear()
        self.AddStoreScreen.textEdit_2.clear()
        self.AddStoreScreen.textEdit_3.clear()
        self.AddStoreScreen.textEdit_4.clear()


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
        self.genpass.setStyleSheet("background: #C2ADAE")

    def Nuke_Clicked(self):
        self.close_screens(self.nukeopt)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\fullw\source\repos\TeamBluePorcupass\res\NukeImage.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nukeopt.NUKEBUTTON.setIcon(icon)
        self.nukeopt.NUKEBUTTON.setIconSize(QtCore.QSize(231, 171))
        self.nukeopt.NUKEBUTTON.setAutoDefault(True)
        self.nukeopt.NUKEBUTTON.setDefault(True)
        self.nukeopt.NUKEBUTTON.setFlat(False)
        self.nukeopt.NUKEBUTTON.setObjectName("pushButton")
        self.nukeopt.show()
        
    
    def PassReset_Clicked(self):
            self.password_reset_screen.show()
            self.password_reset_screen.setStyleSheet("background: #C2ADAE")


    def SendReset_Clicked(self):
        email = self.password_reset_screen.ResetEmail.toPlainText()
        try:
            reset_password(email)
            self.password_reset_sent_screen.show()
            self.password_reset_screen.setStyleSheet("background: #C2ADAE")
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            self.errorWindow(error, self.password_reset_screen)
            return


app = QtWidgets.QApplication(sys.argv)
ui = MyWindow()
sys.exit(app.exec_())

