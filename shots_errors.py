def parse_xg(text):
    try:
        value = float(text.replace(",", "."))
    except ValueError:
        print("Не удалось прочитать xG:", text)
        return None
    if value < 0 or value > 1:
        print("xG должен быть от 0 до 1:", value)
        return None
    return value


print(parse_xg("0,76"))
print(parse_xg("0.3"))
print(parse_xg("abc"))
print(parse_xg("1.5"))