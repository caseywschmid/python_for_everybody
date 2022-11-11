# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None. Then write a function
# called middle that takes a list and returns a new list that contains all but
# the first and last elements.



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def chop(l):
    del l[0]
    del l[len(l) - 1]

def middle(l):
    newl = l[1:len(l) - 1]
    return newl

print(middle(lst))
    


