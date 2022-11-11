hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours <= 40 :
    pay = hours*rate
    print('Pay:', pay)
else : 
    othours = hours - 40
    otrate = rate * 1.5
    pay = (othours * otrate)+ (40 * rate)
    print('Pay:', pay)