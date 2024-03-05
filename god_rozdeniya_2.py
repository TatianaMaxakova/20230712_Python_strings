def get_god():
    while True:
        try:
            god = int(input("Введите ваш год рождения: "))
            if god > 2024:
                raise ValueError("Возраст не может быть отрицательным")
            break
        except ValueError:
            print("Ошибка: введенное значение не является годом рождения")

    vozrast = 2024 - god
    print(f"Ваш возраст: {vozrast}")

get_god()