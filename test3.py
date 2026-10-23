grades={"liam":67, "aiden":98, "xander":73, "tatum":89, "mark":76}
total=0
for scores in grades.values:
    total+=scores
average=total/len(grades)
print("The class average is:",average)
highestscore=max(grades.values())
lowestscore=min(grades.values())
for name scores in grades.items():
    if scores==highestscore:
    higheststudent=name
    if score==lowestscore:
    loweststudent=name
print("Highest scoring student:", higheststudent,",",highestscore)
print("lowest scoring student:",loweststudent,","lowestscore)
student=input("enter a student name: ")
scores=grades.get(stu)
