# модуль 2 урок 2 задача 2
# ввод первого числа
while True:
    try:
        num_1 = int(input("Введите первое число:"))
        break
    except ValueError:
        print("Вы ввели нечисловое значение. Повторите.")
# ввод второго числа
while True:
    try:
        num_2 = int(input("Введите второе число:"))
        break
    except ValueError:
        print("Вы ввели нечисловое значение. Повторите.")
# ввод третьего числа
while True:
    try:
        num_3 = int(input("Введите третье число:"))
        break
    except ValueError:
        print("Вы ввели нечисловое значение. Повторите.")
medial_num = (num_1 + num_2 + num_3) / 3
print("{:.1f}".format(medial_num))