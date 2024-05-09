"""
Task 1: Code a function to calculate the average grade.
"""
def average_grade(grades):
  if len(grades) == 0:
    print("You didn't enter any grades!")
  else:
    average = sum(grades) / len(grades)
    print(f"The average of across the whole class is {average:.2f}.")

grades = []
while True:
    grade = input("Enter a grade (or 'done' to finish): ").strip() .lower()
    if grade.lower() .strip() == 'done':
        break
    grades.append(int(grade))

average_grade(grades)


