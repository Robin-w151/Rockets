import math

def dV(isp, m0, m1):
    
    g0  = float(9.80665)

    dVrocket = isp * g0 * math.log(m0/m1)

    return dVrocket
