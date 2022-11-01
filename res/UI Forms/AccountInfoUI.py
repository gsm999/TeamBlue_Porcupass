# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountInfoForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1263, 772)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet("background-color: rgb(194, 173, 173);")
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(100, 40, 1041, 611))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("background-color: rgb(127, 180, 233);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(37, 45, 50);\n"
"")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.StoreName = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.StoreName.setFont(font)
        self.StoreName.setStyleSheet("color: rgb(0, 0, 0);")
        self.StoreName.setAlignment(QtCore.Qt.AlignCenter)
        self.StoreName.setObjectName("StoreName")
        self.verticalLayout.addWidget(self.StoreName)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("border-color: rgb(64, 90, 124);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.copyUsername = QtWidgets.QPushButton(self.widget)
        self.copyUsername.setStyleSheet("background-color: rgb(127, 180, 233);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(37, 45, 50);")
        self.copyUsername.setAutoDefault(True)
        self.copyUsername.setObjectName("copyUsername")
        self.gridLayout_2.addWidget(self.copyUsername, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.storeDelete = QtWidgets.QPushButton(self.widget)
        self.storeDelete.setMinimumSize(QtCore.QSize(100, 50))
        self.storeDelete.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.storeDelete.setStyleSheet("background-color: rgb(127, 180, 233);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(37, 45, 50);")
        self.storeDelete.setObjectName("storeDelete")
        self.horizontalLayout.addWidget(self.storeDelete)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.copyPassword = QtWidgets.QPushButton(self.widget)
        self.copyPassword.setStyleSheet("background-color: rgb(127, 180, 233);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(37, 45, 50);")
        self.copyPassword.setAutoDefault(True)
        self.copyPassword.setObjectName("copyPassword")
        self.gridLayout_3.addWidget(self.copyPassword, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.showPassword = QtWidgets.QPushButton(self.widget)
        self.showPassword.setStyleSheet("background-color: rgb(127, 180, 233);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(37, 45, 50);")
        self.showPassword.setAutoDefault(True)
        self.showPassword.setObjectName("showPassword")
        self.gridLayout_3.addWidget(self.showPassword, 0, 2, 1, 1)
        self.update_password = QtWidgets.QPushButton(self.widget)
        self.update_password.setStyleSheet("background-color: rgb(127, 180, 233);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(37, 45, 50);")
        self.update_password.setAutoDefault(True)
        self.update_password.setObjectName("update_password")
        self.gridLayout_3.addWidget(self.update_password, 0, 4, 1, 1)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.gridLayout_3)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.line_3)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_4)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Password_status_box = QtWidgets.QLabel(self.widget)
        self.Password_status_box.setStyleSheet("color: rgb(0, 0, 0);")
        self.Password_status_box.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Password_status_box.setObjectName("Password_status_box")
        self.horizontalLayout_2.addWidget(self.Password_status_box)
        self.password_age_box = QtWidgets.QLabel(self.widget)
        self.password_age_box.setStyleSheet("color: rgb(0, 0, 0);")
        self.password_age_box.setAlignment(QtCore.Qt.AlignCenter)
        self.password_age_box.setObjectName("password_age_box")
        self.horizontalLayout_2.addWidget(self.password_age_box)
        self.password_strength_box = QtWidgets.QLabel(self.widget)
        self.password_strength_box.setMinimumSize(QtCore.QSize(0, 133))
        self.password_strength_box.setStyleSheet("color: rgb(0, 0, 0);")
        self.password_strength_box.setText("")
        self.password_strength_box.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.password_strength_box.setObjectName("password_strength_box")
        self.horizontalLayout_2.addWidget(self.password_strength_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.time_to_crack = QtWidgets.QLabel(self.widget)
        self.time_to_crack.setStyleSheet("color: rgb(0, 0, 0);")
        self.time_to_crack.setAlignment(QtCore.Qt.AlignCenter)
        self.time_to_crack.setObjectName("time_to_crack")
        self.verticalLayout_3.addWidget(self.time_to_crack)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setStyleSheet("color: rgb(64, 90, 124);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_2)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem9)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "Back"))
        self.StoreName.setText(_translate("Widget", "TextLabel"))
        self.label_4.setText(_translate("Widget", "TextLabel"))
        self.label.setText(_translate("Widget", "Email:"))
        self.copyUsername.setText(_translate("Widget", "Copy"))
        self.label_2.setText(_translate("Widget", "Username:"))
        self.label_5.setText(_translate("Widget", "TextLabel"))
        self.storeDelete.setText(_translate("Widget", "Delete Account"))
        self.label_3.setText(_translate("Widget", "Password:"))
        self.copyPassword.setText(_translate("Widget", "Copy"))
        self.label_6.setText(_translate("Widget", "TextLabel"))
        self.showPassword.setText(_translate("Widget", "Show"))
        self.update_password.setText(_translate("Widget", "Update"))
        self.Password_status_box.setText(_translate("Widget", "<html><head/><body><p>Password Breaches:</p><p>1</p></body></html>"))
        self.password_age_box.setText(_translate("Widget", "TextLabel"))
        self.time_to_crack.setText(_translate("Widget", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
