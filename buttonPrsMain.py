import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from buttonPrs import Ui_Button

class MyFirstGuiProgram(Ui_Button):
	def __init__(self, dialog):
		Ui_Button.__init__(self)
		self.setupUi(dialog)

		# Connect "add" button with a custom function (addInputTextToListbox)
		self.pushButton.clicked.connect(self.OK)

	def OK(self):
		print('OK pressed')

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
	prog = MyFirstGuiProgram(dialog)
	dialog.show()
	sys.exit(app.exec_())