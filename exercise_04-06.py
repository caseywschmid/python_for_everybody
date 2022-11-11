


hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
def computepay(h, r):
    h = float(h)
    r = float(r)
    if h <= 40 :
        pay = h * r
        return pay
    else :
        oth = h - 40
        otr = r * 1.5
        pay = (oth * otr)+ (40 * r)
        return pay
try :
    print('Pay: ', computepay(hours, rate))
except :
    print('Error, please input a valid number')