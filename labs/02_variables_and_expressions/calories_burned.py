# Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368

# Type your code here.
age = float(input("What's your age? "))
weight = float(input("How much do you weigh? "))
heart_rate = float(input("What's your bpm? "))
time = float(input("How long are you working out for? "))

calories_burned = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368
print(f"Calories: {calories_burned:.2f} calories")