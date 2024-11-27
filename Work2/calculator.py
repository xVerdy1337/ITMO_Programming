def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /, **): ")
        num2 = float(input("Введите второе число: "))

        if num1.is_integer():
            num1 = int(num1)
        if num2.is_integer():
            num2 = int(num2)

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2

        else:
            return "Ошибка: недопустимая операция!"

        if result.is_integer():
            result = int(result)

        return f"{num1} {operation} {num2} = {result}"
    except ValueError:
        return "Введите число!"
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    except Exception as e:
        return f"Произошла ошибка: {e}"

print(calculator())
