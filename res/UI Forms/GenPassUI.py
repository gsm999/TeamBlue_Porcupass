# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\TeamBlue_Porcupass\res\UI Forms\GenPassForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        Widget.setFont(font)
        self.Menu = QtWidgets.QToolBox(Widget)
        self.Menu.setGeometry(QtCore.QRect(30, 20, 85, 181))
        self.Menu.setLineWidth(1)
        self.Menu.setObjectName("Menu")
        self.Dropdown = QtWidgets.QWidget()
        self.Dropdown.setGeometry(QtCore.QRect(0, 0, 85, 127))
        self.Dropdown.setObjectName("Dropdown")
        self.Home_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Home_Button.setGeometry(QtCore.QRect(0, 0, 85, 31))
        self.Home_Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Home_Button.setObjectName("Home_Button")
        self.Settings_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Settings_Button.setGeometry(QtCore.QRect(0, 60, 85, 29))
        self.Settings_Button.setObjectName("Settings_Button")
        self.Nuke_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Nuke_Button.setGeometry(QtCore.QRect(0, 88, 85, 41))
        self.Nuke_Button.setObjectName("Nuke_Button")
        self.Accounts_Button = QtWidgets.QPushButton(self.Dropdown)
        self.Accounts_Button.setGeometry(QtCore.QRect(0, 30, 85, 29))
        self.Accounts_Button.setStyleSheet("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
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
        self.Accounts_Button.setObjectName("Accounts_Button")
        self.Menu.addItem(self.Dropdown, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 127))
        self.page.setObjectName("page")
        self.Menu.addItem(self.page, "")
        self.GenPassOut = QtWidgets.QTextBrowser(Widget)
        self.GenPassOut.setGeometry(QtCore.QRect(200, 180, 401, 31))
        self.GenPassOut.setInputMethodHints(QtCore.Qt.ImhNone)
        self.GenPassOut.setObjectName("GenPassOut")
        self.GeneratePass = QtWidgets.QPushButton(Widget)
        self.GeneratePass.setGeometry(QtCore.QRect(360, 220, 81, 21))
        self.GeneratePass.setObjectName("GeneratePass")
        self.layoutWidget = QtWidgets.QWidget(Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 268, 591, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NumericPass = QtWidgets.QCheckBox(self.layoutWidget)
        self.NumericPass.setObjectName("NumericPass")
        self.verticalLayout_2.addWidget(self.NumericPass)
        self.LowerPass = QtWidgets.QCheckBox(self.layoutWidget)
        self.LowerPass.setObjectName("LowerPass")
        self.verticalLayout_2.addWidget(self.LowerPass)
        self.CapPass = QtWidgets.QCheckBox(self.layoutWidget)
        self.CapPass.setObjectName("CapPass")
        self.verticalLayout_2.addWidget(self.CapPass)
        self.SpecCharPass = QtWidgets.QCheckBox(self.layoutWidget)
        self.SpecCharPass.setObjectName("SpecCharPass")
        self.verticalLayout_2.addWidget(self.SpecCharPass)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PassCharLim = QtWidgets.QSpinBox(self.layoutWidget)
        self.PassCharLim.setMinimum(15)
        self.PassCharLim.setObjectName("PassCharLim")
        self.horizontalLayout.addWidget(self.PassCharLim)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.SaveGenPassSet = QtWidgets.QCheckBox(self.layoutWidget)
        self.SaveGenPassSet.setMouseTracking(False)
        self.SaveGenPassSet.setObjectName("SaveGenPassSet")
        self.verticalLayout.addWidget(self.SaveGenPassSet)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

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
        self.Accounts_Button.setText(_translate("Widget", "Accounts"))
        self.Menu.setItemText(self.Menu.indexOf(self.Dropdown), _translate("Widget", "Menu"))
        self.Menu.setItemText(self.Menu.indexOf(self.page), _translate("Widget", "Close"))
        self.GeneratePass.setText(_translate("Widget", "Generate"))
        self.NumericPass.setText(_translate("Widget", " Numbers "))
        self.LowerPass.setText(_translate("Widget", "Lowecase Only"))
        self.CapPass.setText(_translate("Widget", "Uppercase Only"))
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