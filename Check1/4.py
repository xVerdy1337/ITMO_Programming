from modules import load_data, save_data

data = load_data('databases/numbers.json')
nums = list(map(float, input('Введите вещественные числа: ').split()))

nums = [round(num * 1.12, 2) if num < 10 else round(num * 0.25, 2) if num > 10 else num for num in nums]

nums.sort()
print(f'Результат: {nums}')

new_data = data + nums

print(f'Сохранены следующие числа: {new_data}')
save_data('databases/numbers.json', new_data)
