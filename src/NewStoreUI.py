# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\TeamBlue_Porcupass\res\UI Forms\NewStoreForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(441, 455)
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(190, 330, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(190, 200, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(150, 170, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(170, 400, 101, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("border: 2px solid #405A7C;"
        "border-radius: 8px;" "background: #7FB4E9")
        self.textEdit_3 = QtWidgets.QTextEdit(Widget)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 350, 151, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(120, 50, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(200, 270, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(Widget)
        self.textEdit_4.setGeometry(QtCore.QRect(150, 290, 151, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Widget)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 230, 151, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(170, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit.setStyleSheet("border: 2px solid #405A7C;"
        "border-radius: 14px;" "background: #FFFFFF")
        self.textEdit_2.setStyleSheet("border: 2px solid #405A7C;"
        "border-radius: 14px;" "background: #FFFFFF")
        self.textEdit_3.setStyleSheet("border: 2px solid #405A7C;"
        "border-radius: 14px;" "background: #FFFFFF")
        self.textEdit_4.setStyleSheet("border: 2px solid #405A7C;"
        "border-radius: 14px;" "background: #FFFFFF")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label_4.setText(_translate("Widget", "Password"))
        self.label_3.setText(_translate("Widget", "Username"))
        self.pushButton.setText(_translate("Widget", "Create"))
        self.label.setText(_translate("Widget", "Add New Account"))
        self.label_5.setText(_translate("Widget", "Email"))
        self.label_2.setText(_translate("Widget", "Account Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    Widget.setStyleSheet("background: #C2ADAE")
    sys.exit(app.exec_())
