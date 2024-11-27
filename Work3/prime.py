def is_prime(num: int) -> bool:
    if num > 1:
        for div in range(2, num // 2 + 1):
            if num % div == 0:
                return False

    return True

prime_numbers = []
predel = int(input("Введите число, до (включительно) которого будут искаться простые числа: "))
for i in range(2, predel + 1):
    if is_prime(i):
        prime_numbers.append(i)

print(f'Простые числа: {prime_numbers}')
