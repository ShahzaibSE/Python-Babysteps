marks = []
eng_marks = int(input("Enter marks for English:"))
marks.append(eng_marks)
#
chemistry_marks = int(input("Enter marks for Chemistry:"))
marks.append(chemistry_marks)
#
computer_marks = int(input("Enter marks for Computer:"))
marks.append(computer_marks)
#
physics_marks = int(input("Enter marks for Physics:"))
marks.append(physics_marks)
#
math_marks = int(input("Enter marks for Math:"))
marks.append(math_marks)
#
# marks = [87, 86, 98, 99, 80]
total = 0
for mark in marks:
     total += mark
print(f"Total marks: {total}")
#
# Calculate percentage.
percentage = total / len(marks)
print(f"Percentage: {percentage}")
#
# Grading student.
if percentage >= 80:
    print("Grade: A+")
elif percentage >= 70 and percentage <80:
    print("Grade: A")
elif percentage >= 60 and percentage <70:
    print("Grade: B")
elif percentage >= 50 and percentage <60:
    print("Grade: C")
elif percentage >= 40 and percentage <50:
    print("Grade: D")
elif percentage >= 30 and percentage <40:
    print("Grade: E")
else:
    print("Failed!")

number = 12
print(type(number))

numbers_in_words = {1: "one"}
print(type(numbers_in_words))