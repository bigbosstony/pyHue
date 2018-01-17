# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buttonPrs.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Button(object):
    def setupUi(self, Button):
        Button.setObjectName("Button")
        Button.resize(383, 226)
        self.pushButton = QtWidgets.QPushButton(Button)
        self.pushButton.setGeometry(QtCore.QRect(230, 90, 73, 32))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Button)
        self.comboBox.setGeometry(QtCore.QRect(50, 70, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.horizontalSlider = QtWidgets.QSlider(Button)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 170, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.retranslateUi(Button)
        QtCore.QMetaObject.connectSlotsByName(Button)

    def retranslateUi(self, Button):
        _translate = QtCore.QCoreApplication.translate
        Button.setWindowTitle(_translate("Button", "Dialog"))
        self.pushButton.setText(_translate("Button", "Push"))

