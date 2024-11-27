def calculate_time_difference(h1: int, m1: int, h2: int, m2: int):
    total_minutes1 = h1 * 60 + m1
    total_minutes2 = h2 * 60 + m2

    difference = total_minutes2 - total_minutes1

    if difference < 0:
        difference += 1440

    hours = difference // 60
    minutes = difference % 60

    return hours, minutes


h1, m1 = map(int, input("Введите начальное время (чч мм)\n").split())
h2, m2 = map(int, input("Введите конечное время (чч мм)\n").split())

result_hours, result_minutes = calculate_time_difference(h1, m1, h2, m2)
print(f"Время в пути: {result_hours:02}:{result_minutes:02}")
