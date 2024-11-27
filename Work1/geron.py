from math import sqrt

def form_geron(a: int, b: int, c: int) -> float | int:
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        return "Треугольника с такими сторонами не существует."

    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

try:
    a, b, c = map(int, input('Введите a, b, c\n').split())
except Exception as e:
    print(f'Произошла ошибка: {e}')

print(form_geron(a, b, c))
