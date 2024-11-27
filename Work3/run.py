def calculate_days(start_km: float, target_km: float) -> int:
    days = 0
    current_km = start_km

    while current_km < target_km:
        current_km += current_km * 0.1
        days += 1

    return days

start_km = float(input("Введите количество километров в первый день: "))
target_km = float(input("Введите целевое количество километров: "))

days_needed = calculate_days(start_km, target_km)

print(f"Спортсмену понадобится {days_needed} дней, чтобы достичь цели.")
