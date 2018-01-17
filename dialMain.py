#!/usr/local/bin/python3



import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dial import Ui_Form
from phue import Bridge


b = Bridge('192.168.0.10')

lights = b.get_light_objects('id')


class MyFirstGuiProgram(Ui_Form):


	def __init__(self, dialog):

		Ui_Form.__init__(self)
		self.setupUi(dialog)

		for l in lights:
			self.comboBox.addItem(lights[l].name)

		self.comboBox.activated.connect(self.getLightValue)

		self.dial.valueChanged['int'].connect(self.setHueLight)

		self.dial.setValue(b.get_light(self.comboBox.currentIndex() + 1, 'bri'))


	def getLightValue(self, index):


		# if (b.get_light(index + 1, 'bri')) <= 1:
		# 	self.dial.setValue(0)
		# else:
		# 	self.dial.setValue(b.get_light(index + 1, 'bri'))

		self.dial.setValue(b.get_light(index + 1, 'bri'))
		

		# print(self.comboBox.currentIndex())
		# if index in lights:
			# print(lights[index].light_id)


	def setHueLight(self, value):
		if self.dial.value() > 1:
			b.set_light(self.comboBox.currentIndex() + 1, {'bri': self.dial.value(), 'transitiontime': 1, 'on' : True})
		else:
			if (b.get_light(self.comboBox.currentIndex() + 1, 'bri')) > 1:
				b.set_light(self.comboBox.currentIndex() + 1, 'bri', 1)
			else:
				b.set_light(self.comboBox.currentIndex() + 1, 'on',	 False)

			# print(b.get_light(self.comboBox.currentIndex() + 1, 'bri'))



	


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
	prog = MyFirstGuiProgram(dialog)
	dialog.show()
	sys.exit(app.exec_())


