number = input("Введите число: ")

try:
    if '.' in number:
        reversed_number = number[::-1]
        reversed_number = float(reversed_number)
    else:
        reversed_number = number[::-1]
        reversed_number = int(reversed_number)

    print("Перевёрнутое число:", reversed_number)

except ValueError:
    print("Ошибка: введено некорректное число. Попробуйте снова.")
except Exception as e:
    print(f'Произошла ошибка: {e}')