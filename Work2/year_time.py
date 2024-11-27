def get_season(month: str) -> str:
    months_to_seasons = {
        12: 'Зима', 1: 'Зима', 2: 'Зима',
        3: 'Весна', 4: 'Весна', 5: 'Весна',
        6: 'Лето', 7: 'Лето', 8: 'Лето',
        9: 'Осень', 10: 'Осень', 11: 'Осень'
    }

    if month in months_to_seasons:
        return months_to_seasons[month]
    else:
        raise ValueError("Неправильное значение месяца. Введите месяц как порядковый номер.")

month = input('Введите месяц (как порядковый)\n')
print(get_season(month))
