student_name="Fathima"

python_marks=90
maths_marks=95
english_marks=88

total=python_marks+maths_marks+english_marks

average=total/3
if average>=90:
    grade="A+"
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=40:
    grade="c"
else:
    grade="Fail"
print("STUDENT PERFORMANCE REPORT")
print("------------------------------")
print("Student Name:",student_name)
print("Total Marks:",total)
print("Average Marks:",average)
print("Grade:",grade)
