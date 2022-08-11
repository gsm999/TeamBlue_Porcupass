# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenPassForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.Menu = QtWidgets.QToolBox(Widget)
        self.Menu.setGeometry(QtCore.QRect(30, 20, 85, 181))
        self.Menu.setLineWidth(1)
        self.Menu.setObjectName("Menu")
        self.Dropdown = QtWidgets.QWidget()
        self.Dropdown.setGeometry(QtCore.QRect(0, 0, 85, 125))
        self.Dropdown.setObjectName("Dropdown")
        self.Home_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Home_Button.setGeometry(QtCore.QRect(0, 0, 85, 31))
        self.Home_Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Home_Button.setObjectName("Home_Button")
        self.Settings_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Settings_Button.setGeometry(QtCore.QRect(0, 30, 85, 29))
        self.Settings_Button.setObjectName("Settings_Button")
        self.Nuke_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Nuke_Button.setGeometry(QtCore.QRect(0, 60, 85, 41))
        self.Nuke_Button.setObjectName("Nuke_Button")
        self.Menu.addItem(self.Dropdown, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 125))
        self.page.setObjectName("page")
        self.Menu.addItem(self.page, "")
        self.GenPassOut = QtWidgets.QTextBrowser(Widget)
        self.GenPassOut.setGeometry(QtCore.QRect(150, 190, 401, 51))
        self.GenPassOut.setObjectName("GenPassOut")
        self.GeneratePass = QtWidgets.QPushButton(Widget)
        self.GeneratePass.setGeometry(QtCore.QRect(550, 190, 93, 51))
        self.GeneratePass.setObjectName("GeneratePass")
        self.NumericPass = QtWidgets.QCheckBox(Widget)
        self.NumericPass.setGeometry(QtCore.QRect(110, 330, 91, 24))
        self.NumericPass.setObjectName("NumericPass")
        self.CapPass = QtWidgets.QCheckBox(Widget)
        self.CapPass.setGeometry(QtCore.QRect(110, 380, 121, 24))
        self.CapPass.setObjectName("CapPass")
        self.SpecCharPass = QtWidgets.QCheckBox(Widget)
        self.SpecCharPass.setGeometry(QtCore.QRect(110, 430, 151, 24))
        self.SpecCharPass.setObjectName("SpecCharPass")
        self.PassCharLim = QtWidgets.QTextEdit(Widget)
        self.PassCharLim.setGeometry(QtCore.QRect(530, 320, 51, 31))
        self.PassCharLim.setObjectName("PassCharLim")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(590, 330, 111, 20))
        self.label.setObjectName("label")
        self.SaveGenPassSet = QtWidgets.QCheckBox(Widget)
        self.SaveGenPassSet.setGeometry(QtCore.QRect(530, 430, 161, 24))
        self.SaveGenPassSet.setObjectName("SaveGenPassSet")

        self.retranslateUi(Widget)
        self.Menu.setCurrentIndex(1)
        self.Menu.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.Home_Button.setText(_translate("Widget", "Home"))
        self.Settings_Button.setText(_translate("Widget", "Settings"))
        self.Nuke_Button.setText(_translate("Widget", "Nuclear \n"
"Option"))
        self.Menu.setItemText(self.Menu.indexOf(self.Dropdown), _translate("Widget", "Menu"))
        self.Menu.setItemText(self.Menu.indexOf(self.page), _translate("Widget", "Close"))
        self.GeneratePass.setText(_translate("Widget", "PushButton"))
        self.NumericPass.setText(_translate("Widget", "Numbers"))
        self.CapPass.setText(_translate("Widget", "Capatilization"))
        self.SpecCharPass.setText(_translate("Widget", "Special Characters"))
        self.label.setText(_translate("Widget", "Character Limit"))
        self.SaveGenPassSet.setText(_translate("Widget", "Save these settings?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

