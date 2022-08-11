# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NukeForm.ui'
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
        self.Menu.setGeometry(QtCore.QRect(40, 20, 85, 171))
        self.Menu.setLineWidth(1)
        self.Menu.setObjectName("Menu")
        self.Dropdown = QtWidgets.QWidget()
        self.Dropdown.setGeometry(QtCore.QRect(0, 0, 85, 115))
        self.Dropdown.setObjectName("Dropdown")
        self.Home_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Home_Button.setGeometry(QtCore.QRect(0, -2, 85, 29))
        self.Home_Button.setStyleSheet("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton_2\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>0</x>\n"
"     <y>0</y>\n"
"     <width>85</width>\n"
"     <height>29</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>PushButton</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.Home_Button.setObjectName("Home_Button")
        self.GenPass_Button = QtWidgets.QPushButton(self.Dropdown)
        self.GenPass_Button.setGeometry(QtCore.QRect(0, 30, 85, 41))
        self.GenPass_Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.GenPass_Button.setObjectName("GenPass_Button")
        self.Settings_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Settings_Button.setGeometry(QtCore.QRect(0, 70, 85, 29))
        self.Settings_Button.setObjectName("Settings_Button")
        self.Menu.addItem(self.Dropdown, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 115))
        self.page.setObjectName("page")
        self.Menu.addItem(self.page, "")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 281, 171))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("NukeImage.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(231, 171))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Widget)
        self.Menu.setCurrentIndex(1)
        self.Menu.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.Home_Button.setText(_translate("Widget", "Home"))
        self.GenPass_Button.setText(_translate("Widget", "Generate \n"
"Password"))
        self.Settings_Button.setText(_translate("Widget", "Settings"))
        self.Menu.setItemText(self.Menu.indexOf(self.Dropdown), _translate("Widget", "Menu"))
        self.Menu.setItemText(self.Menu.indexOf(self.page), _translate("Widget", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

