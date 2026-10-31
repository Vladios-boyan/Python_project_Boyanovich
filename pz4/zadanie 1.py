#Дано вещественное число - цена 1 кг конфет. Вывести стоимость 1.2 1.4 ... , 2кг конфет
while True:
    try:
        price = float(input("Введите цену за 1кг: "))
        break
    except ValueError:
        print("Ошибка")
        price = input("Введите цену за 1кг: ")

weight = 1.2
while  weight <= 2:
    cost = weight * price
    weight += 0.2
    print(f"Стоимость за {weight:.2f}кг: {cost:.2f} рублей")
