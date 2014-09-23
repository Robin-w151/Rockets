def time_extend(hours):
    timehf = hours
    #timehi = 0
    timehi = int(timehf)
    timemf = (timehf - timehi) * 60
    #timemi = 0
    timemi = int(timemf)
    timesf = (timemf - timemi) * 60
    #timesi = 0
    timesi = round(timesf,0)
    if timesi == 60.0:
        timemi += 1
        timesi = 0
    if timemi == 60:
        timehi += 1
        timemi = 0
    
    return (timehi, timemi, timesi)


def time_s(hours, minutes, seconds):
    
    if hours == 1:
        hr = ' hour '
    else:
        hr = ' hours '

    if minutes == 1:
        mi = ' minute '
    else:
        mi = ' minutes '

    if seconds == 1:
        se = ' second'
    else:
        se = ' seconds'

    return hr, mi, se
