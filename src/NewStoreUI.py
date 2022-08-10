# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewStoreForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(340, 310, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(330, 180, 111, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(330, 140, 111, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(340, 380, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(Widget)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 330, 111, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(350, 80, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(360, 250, 41, 21))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(Widget)
        self.textEdit_4.setGeometry(QtCore.QRect(330, 270, 111, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Widget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 210, 111, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(350, 120, 81, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label_4.setText(_translate("Widget", "Store Password"))
        self.label_3.setText(_translate("Widget", "Store Username"))
        self.pushButton.setText(_translate("Widget", "Enter"))
        self.label.setText(_translate("Widget", "Add Store"))
        self.label_5.setText(_translate("Widget", "Email"))
        self.label_2.setText(_translate("Widget", "Store Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

