# лесник
trail = "Тропа"
home = "Дом"
maze = [0, -1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, -1, 0]
maze2 = {1: "oak", 2: "spruce", 3: "spruce", 4: "birch", 5: "birch",
         6: "spruce", 7: "oak", 8: "spruce", 9: "spruce", 10: "birch", 11: "spruce",
         12: "oak", 13: "birch", 14: "spruce"}
print("Начало пути")
print(trail)
for i in maze:
    if i == -1:
        print('налево')
    if i == 0:
        print('прямо')
    elif i == 1:
        print('направо')
print("Путь определил, теперь собираю грибы")

for key, value in maze2.items():
    if value == "oak":
        print("дуб плюс один грибок")
    if value == "birch":
        print("береза плюс один грибок")
    elif value == "spruce":
        print('сосна гриба нету (')
count = (sum(1 for v in maze2.values() if v == "oak")
         + sum(1 for s in maze2.values() if s == "birch"))
print(f'вернулся в {home}, итого собрал {count} грибов')
