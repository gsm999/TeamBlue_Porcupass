# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountPageForm.ui'
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
        self.Menu.setGeometry(QtCore.QRect(20, 10, 85, 181))
        self.Menu.setLineWidth(1)
        self.Menu.setObjectName("Menu")
        self.Dropdown = QtWidgets.QWidget()
        self.Dropdown.setGeometry(QtCore.QRect(0, 0, 85, 125))
        self.Dropdown.setObjectName("Dropdown")
        self.GenPass_Button = QtWidgets.QPushButton(self.Dropdown)
        self.GenPass_Button.setGeometry(QtCore.QRect(0, 0, 85, 41))
        self.GenPass_Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.GenPass_Button.setObjectName("GenPass_Button")
        self.Settings_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Settings_Button.setGeometry(QtCore.QRect(0, 40, 85, 29))
        self.Settings_Button.setObjectName("Settings_Button")
        self.Nuke_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Nuke_Button.setGeometry(QtCore.QRect(0, 70, 85, 41))
        self.Nuke_Button.setObjectName("Nuke_Button")
        self.Menu.addItem(self.Dropdown, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 125))
        self.page.setObjectName("page")
        self.Menu.addItem(self.page, "")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 540, 331, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Widget)
        self.Menu.setCurrentIndex(1)
        self.Menu.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.GenPass_Button.setText(_translate("Widget", "Generate \n"
"Password"))
        self.Settings_Button.setText(_translate("Widget", "Settings"))
        self.Nuke_Button.setText(_translate("Widget", "Nuclear \n"
"Option"))
        self.Menu.setItemText(self.Menu.indexOf(self.Dropdown), _translate("Widget", "Menu"))
        self.Menu.setItemText(self.Menu.indexOf(self.page), _translate("Widget", "Close"))
        self.commandLinkButton.setText(_translate("Widget", "New store account? Click here to add it"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

