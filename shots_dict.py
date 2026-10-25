shot = {
    "minute": 23,
    "player": "Игрок 1",
    "body_part": "нога",
    "xg": 0.76,
    "is_goal": False,
}

print("Минута:", shot["minute"])
print("xG:", shot["xg"])

shot["is_goal"] = True
print("Гол:", shot["is_goal"])

shots = [
    {"minute": 12, "xg": 0.05, "is_goal": False},
    {"minute": 23, "xg": 0.76, "is_goal": True},
    {"minute": 67, "xg": 0.12, "is_goal": False},
]
shots.append({"minute": 80, "xg": 0.33, "is_goal": False})
print(shots[3]["minute"])
print("Ударов:", len(shots))
print("xG второго удара:", shots[1]["xg"])