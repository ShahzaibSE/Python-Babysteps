marks = [87, 86, 98, 99, 80]
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
if percentage >= 90:
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