def is_leap(year: int) -> str:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'Високосный'
    return 'Невискокосный'

year = int(input("Введите год\n"))
print(is_leap(year))
