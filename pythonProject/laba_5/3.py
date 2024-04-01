import itertools
import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

# Функция для вычисления площади треугольника по длинам сторон
def triangle_area(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        # Полупериметр
        s = (a + b + c) / 2
        # Формула Герона для площади треугольника
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return 0

areas = []
# Собираем треугольники из минимального и максимального значений
for combo in itertools.product([min(one), max(one)], [min(two), max(two)], [min(three), max(three)]):
    a, b, c = combo
    area = triangle_area(a, b, c)
    if area != 0:
        areas.append(area)

# Выводим только минимальную и максимальную площадь
print("Минимальная площадь треугольника:", min(areas))
print("Максимальная площадь треугольника:", max(areas))
