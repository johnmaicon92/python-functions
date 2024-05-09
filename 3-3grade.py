"""
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
"""

def average_grade(grades):
  if len(grades) == 0:
    print("You didn't enter any grades!")
  else:
    average = sum(grades) / len(grades)
    print(f"The average of across the whole class is {average:.2f}.")

def high_low_grade(grades):
   if len(grades) == 0:
     print("You did't enter any grades!")
   else:
     mx = max(grades) 
     mn = min(grades)
     print(f"The highest grade is {mx} and the lowest grade is {mn}.")

def letter_grade(grades):
   if len(grades) == 0:
     print("You didn't enter any grades!")
   else:
     for grade in grades:
       if grade >= 90:
         print(f"{grade} is an A")
       elif grade >= 80:
         print(f"{grade} is a B")
       elif grade >= 70:
         print(f"{grade} is a C")
       elif grade >= 60:
         print(f"{grade} is a D")
       else:
         print(f"{grade} is an F")

grades = []
while True:
    grade = input("Enter a grade (or 'done' to finish): ").strip()
    if grade.lower().strip() == 'done':
        break
    grades.append(int(grade))

average_grade(grades)
high_low_grade(grades)
letter_grade(grades)