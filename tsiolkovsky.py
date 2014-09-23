import math

def burntime(dVrequired, isp, mass, thrust):
    
    g0         = float(9.80665)

    # Massloss rate
    massloss_per_sec = thrust / isp / g0

    # Burntime in seconds
    xs = (mass / math.e ** (dVrequired / (isp * g0)) - mass) / (-massloss_per_sec)

    # Burntime in hours
    xh = xs / 3600

    return xh


def dV(isp, m0, m1):
    
    g0  = float(9.80665)

    dVrocket = isp * g0 * math.log(m0/m1)

    return dVrocket
