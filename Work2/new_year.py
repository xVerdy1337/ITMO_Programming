from datetime import datetime, date

def is_valid_date(day: int, month: int):
    try:
        date(datetime.now().year, month, day)
        return True
    except ValueError:
        return False


def days_until_new_year(day: int, month: int):
    today = date.today()
    this_year = today.year
    given_date = date(this_year, month, day)

    new_year = date(this_year, 12, 31)

    return (new_year - given_date).days


try:
    day = int(input("Введите день (1-31)\n"))
    month = int(input("Введите месяц (1-12)\n"))

    if not is_valid_date(day, month):
        raise ValueError("Некорректная дата")

    days_left = days_until_new_year(day, month)
    print(f"До Нового года осталось {days_left} дней.")

except ValueError as e:
    print(f"Ошибка: {e}. Пожалуйста, введите корректные значения.")
