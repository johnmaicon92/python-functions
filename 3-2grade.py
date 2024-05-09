"""
Task 2: Implement a function to find the highest and lowest grade.
"""

def average_grade(grades):
  if len(grades) == 0:
    print("You didn't enter any grades!")
  else:
    average = sum(grades) / len(grades)
    print(f"The average of across the whole class is {average:.2f}.")

def high_low_grade(grades):
   if len(grades) == 0:
     print("You didn't enter any grades!")
   else:
     mx = max(grades) 
     mn = min(grades)
     print(f"The highest grade is {mx} and the lowest grade is {mn}.")

grades = []
while True:
    grade = input("Enter a grade (or 'done' to finish): ").strip() .lower()
    if grade.lower() .strip() == 'done':
        break
    grades.append(int(grade))

average_grade(grades)
high_low_grade(grades)