import math

def solve_quadratic(a: int | float, b: int | float, c: int | float):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Уравнение имеет два корня: {root1} и {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Уравнение имеет один корень: {root}"
    else:
        return "Уравнение не имеет корней"


a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))


if a == 0:
    print("Это не квадратное уравнение, коэффициент a не должен равен нулю.")
else:
    result = solve_quadratic(a, b, c)
    print(result)
