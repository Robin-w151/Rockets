# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deltaVdialogue.ui'
#
# Created: Fri Aug  1 19:42:25 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dVCalculator(object):
    def setupUi(self, dVCalculator):
        dVCalculator.setObjectName(_fromUtf8("dVCalculator"))
        dVCalculator.resize(321, 301)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Objects-Rocket-icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dVCalculator.setWindowIcon(icon)
        dVCalculator.setWindowOpacity(1.0)
        self.calculate_button = QtGui.QPushButton(dVCalculator)
        self.calculate_button.setGeometry(QtCore.QRect(80, 240, 75, 23))
        self.calculate_button.setObjectName(_fromUtf8("calculate_button"))
        self.isp = QtGui.QLineEdit(dVCalculator)
        self.isp.setGeometry(QtCore.QRect(70, 50, 181, 20))
        self.isp.setObjectName(_fromUtf8("isp"))
        self.init_mass = QtGui.QLineEdit(dVCalculator)
        self.init_mass.setGeometry(QtCore.QRect(70, 100, 181, 20))
        self.init_mass.setObjectName(_fromUtf8("init_mass"))
        self.label = QtGui.QLabel(dVCalculator)
        self.label.setGeometry(QtCore.QRect(70, 30, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(dVCalculator)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(dVCalculator)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.final_mass = QtGui.QLineEdit(dVCalculator)
        self.final_mass.setGeometry(QtCore.QRect(70, 150, 181, 20))
        self.final_mass.setObjectName(_fromUtf8("final_mass"))
        self.exit_button = QtGui.QPushButton(dVCalculator)
        self.exit_button.setGeometry(QtCore.QRect(170, 240, 75, 23))
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.label_4 = QtGui.QLabel(dVCalculator)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.deltaVoutput = QtGui.QLabel(dVCalculator)
        self.deltaVoutput.setGeometry(QtCore.QRect(70, 200, 181, 21))
        self.deltaVoutput.setBaseSize(QtCore.QSize(0, 0))
        self.deltaVoutput.setAcceptDrops(False)
        self.deltaVoutput.setFrameShadow(QtGui.QFrame.Plain)
        self.deltaVoutput.setLineWidth(1)
        self.deltaVoutput.setText(_fromUtf8(""))
        self.deltaVoutput.setObjectName(_fromUtf8("deltaVoutput"))

        self.retranslateUi(dVCalculator)
        QtCore.QMetaObject.connectSlotsByName(dVCalculator)
        dVCalculator.setTabOrder(self.isp, self.init_mass)
        dVCalculator.setTabOrder(self.init_mass, self.final_mass)
        dVCalculator.setTabOrder(self.final_mass, self.calculate_button)

    def retranslateUi(self, dVCalculator):
        dVCalculator.setWindowTitle(_translate("dVCalculator", "ΔV Calculator", None))
        self.calculate_button.setText(_translate("dVCalculator", "Calculate dV", None))
        self.label.setText(_translate("dVCalculator", "Isp in seconds", None))
        self.label_2.setText(_translate("dVCalculator", "Initial Mass", None))
        self.label_3.setText(_translate("dVCalculator", "Final Mass", None))
        self.exit_button.setText(_translate("dVCalculator", "Beenden", None))
        self.label_4.setText(_translate("dVCalculator", "ΔV in m/s", None))

