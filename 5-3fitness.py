"""
Task 3: Create a summary function that provides a report of all activities and total calories burned for the day."""
def log_activities(activities, duration):
  for i in range(len(activities)):
    print(f"{activities[i]}: {duration[i]} minutes")

def calories_burned(duration):
    return duration * 3.5

activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]

log_activities(activities, duration)
print("Calories burned:", calories_burned(sum(duration)))
