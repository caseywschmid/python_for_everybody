score = input('Enter a score between 0.0 and 1.0: ')
try :   
    score = float(score)
    if score >= 0.9 and score < 1.0 :
        grade = "A"
        print(grade)
    elif score >= 0.8 and score < 0.9 :
        grade = "B"
        print(grade)
    elif score >= 0.7 and score < 0.8 :
        grade = "C"
        print(grade)
    elif score >= 0.6 and score < 0.7 :
        grade = "D"
        print(grade)
    elif score < 0.6 and score >= 0.0 :
        grade = "F"
        print(grade)
    else :
        print('Error: Bad Score')
except :   
     print('Error: Bad Score')
