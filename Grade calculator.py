#write a program to calculate student grade
name = input ("name of student: ")
subject= input ("subject: ")
score = int (input("enter score: "))

if (score >= 70 and score < 101):
    print ("Grade:  A")
elif (score>=60 and score < 70):
    print ("Grade:  B")
elif (score >=50 and score < 60):
    print ("Grade:  C")
elif (score >=40 and score < 50):
    print ("Grade:  D")
elif (score >= 30 and score < 40 ):
    print ("Grade:  E")
elif (score <= 29):
    print ("Grade:  F")
else:
    print ("Enter a valid score")
    
