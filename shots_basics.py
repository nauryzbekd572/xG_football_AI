team = "Команда А"
shots = 5
xg_value = 0.76
is_goal = True

print(type(team), type(shots), type(xg_value), type(is_goal))

shot_xg = [0.05, 0.12, 0.76, 0.03, 0.31]
shot_xg.append(0.45)
print("Количество ударов:", len(shot_xg))
print("Первый удар, xG:", shot_xg[0])
print("Суммарный xG:", round(sum(shot_xg), 2))

