# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\TeamBlue_Porcupass\res\UI Forms\PassReset.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(375, 178)
        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setGeometry(QtCore.QRect(90, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(21)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.emailLabel = QtWidgets.QLabel(Form)
        self.emailLabel.setGeometry(QtCore.QRect(160, 70, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.ResetEmail = QtWidgets.QTextEdit(Form)
        self.ResetEmail.setGeometry(QtCore.QRect(70, 100, 231, 31))
        self.ResetEmail.setObjectName("ResetEmail")
        self.sendresetButton = QtWidgets.QPushButton(Form)
        self.sendresetButton.setGeometry(QtCore.QRect(130, 140, 101, 23))
        self.sendresetButton.setObjectName("sendresetButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titleLabel.setText(_translate("Form", "Password Reset"))
        self.emailLabel.setText(_translate("Form", "Email"))
        self.sendresetButton.setText(_translate("Form", "Send Reset Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())