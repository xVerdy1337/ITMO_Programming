from math import pi
from typing import List, Union, Optional, Tuple


def get_user_choice(allowed_values: List[int]) -> Optional[int]:
    print("\nПлощадь какой фигуры Вы хотите вычислить? Доступные фигуры:")
    print("1. Круг\n2. Прямоугольник\n3. Треугольник")
    choice = input("Выберите номер фигуры (или 'q' для выхода): ")

    if choice.lower() == 'q':
        return -1

    if not choice.isdigit():
        return None

    value = int(choice)
    return value if value in allowed_values else None


def validate_positive_numbers(*args: float) -> bool:
    return all(num > 0 for num in args)


def validate_triangle(a: float, b: float, c: float) -> bool:
    return (validate_positive_numbers(a, b, c) and
            a + b > c and b + c > a and a + c > b)


def get_number_input(prompt: str) -> Optional[float]:
    value = input(prompt)
    if value.lower() == 'q':
        return -1

    try:
        num = float(value)
        if not validate_positive_numbers(num):
            print("Число должно быть положительным!")
            return None
        return num
    except ValueError:
        return None


def get_multiple_numbers(prompt: str, count: int) -> Optional[Tuple[float, ...]]:
    values = input(prompt)
    if values.lower() == 'q':
        return (-1,)

    try:
        numbers = values.split()
        if len(numbers) != count:
            print(f"Требуется ввести {count} числа(ел)!")
            return None

        nums = tuple(float(x) for x in numbers)
        if not validate_positive_numbers(*nums):
            print("Все числа должны быть положительными!")
            return None

        return nums
    except ValueError:
        return None


def calculate_circle_area(radius: float) -> float:
    return pi * radius ** 2


def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height


def calculate_triangle_area(a: float, b: float, c: float) -> float:
    if not validate_triangle(a, b, c):
        raise ValueError("Невозможно построить треугольник с такими сторонами!")

    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def format_number(number: float) -> Union[int, float]:
    return int(number) if number.is_integer() else number


def calculate_area(figure_type: int) -> Optional[float]:
    try:
        if figure_type == 1:
            radius = get_number_input("Введите радиус круга: ")
            if radius is None:
                return None
            if radius == -1:  # Признак выхода
                return -1
            return calculate_circle_area(radius)

        elif figure_type == 2:
            sides = get_multiple_numbers("Введите стороны прямоугольника через пробел: ", 2)
            if sides is None:
                return None
            if sides[0] == -1:  # Признак выхода
                return -1
            return calculate_rectangle_area(*sides)

        elif figure_type == 3:
            sides = get_multiple_numbers("Введите стороны треугольника через пробел: ", 3)
            if sides is None:
                return None
            if sides[0] == -1:  # Признак выхода
                return -1
            return calculate_triangle_area(*sides)

        return None
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None


def main():
    figure_names = {
        1: "круга",
        2: "прямоугольника",
        3: "треугольника"
    }

    while True:
        choice = get_user_choice([1, 2, 3])

        if choice == -1:  # Признак выхода
            print("Программа завершена!")
            break

        if choice is None:
            print("Некорректный ввод! Выберите число от 1 до 3 или 'q' для выхода.")
            continue

        area = calculate_area(choice)
        if area == -1:  # Признак выхода
            print("Программа завершена!")
            break

        if area is not None:
            formatted_area = format_number(area)
            print(f"\nПлощадь {figure_names[choice]}: {formatted_area}")


if __name__ == "__main__":
    main()