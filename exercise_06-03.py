# Exercise 3: Encapsulate this code in a function named count, and gen- eralize
# it so that it accepts the string and the letter as arguments.


string = input('Enter some text:')
letter = input('Enter a letter to be counted:')
def count(s, l) :
    counter = 0
    for letter in s :
        if letter == l:
            counter = counter + 1
    return counter
print(count(string, letter))