largestnumber = -1
for i in [3, 41, 12, 9, 74, 15]:
    if i > largestnumber:
        largestnumber = i
print(largestnumber)

# I messed this up when writing it the first time by having "i = largestnumber"
# in line 4. Switching them fixed my issue. I also messed up by trying to
# initialize my largestnumber variable inside the for loop. 