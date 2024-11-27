from functools import reduce
from statistics import mean

data = []

while True:
    user_input = input("Введите список (q - для выхода): ")

    if user_input == 'q':
        break

    for i in map(int, user_input.split()):
        data.append(i)

print(
    f"Количество элементов: {len(data)}\n"
    f"Среднее арифметическое: {mean(data)}\n"
    f"Сумма: {sum(data)}\n"
    f"Минимальное число и его индекс: {min(data)} {(min_index := data.index(min(data)))}\n"
    f"Максимальное число и его индекс: {max(data)} {(max_index := data.index(max(data)))}"
)

mul = lambda lst: reduce(lambda x, y: x * y, lst)
mul_data = mul(data[min_index + 1:max_index]) if min_index < max_index else mul(data[max_index + 1:min_index])

print(
    f"Произведение чисел между минимальным и максимальным: {mul_data}"
)
