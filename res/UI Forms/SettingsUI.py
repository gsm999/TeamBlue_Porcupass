# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsForm.ui'
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
        self.Menu.setGeometry(QtCore.QRect(20, 20, 85, 181))
        self.Menu.setLineWidth(1)
        self.Menu.setObjectName("Menu")
        self.Dropdown = QtWidgets.QWidget()
        self.Dropdown.setGeometry(QtCore.QRect(0, 0, 85, 125))
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
        self.GenPass_Button.setGeometry(QtCore.QRect(0, 20, 85, 41))
        self.GenPass_Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.GenPass_Button.setObjectName("GenPass_Button")
        self.Nuke_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Nuke_Button.setGeometry(QtCore.QRect(0, 60, 85, 41))
        self.Nuke_Button.setObjectName("Nuke_Button")
        self.Menu.addItem(self.Dropdown, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 125))
        self.page.setObjectName("page")
        self.Menu.addItem(self.page, "")
        self.SettingsTree = QtWidgets.QTreeWidget(Widget)
        self.SettingsTree.setGeometry(QtCore.QRect(150, 0, 651, 581))
        self.SettingsTree.setAutoFillBackground(True)
        self.SettingsTree.setObjectName("SettingsTree")
        self.SettingsTree.header().setVisible(False)

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
        self.Nuke_Button.setText(_translate("Widget", "Nuclear \n"
"Option"))
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

