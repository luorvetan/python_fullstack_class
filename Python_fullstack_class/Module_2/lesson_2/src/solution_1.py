# модуль 2 урок 2 Задача 1
while True:
    begin_cost = input("Введите цену:")
    try:
        num_cost = int(begin_cost)
        end_cost = str(num_cost * 2)
        print("Ваша цена:",end_cost)
        break
    except ValueError:
        print("Вы ввели нечисловое значение. Повторите.")
