def sum_in_str(text: str) -> int:
    digits = []

    for i in text:
        if i.isdigit():
            digits.append(int(i))

    return sum(digits)

data = input('Введите строку с цифрами и числами для получения суммы: ')
print(sum_in_str(data))
