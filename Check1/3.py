from random import randint
from modules import get_names

try:
    digit = int(input('Введите величину для сравнения: '))
except ValueError:
    print('Необходимо ввести целое число!')
    exit()

random_list = [randint(1, 20) for _ in range(20)]

equal = [i for i in random_list if i == digit]
high = [i for i in random_list if i > digit]
low = [i for i in random_list if i < digit]

names = get_names(30, 10)

alph = 'АБВГДЕЁЖЗИК'
before = []
after = []

for name in names:
    if name[0] in alph:
        before.append(name)
    else:
        after.append(name)

if equal:
    print(f'Равные {digit} величины: {equal}')
if high:
    print(f'Величины больше {digit}: {high}')
if low:
    print(f'Величины меньше {digit}: {low}')

print()

print(f'Имена от А до К: {before}')
print(f'Остальные имена: {after}')
