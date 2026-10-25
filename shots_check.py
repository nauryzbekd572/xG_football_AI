shots = 2
goals = 5
goals = 1
shots = 3
xg = 0.05
if goals > shots:
    print("Ошибка в данных: голов больше, чем ударов")
else:
    print("Данные выглядят правильно")

xg = 0.76
if xg < 0 or xg > 1:
    print("Ошибка: xG должен быть от 0 до 1")
elif xg >= 0.5:
    print("Очень опасный момент")
elif xg >= 0.1:
    print("Умеренно опасный удар")
else:
    print("Удар из малоопасной позиции")