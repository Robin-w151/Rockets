import sys
import tsiolkovsky
import timex

from PyQt4 import QtGui, QtCore
from rocketsMainWindow import Ui_Rockets as Dlg

class MainWindow(QtGui.QMainWindow, Dlg):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        # Slots setup
        self.connect(self.exit_button,
                     QtCore.SIGNAL("clicked()"),
                     self.exitMainWindow)

        self.connect(self.calculate_button,
                     QtCore.SIGNAL("clicked()"),
                     self.calculate)


    def exitMainWindow(self):
        self.close()


    def calculate(self):
        if self.tabWidget.currentIndex() == 0:
            # Daten einlesen
            dVrequired =   float(self.requiredv.text())
            isp =          float(self.isp.text())
            currentmass =  float(self.currentmass.text())
            totalthrust =  float(self.totalthrust.text())

            # burntime berechnen
            xh = tsiolkovsky.burntime(dVrequired, isp, currentmass, totalthrust)

            # Half Burntime
            xhhalf = xh / 2

            # Extend the hours to full hours, minutes and seconds
            hours, minutes, seconds = timex.time_extend(xh)
            
            hr, mi, se = timex.time_s(hours, minutes, seconds)

            hours = str(hours)
            minutes = str(minutes)
            seconds = str(seconds)

            self.burntimeoutput.setText(str("Full: " +
                                            hours + hr +
                                            minutes + mi +
                                            seconds + se))

            hours, minutes, seconds = timex.time_extend(xhhalf)

            hr, mi, se = timex.time_s(hours, minutes, seconds)

            hours = str(hours)
            minutes = str(minutes)
            seconds = str(seconds)
            
            self.burntime2output.setText(str("Half: " +
                                                    hours + hr +
                                                    minutes + mi +
                                                    seconds + se))
            
            
        elif self.tabWidget.currentIndex() == 1:
            # Daten einlesen
            isp = float(self.isp_2.text())
            m0 =  float(self.init_mass.text())
            m1 =  float(self.final_mass.text())

            # dV berechnen
            dV = tsiolkovsky.dV(isp, m0, m1)

            # dV ausgeben

            self.deltaVoutput.setText(str(round(dV, 3)))


application = QtGui.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(application.exec_())
