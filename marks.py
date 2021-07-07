english_marks = int(input("Marks in english: "))
science_marks = int(input("Marks in science: "))
maths_marks = int(input("Marks in maths: "))
sst_marks = int(input("Marks in sst: "))
hindi_marks = int(input("Marks in hindi: "))
total_marks = english_marks+science_marks+maths_marks+sst_marks+hindi_marks
percentage = total_marks/5

if percentage > 85:
    grade = "A"
elif percentage > 60 and percentage<85:
    grade = "B+"
elif percentage > 40 and percentage<60:
    grade = "B"
elif percentage > 30 and percentage<40:
    grade = "C"
else:
    grade = "D"

print(total_marks)
print(percentage)
print("Your grade is " + grade)