# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\TeamBlue_Porcupass\res\UI Forms\PassResetSent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(365, 181)
        self.sentLabel = QtWidgets.QLabel(Form)
        self.sentLabel.setGeometry(QtCore.QRect(50, 50, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.sentLabel.setFont(font)
        self.sentLabel.setObjectName("sentLabel")
        self.checkLabel = QtWidgets.QLabel(Form)
        self.checkLabel.setGeometry(QtCore.QRect(60, 90, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkLabel.setFont(font)
        self.checkLabel.setObjectName("checkLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sentLabel.setText(_translate("Form", "Your password email has been sent."))
        self.checkLabel.setText(_translate("Form", "Please check all folders, including spam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
