import math
import timex

def dV():
    
    isp = float(input('Enter Isp:          '))
    m0  = float(input('Enter initial mass: '))
    m1  = float(input('Enter final mass:   '))
    g0  = float(9.80665)

    dVrocket = isp * g0 * math.log(m0/m1)

    return dVrocket

def burntime():
    
    dVrequired = float(input('Enter the required dV:  '))
    isp        = float(input('Enter Isp in seconds:   '))
    mass       = float(input('Enter the current mass: '))
    thrust     = float(input('Enter the total thrust: '))
    g0         = float(9.80665)

    print()

    # Massloss rate
    massloss_per_sec = thrust / isp / g0

    # Burntime in seconds
    xs = (mass / math.e ** (dVrequired / (isp * g0)) - mass) / (-massloss_per_sec)

    # Burntime in hours
    xh = xs / 3600

    # Half Burntime
    xhhalf = xh / 2

    # Extend the hours to full hours, minutes and seconds
    hours, minutes, seconds = timex.time_extend(xh)
    
    hr, mi, se = timex.time_s(hours, minutes, seconds)

    print('Full burntime:', hours, hr, minutes, mi, seconds, se)

    hours, minutes, seconds = timex.time_extend(xhhalf)

    hr, mi, se = timex.time_s(hours, minutes, seconds)
    
    print('Half burntime:', hours, hr, minutes, mi, seconds, se)





