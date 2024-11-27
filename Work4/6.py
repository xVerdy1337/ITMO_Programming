def cyclic_shift(numbers: list[int], step: int) -> list[int]:
    return numbers[-step % len(numbers):] + numbers[:-step % len(numbers)]
ё
try:
    choose = input('Введите 1 или 2. \n1 - входные данные: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n2 - ваши входные данные\n')

    if choose == '1':
        numbers = [i for i in range(2, 21 , 2)]
    elif choose == '2':
        numbers = list(map(int, input('Вводите числа через пробел: ').split()))
    else:
        print('Необходимо ввести 1 или 2!!!')
        exit()

    step = int(input("Введите величину сдвига: "))

    shifted_numbers = cyclic_shift(numbers, step)

    print("Изначальный список:", numbers)
    print("Список после циклического сдвига:", shifted_numbers)

except ValueError:
    print("Пожалуйста, введите корректные целые числа.")
