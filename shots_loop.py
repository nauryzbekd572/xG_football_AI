shots = [
    {"minute": 12, "xg": 0.05, "is_goal": False},
    {"minute": 23, "xg": 0.76, "is_goal": True},
    {"minute": 67, "xg": 0.12, "is_goal": False},
    {"minute": 80, "xg": 0.33, "is_goal": False},
    {"minute": 88, "xg": 0.45, "is_goal": True}
]

total_xg = 0
goals = 0
dangerous_shots=0
for shot in shots:
    print("Удар на", shot["minute"], "минуте, xG =", shot["xg"])
    total_xg = total_xg + shot["xg"]
    if shot["is_goal"]:
        goals = goals + 1
for shot in shots:
    if shot["xg"]>=0.3:
        dangerous_shots+=1

print(dangerous_shots)
print("Ударов:", len(shots))
print("Голов:", goals)
print("Суммарный xG:", round(total_xg, 2))