import sys
import tsiolkovsky
import timex

from PyQt4 import QtGui, QtCore
from burntimedialogue import Ui_burntimeCalculator as Dlg

class Hauptdialog(QtGui.QDialog, Dlg): 
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.setupUi(self)

        # Slots einrichten
        self.connect(self.calculate_button,
                     QtCore.SIGNAL("clicked()"),
                     self.calculate)
        self.connect(self.exit_button,
                     QtCore.SIGNAL("clicked()"),
                     self.exitHauptdialog)

    def calculate(self):
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
        

    def exitHauptdialog(self):
        self.close()

        

app = QtGui.QApplication(sys.argv) 
dialog = Hauptdialog() 
dialog.show() 
sys.exit(app.exec_())
