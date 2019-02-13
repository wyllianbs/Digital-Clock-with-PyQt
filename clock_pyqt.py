#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Relógio Digital
Prof. Wyllian B. da Silva
'''

from PyQt4 import QtCore, QtGui

class relogioDigital(QtGui.QLCDNumber):

	def __init__(self, parent=None):
		super(relogioDigital, self).__init__(parent)
		self.setSegmentStyle(QtGui.QLCDNumber.Filled)
		self.setNumDigits(8)
		temporizador = QtCore.QTimer(self)
		temporizador.timeout.connect(self.mostraTempo)
		temporizador.start(10)
		self.mostraTempo()
		self.setWindowTitle('Relógio Digital'.decode('UTF-8'))
		self.resize(800, 200)
		self.setStyleSheet("font-size:1200px;background-color:#ffeab4; border: 10px solid #ffeab4")

	def mostraTempo(self):
		tempo = QtCore.QTime.currentTime()
		texto = tempo.toString('hh:mm:ss')
		if (tempo.second() % 2) == 0:
			texto = texto[:2] + ' ' + texto[3:]
		self.display(texto)

if __name__ == '__main__':
	import sys
	aplicativo = QtGui.QApplication(sys.argv)
	relogio = relogioDigital()
	relogio.show()
	sys.exit(aplicativo.exec_())
