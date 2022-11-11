# Exercise 1: Write a program which repeatedly reads numbers until the user
# enters “done”. Once “done” is entered, print out the total, count, and average
# of the numbers. If the user enters anything other than a number, detect their
# mistake using try and except and print an error message and skip to the next
# number.

total = None
count = None

while True :
    num = input('Please enter a number: ')
    if num == 'done':
        break
    try :
        intnum = int(num)
    except :
        if num != 'done' :
            print('Invalid input')
    if total is None :
        total = float(num)
    else :
        total = float(total) + float(num)
    if count is None :
        count = 1
    else :
        count = count + 1

average = float(total) / float(count)

print('Count: ', count)
print('Total: ', total)
print('Average: ', average)