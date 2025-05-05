
student= {'Alice':85,'Mike':90,'Mark':95,'Peter':100}
var1=input('Enter the student\'s name :')
if (var1 in student) == 1:
    marks=student[var1]
    print("{}'s marks : {}".format(var1,marks))
else:
    print('Student not found')