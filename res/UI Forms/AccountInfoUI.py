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
        Widget.resize(800, 600)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.StoreName = QtWidgets.QLabel(Widget)
        self.StoreName.setGeometry(QtCore.QRect(150, 60, 521, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.StoreName.setFont(font)
        self.StoreName.setAlignment(QtCore.Qt.AlignCenter)
        self.StoreName.setObjectName("StoreName")
        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(77, 130, 651, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(110, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(110, 270, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(270, 150, 421, 61))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(270, 210, 421, 61))
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(270, 270, 421, 61))
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(Widget)
        self.line_2.setGeometry(QtCore.QRect(110, 150, 581, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Widget)
        self.line_3.setGeometry(QtCore.QRect(100, 159, 16, 171))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Widget)
        self.line_4.setGeometry(QtCore.QRect(110, 320, 581, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Widget)
        self.line_5.setGeometry(QtCore.QRect(680, 160, 16, 171))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Widget)
        self.line_6.setGeometry(QtCore.QRect(260, 160, 16, 171))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Widget)
        self.line_7.setGeometry(QtCore.QRect(110, 200, 581, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Widget)
        self.line_8.setGeometry(QtCore.QRect(110, 260, 581, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.showPassword = QtWidgets.QPushButton(Widget)
        self.showPassword.setGeometry(QtCore.QRect(630, 270, 61, 61))
        self.showPassword.setObjectName("showPassword")
        self.label_7 = QtWidgets.QLabel(Widget)
        self.label_7.setGeometry(QtCore.QRect(140, 420, 91, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setGeometry(QtCore.QRect(560, 420, 121, 20))
        self.label_8.setObjectName("label_8")
        self.HIBPst = QtWidgets.QLabel(Widget)
        self.HIBPst.setGeometry(QtCore.QRect(10, 460, 341, 61))
        self.HIBPst.setAlignment(QtCore.Qt.AlignCenter)
        self.HIBPst.setObjectName("HIBPst")
        self.BFTime = QtWidgets.QLabel(Widget)
        self.BFTime.setGeometry(QtCore.QRect(440, 460, 351, 91))
        self.BFTime.setAlignment(QtCore.Qt.AlignCenter)
        self.BFTime.setObjectName("BFTime")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "Back"))
        self.StoreName.setText(_translate("Widget", "TextLabel"))
        self.label.setText(_translate("Widget", "Email:"))
        self.label_2.setText(_translate("Widget", "Username:"))
        self.label_3.setText(_translate("Widget", "Password:"))
        self.label_4.setText(_translate("Widget", "TextLabel"))
        self.label_5.setText(_translate("Widget", "TextLabel"))
        self.label_6.setText(_translate("Widget", "TextLabel"))
        self.showPassword.setText(_translate("Widget", "Show"))
        self.label_7.setText(_translate("Widget", "HIBP Status:"))
        self.label_8.setText(_translate("Widget", "Brute Force Time:"))
        self.HIBPst.setText(_translate("Widget", "TextLabel"))
        self.BFTime.setText(_translate("Widget", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
