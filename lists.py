days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daily_steps = []
for i in days:
    print("How many steps did you take on " + i + "?")
    daily_steps.append(int(input()))
for j in range(7):
    print("You took", daily_steps[j], "steps on", days[j], ".")
total_steps = sum(daily_steps)
print("You took", total_steps, "steps this week.")
average = round(total_steps / len(daily_steps))
print("You took an average of", average, "steps this week.")
