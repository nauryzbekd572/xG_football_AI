lines = [
    "Команда А;5;2;1.71",
    "Команда Б;4;1;0.49",
]

with open("summary.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

with open("summary.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
try:
    with open("sum.txt","r",encoding="utf-8") as file_1:
         text_1=file_1.read()
except FileNotFoundError:
        text_1=" 1"
        print("no such file_1")
        print(text_1)
