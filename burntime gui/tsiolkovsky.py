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
