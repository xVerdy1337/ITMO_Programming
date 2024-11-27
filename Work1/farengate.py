def from_farengate_to_celc(temp_farengate: int) -> float:
    return (temp_farengate - 32) / 1.8

print(from_farengate_to_celc(59))

try:
    temp_farengate = int(input('Введите градусы Фаренгейта\n'))
    print(f'{temp_farengate}°F -> {from_farengate_to_celc(temp_farengate)}°C')
except ValueError:
    print('Введите число, а не строку!')

