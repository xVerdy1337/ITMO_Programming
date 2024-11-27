from math import sqrt
from typing import Union, Optional, Tuple

def get_coefficient(prompt: str) -> Optional[float]:
    try:
        value = input(prompt)
        if value.lower() == 'q':
            return None
        return float(value)
    except ValueError:
        print("Ошибка: введите корректное число!")
        return None

def format_number(number: float) -> Union[int, float]:
    return int(number) if number.is_integer() else number

def solve_quadratic(a: float, b: float, c: float) -> Union[Tuple[float, float], str, float]:
    try:
        if a == 0:
            return "Ошибка: это не квадратное уравнение (a = 0)"

        discriminant = (b ** 2) - (4 * a * c)

        if discriminant < 0:
            return "Корней нет!"

        elif discriminant > 0:
            return (-b + sqrt(discriminant)) / (2*a), (-b - sqrt(discriminant)) / (2*a)

        else:
            return (-b) / (2*a)

    except Exception as e:
        return f"Ошибка при вычислении: {str(e)}"


def format_equation(a: float, b: float, c: float) -> str:
    terms = []

    # Форматируем ax^2
    a_str = format_number(a)
    if a != 1 and a != -1:
        terms.append(f"{a_str}x^2")
    else:
        if a == 1:
            terms.append("x^2")
        if a == -1:
            terms.append("-x^2")

    # Форматируем bx
    if b != 0:
        b_str = format_number(abs(b))
        if b == 1:
            terms.append("+ x")
        elif b == -1:
            terms.append("- x")
        elif b > 0:
            terms.append(f"+ {b_str}x")
        else:
            terms.append(f"- {b_str}x")

    # Форматируем c
    if c != 0:
        c_str = format_number(abs(c))
        if c > 0:
            terms.append(f"+ {c_str}")
        else:
            terms.append(f"- {c_str}")

    return " ".join(terms) + " = 0"


def main():
    print("Программа для решения квадратных уравнений вида ax^2 + bx + c = 0")
    print("Для выхода введите 'q' в любой момент")

    while True:
        # Получаем коэффициенты
        a = get_coefficient("Введите коэффициент a: ")
        if a is None:
            print("Программа завершена!")
            break

        b = get_coefficient("Введите коэффициент b: ")
        if b is None:
            print("Программа завершена!")
            break

        c = get_coefficient("Введите коэффициент c: ")
        if c is None:
            print("Программа завершена!")
            break

        # Выводим уравнение
        equation = format_equation(a, b, c)
        print(f"\nУравнение: {equation}")

        # Решаем уравнение
        result = solve_quadratic(a, b, c)

        # Выводим результат
        if isinstance(result, str):
            print(result)
        if isinstance(result, float):
            root1 = result

            print(f"Уравнение имеет один корень: x = {format_number(root1)}")
        else:
            root1, root2 = result

            print(f"Корни уравнения:\nx_1 = {format_number(root1)}\nx_2 = {format_number(root2)}")

if __name__ == "__main__":
    main()