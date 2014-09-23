import sys
import tsiolkovsky

from PyQt4 import QtGui, QtCore
from deltaVdialogue import Ui_dVCalculator as Dlg

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
        isp = float(self.isp.text())
        m0 =  float(self.init_mass.text())
        m1 =  float(self.final_mass.text())

        # dV berechnen
        dV = tsiolkovsky.dV(isp, m0, m1)

        # dV ausgeben

        self.deltaVoutput.setText(str(round(dV, 3)))

    def exitHauptdialog(self):
        self.close()

        

app = QtGui.QApplication(sys.argv) 
dialog = Hauptdialog() 
dialog.show() 
sys.exit(app.exec_())
