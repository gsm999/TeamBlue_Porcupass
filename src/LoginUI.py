# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\TeamBlue_Porcupass\res\UI Forms\LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
script_dir = os.path.dirname(__file__) 
res_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'res'))

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(472, 552)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setKerning(True)
        Widget.setFont(font)
        self.LoginUser = QtWidgets.QTextEdit(Widget)
        self.LoginUser.setGeometry(QtCore.QRect(103, 286, 251, 31))
        self.LoginUser.setObjectName("LoginUser")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(200, 260, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(210, 340, 71, 20))
        self.label_2.setObjectName("label_2")
        self.LoginEnter = QtWidgets.QPushButton(Widget)
        self.LoginEnter.setGeometry(QtCore.QRect(190, 430, 93, 29))
        self.LoginEnter.setCheckable(False)
        self.LoginEnter.setAutoDefault(True)
        self.LoginEnter.setDefault(True)
        self.LoginEnter.setFlat(False)
        self.LoginEnter.setObjectName("LoginEnter")
        self.CreateNewUser = QtWidgets.QCommandLinkButton(Widget)
        self.CreateNewUser.setGeometry(QtCore.QRect(120, 470, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setItalic(True)
        font.setKerning(False)
        self.CreateNewUser.setFont(font)
        self.CreateNewUser.setIconSize(QtCore.QSize(0, 0))
        self.CreateNewUser.setCheckable(False)
        self.CreateNewUser.setObjectName("CreateNewUser")
        self.PassReset = QtWidgets.QPushButton(Widget)
        self.PassReset.setGeometry(QtCore.QRect(180, 400, 111, 21))
        self.PassReset.setCheckable(False)
        self.PassReset.setAutoDefault(True)
        self.PassReset.setDefault(True)
        self.PassReset.setFlat(False)
        self.PassReset.setObjectName("PassReset")
        self.LoginPassword = QtWidgets.QLineEdit(Widget)
        self.LoginPassword.setGeometry(QtCore.QRect(100, 360, 251, 31))
        self.LoginPassword.setObjectName("LoginPassword")
        self.LoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordToggle = QtWidgets.QPushButton(Widget)
        self.PasswordToggle.setGeometry(QtCore.QRect(320, 360, 31, 31))
        self.PasswordToggle.setFlat(True)
        self.PasswordToggle.setText("")
        self.PasswordToggle.setIcon(QtGui.QIcon(res_dir + "/eye_visible.svg"))
        self.PasswordToggle.setObjectName("PasswordToggle")
        self.PasswordToggle.clicked.connect(self.toggleVisibility)
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Username:"))
        self.label_2.setText(_translate("Widget", "Password"))
        self.LoginEnter.setText(_translate("Widget", "Enter"))
        self.CreateNewUser.setText(_translate("Widget", "No account? Click here to create."))
        self.PassReset.setText(_translate("Widget", "Forgot Password?"))
    
    def toggleVisibility(self):
        if self.LoginPassword.echoMode()==QtWidgets.QLineEdit.Normal:
            self.LoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            self.PasswordToggle.setIcon(QtGui.QIcon(res_dir + "/eye_visible.svg"))
        else:
            self.LoginPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.PasswordToggle.setIcon(QtGui.QIcon(res_dir + "/eye_hidden.svg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
