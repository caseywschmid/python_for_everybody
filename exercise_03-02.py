hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try :
    float(hours)
    float(rate)
    if float(hours) <= 40 :
        pay = hours*rate
        print('Pay:', pay)
    else : 
        othours = float(hours) - 40
        otrate = float(rate) * 1.5
        pay = (othours * otrate)+ (40 * float(rate))
        print('Pay:', pay)
except :
    print('Error, please input a valid number')