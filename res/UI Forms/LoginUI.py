# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(472, 552)
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        Widget.setFont(font)
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(100, 30, 282, 511))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Logo = QtWidgets.QGraphicsView(self.widget)
        self.Logo.setObjectName("Logo")
        self.verticalLayout.addWidget(self.Logo)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.LoginUser = QtWidgets.QTextEdit(self.widget)
        self.LoginUser.setMaximumSize(QtCore.QSize(16777215, 35))
        self.LoginUser.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.LoginUser.setTabChangesFocus(True)
        self.LoginUser.setObjectName("LoginUser")
        self.verticalLayout.addWidget(self.LoginUser)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoginPassword = QtWidgets.QLineEdit(self.widget)
        self.LoginPassword.setMinimumSize(QtCore.QSize(0, 35))
        self.LoginPassword.setMaximumSize(QtCore.QSize(16777215, 35))
        self.LoginPassword.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.LoginPassword.setObjectName("LoginPassword")
        self.horizontalLayout.addWidget(self.LoginPassword)
        self.PasswordToggle = QtWidgets.QPushButton(self.widget)
        self.PasswordToggle.setMinimumSize(QtCore.QSize(0, 35))
        self.PasswordToggle.setStyleSheet("background-color: rgb(127, 180, 233);")
        self.PasswordToggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../eye_hidden.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../eye_visible.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PasswordToggle.setIcon(icon)
        self.PasswordToggle.setObjectName("PasswordToggle")
        self.horizontalLayout.addWidget(self.PasswordToggle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.PassReset = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setKerning(True)
        self.PassReset.setFont(font)
        self.PassReset.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(127, 180, 233);")
        self.PassReset.setCheckable(False)
        self.PassReset.setAutoDefault(True)
        self.PassReset.setDefault(True)
        self.PassReset.setFlat(False)
        self.PassReset.setObjectName("PassReset")
        self.verticalLayout.addWidget(self.PassReset)
        self.LoginEnter = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.LoginEnter.setFont(font)
        self.LoginEnter.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(127, 180, 233);")
        self.LoginEnter.setCheckable(False)
        self.LoginEnter.setAutoDefault(True)
        self.LoginEnter.setDefault(True)
        self.LoginEnter.setFlat(False)
        self.LoginEnter.setObjectName("LoginEnter")
        self.verticalLayout.addWidget(self.LoginEnter)
        self.CreateNewUser = QtWidgets.QCommandLinkButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setKerning(False)
        self.CreateNewUser.setFont(font)
        self.CreateNewUser.setIconSize(QtCore.QSize(0, 0))
        self.CreateNewUser.setCheckable(False)
        self.CreateNewUser.setObjectName("CreateNewUser")
        self.verticalLayout.addWidget(self.CreateNewUser)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        Widget.setTabOrder(self.LoginUser, self.LoginPassword)
        Widget.setTabOrder(self.LoginPassword, self.PassReset)
        Widget.setTabOrder(self.PassReset, self.LoginEnter)
        Widget.setTabOrder(self.LoginEnter, self.CreateNewUser)
        Widget.setTabOrder(self.CreateNewUser, self.Logo)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Email"))
        self.label_2.setText(_translate("Widget", "Password"))
        self.PassReset.setText(_translate("Widget", "Forgot Password?"))
        self.LoginEnter.setText(_translate("Widget", "Enter"))
        self.CreateNewUser.setText(_translate("Widget", "No account? Click here to create."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
