# Exercise 2: Write a program to prompt for a file name, and then read through
# the file and look for lines of the form: X-DSPAM-Confidence: 0.8475 When you
# encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to
# extract the floating-point number on the line. Count these lines and then
# compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.


filename = input("Enter file name: ")
if len(filename) < 1 :
    filename = 'mbox-short.txt'
filehandle = open(filename)
count = 0 
total = 0 
for line in filehandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    total = total + float(line[20 : ])
average = total / count
print("Average spam confidence:", average)

    