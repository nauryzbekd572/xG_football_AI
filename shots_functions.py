def calc_total_xg(shots):
    total = 0
    for shot in shots:
        total = total + shot["xg"]
    return round(total, 2)


def count_goals(shots):
    goals = 0
    for shot in shots:
        if shot["is_goal"]:
            goals = goals + 1
    return goals


def print_summary(name, shots):
    goals = count_goals(shots)
    xg = calc_total_xg(shots)
    print(name, "- ударов:", len(shots), "голов:", goals, "xG:", xg)


team_a = [
    {"minute": 12, "xg": 0.05, "is_goal": False},
    {"minute": 23, "xg": 0.76, "is_goal": True},
    {"minute": 67, "xg": 0.12, "is_goal": False},
    {"minute": 80, "xg": 0.33, "is_goal": False},
    {"minute": 88, "xg": 0.45, "is_goal": True},
]

team_b = [
    {"minute": 5, "xg": 0.08, "is_goal": False},
    {"minute": 30, "xg": 0.15, "is_goal": False},
    {"minute": 55, "xg": 0.04, "is_goal": False},
    {"minute": 71, "xg": 0.22, "is_goal": True},
]

print_summary("Команда А", team_a)
print_summary("Команда Б", team_b)
def count_dangerous_shots(shots, threshold):
    danger_shot=0
    for shot in shots:
        if shot["xg"]>=threshold:
            danger_shot+=1
    return danger_shot
danger_shot=count_dangerous_shots(team_b,0.2)
print(danger_shot)