import tsiolkovsky
import terminate

term = 'n'

while term == 'n':
    
    dV = tsiolkovsky.dV()
    dV = round(dV, 3)

    print()
    print(dV,'m/s deltaV')
    print()
    term = terminate.terminate()
    print()
