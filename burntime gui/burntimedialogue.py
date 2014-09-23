# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'burntimedialogue.ui'
#
# Created: Sat Aug  2 18:39:38 2014
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

class Ui_burntimeCalculator(object):
    def setupUi(self, burntimeCalculator):
        burntimeCalculator.setObjectName(_fromUtf8("burntimeCalculator"))
        burntimeCalculator.resize(341, 371)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../deltaV/icon/Objects-Rocket-icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        burntimeCalculator.setWindowIcon(icon)
        burntimeCalculator.setWindowOpacity(1.0)
        self.calculate_button = QtGui.QPushButton(burntimeCalculator)
        self.calculate_button.setGeometry(QtCore.QRect(80, 320, 81, 23))
        self.calculate_button.setObjectName(_fromUtf8("calculate_button"))
        self.requiredv = QtGui.QLineEdit(burntimeCalculator)
        self.requiredv.setGeometry(QtCore.QRect(70, 50, 201, 20))
        self.requiredv.setObjectName(_fromUtf8("requiredv"))
        self.isp = QtGui.QLineEdit(burntimeCalculator)
        self.isp.setGeometry(QtCore.QRect(70, 100, 201, 20))
        self.isp.setObjectName(_fromUtf8("isp"))
        self.label_1 = QtGui.QLabel(burntimeCalculator)
        self.label_1.setGeometry(QtCore.QRect(70, 30, 201, 16))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_2 = QtGui.QLabel(burntimeCalculator)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 201, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(burntimeCalculator)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 201, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.currentmass = QtGui.QLineEdit(burntimeCalculator)
        self.currentmass.setGeometry(QtCore.QRect(70, 150, 201, 20))
        self.currentmass.setObjectName(_fromUtf8("currentmass"))
        self.exit_button = QtGui.QPushButton(burntimeCalculator)
        self.exit_button.setGeometry(QtCore.QRect(180, 320, 81, 23))
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.label_4 = QtGui.QLabel(burntimeCalculator)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 201, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.burntimeoutput = QtGui.QLabel(burntimeCalculator)
        self.burntimeoutput.setGeometry(QtCore.QRect(70, 250, 201, 21))
        self.burntimeoutput.setBaseSize(QtCore.QSize(0, 0))
        self.burntimeoutput.setAcceptDrops(False)
        self.burntimeoutput.setFrameShadow(QtGui.QFrame.Plain)
        self.burntimeoutput.setLineWidth(1)
        self.burntimeoutput.setText(_fromUtf8(""))
        self.burntimeoutput.setObjectName(_fromUtf8("burntimeoutput"))
        self.totalthrust = QtGui.QLineEdit(burntimeCalculator)
        self.totalthrust.setGeometry(QtCore.QRect(70, 200, 201, 20))
        self.totalthrust.setObjectName(_fromUtf8("totalthrust"))
        self.label_5 = QtGui.QLabel(burntimeCalculator)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 201, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.burntime2output = QtGui.QLabel(burntimeCalculator)
        self.burntime2output.setGeometry(QtCore.QRect(70, 280, 201, 21))
        self.burntime2output.setBaseSize(QtCore.QSize(0, 0))
        self.burntime2output.setAcceptDrops(False)
        self.burntime2output.setFrameShadow(QtGui.QFrame.Plain)
        self.burntime2output.setLineWidth(1)
        self.burntime2output.setText(_fromUtf8(""))
        self.burntime2output.setObjectName(_fromUtf8("burntime2output"))

        self.retranslateUi(burntimeCalculator)
        QtCore.QMetaObject.connectSlotsByName(burntimeCalculator)
        burntimeCalculator.setTabOrder(self.requiredv, self.isp)
        burntimeCalculator.setTabOrder(self.isp, self.currentmass)
        burntimeCalculator.setTabOrder(self.currentmass, self.totalthrust)
        burntimeCalculator.setTabOrder(self.totalthrust, self.calculate_button)
        burntimeCalculator.setTabOrder(self.calculate_button, self.exit_button)

    def retranslateUi(self, burntimeCalculator):
        burntimeCalculator.setWindowTitle(_translate("burntimeCalculator", "Burntime Calculator", None))
        self.calculate_button.setText(_translate("burntimeCalculator", "Burntime", None))
        self.label_1.setText(_translate("burntimeCalculator", "Required dV", None))
        self.label_2.setText(_translate("burntimeCalculator", "Isp", None))
        self.label_3.setText(_translate("burntimeCalculator", "Current Mass", None))
        self.exit_button.setText(_translate("burntimeCalculator", "Beenden", None))
        self.label_4.setText(_translate("burntimeCalculator", "Total Thrust", None))
        self.label_5.setText(_translate("burntimeCalculator", "Burntime", None))

