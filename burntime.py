import tsiolkovsky_gleichung
import terminate

term = 'n'

while term == 'n':
    tsiolkovsky_gleichung.burntime()
    print()
    term = terminate.terminate()      
    print()
