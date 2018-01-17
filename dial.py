# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dial.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(409, 300)
        font = QtGui.QFont()
        font.setUnderline(False)
        Form.setFont(font)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dial = QtWidgets.QDial(Form)
        self.dial.setEnabled(True)
        self.dial.setGeometry(QtCore.QRect(130, 120, 151, 151))
        font = QtGui.QFont()
        font.setItalic(False)
        self.dial.setFont(font)
        self.dial.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dial.setMinimum(0)
        self.dial.setMaximum(254)
        self.dial.setSingleStep(1)
        self.dial.setObjectName("dial")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 60, 151, 26))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

