"""
Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = ['Dancing', 'Swimming', 'Biking'] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.
"""
def log_activities(activities, duration):
  for i in range(len(activities)):
    print(f"{activities[i]}: {duration[i]} minutes")

activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]

log_activities(activities, duration)