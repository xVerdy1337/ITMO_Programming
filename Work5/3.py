from typing import Union, Optional, Tuple

def get_numbers() -> Optional[Tuple[float, float]]:
    try:
        value = input('Введите первое и второе число (через пробел или "q" для выхода): ')
        if value.lower() == 'q':
            return None

        numbers = value.split()
        if len(numbers) != 2:
            print("Требуется ввести два числа через пробел!")
            return None

        return float(numbers[0]), float(numbers[1])
    except ValueError:
        print("Ошибка: введите корректные числа!")
        return None


def get_operation() -> Optional[str]:
    operations = {'+', '-', '*', '/'}
    value = input('Введите действие (+, -, *, /) или "q" для выхода: ')

    if value.lower() == 'q':
        return None

    if value not in operations:
        print("Ошибка: неверная операция!")
        return None

    return value


def calculate_expression(first_digit: float, second_digit: float, operation: str) -> Union[float, str]:
    try:
        if operation == '+':
            return plus(first_digit, second_digit)
        elif operation == '-':
            return minus(first_digit, second_digit)
        elif operation == '*':
            return multi(first_digit, second_digit)
        elif operation == '/':
            if second_digit == 0:
                return 'Ошибка: деление на ноль невозможно!'
            return division(first_digit, second_digit)
        else:
            return 'Ошибка: операция не существует!'
    except Exception as e:
        return f'Ошибка вычисления: {str(e)}'

def plus(first_digit: float, second_digit: float):
    return first_digit + second_digit

def minus(first_digit: float, second_digit: float):
    return first_digit - second_digit

def multi(first_digit: float, second_digit: float):
    return first_digit * second_digit

def division(first_digit: float, second_digit: float):
    return first_digit / second_digit

def format_number(number: float) -> Union[int, float]:
    return int(number) if number.is_integer() else number


def main():
    print("Калькулятор запущен! Для выхода введите 'q' в любой момент.")

    while True:
        # Получаем числа
        numbers = get_numbers()
        if numbers is None:
            if numbers is None:
                print("Программа завершена!")
                break
            continue

        # Получаем операцию
        operation = get_operation()
        if operation is None:
            print("Программа завершена!")
            break

        # Вычисляем результат
        result = calculate_expression(numbers[0], numbers[1], operation)

        if isinstance(result, str):
            print(result)
        else:
            # Форматируем и выводим результат
            formatted_result = format_number(result)
            print(f"Результат: {format_number(numbers[0])} {operation} {format_number(numbers[1])} = {formatted_result}")


if __name__ == "__main__":
    main()