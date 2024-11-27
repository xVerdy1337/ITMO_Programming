def calculate_points(x: float, y: float) -> int:
    if x == 0 or y == 0:
        return 0
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3

total_points = 0

while True:
    input_data = input("Введите координаты точки (x y) или 'STOP' для завершения: ")
    if input_data.upper() == 'STOP':
        break

    try:
        x, y = map(float, input_data.split())
        points = calculate_points(x, y)
        print(f"Точка ({x}, {y}) получает {points} баллов.")
        total_points += points
    except ValueError:
        print("Некорректный ввод. Попробуйте снова.")

print(f"Общая сумма баллов: {total_points}")
