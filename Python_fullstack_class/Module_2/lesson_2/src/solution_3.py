# модуль 2 урок 2 задача 3
v_book = 2
v_stat = 1.5
v_toy = 3
# ввод количества коробок книг
while True:
    try:
        books_boxes = int(input("Введите количество коробок книг:"))
        break
    except ValueError:
        print("Вы ввели нечисловое значение. Повторите.")
# ввод количества коробок канцтоваров
while True:
    try:
        stats_boxes = int(input("Введите количество коробок канцтоваров:"))
        break
    except ValueError:
        print("Вы ввели нечисловое значение. Повторите.")
# ввод количества коробок игрушек
while True:
    try:
        toys_boxes = int(input("Введите количество коробок игрушек:"))
        break
    except ValueError:
        print("Вы ввели нечисловое значение. Повторите.")
vol_products = v_book * books_boxes + v_stat * stats_boxes + v_toy * toys_boxes
print("{:.1f}".format(vol_products))