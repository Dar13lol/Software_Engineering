# Тема 4. Функции и стандартные модули/библиотеки
Отчет по Теме #4 выполнил(а):
- Антохина Дарья Сергеевна
- ИНО ЗБ ПОАС-22-1

| Задание |  Сам_раб |
| ------ |  ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + | 
| Задание 4 | + | 
| Задание 5 | + |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Дайте подробный комментарий для кода

```python
# Импорт используемых модулей
from datetime import datetime
from math import sqrt
# Основная функция, которая принимает кол-во ключевых аргументов
def main(**kwargs):
    # Итерация по всем переданным аргументам
    for key in kwargs.items():
        # Расчет результата по формуле
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Вывод результата
        print(result)
# условие:
if __name__ == '__main__':
    # Засечение времени начала выполнения программы
    starttime = datetime.now()

    # Вызов функции main с передачей ключевых аргументов
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    # Вычисление времени выполнения программы
    timecosts = datetime.now() - starttime
    # Вывод времени выполнения
    print(f"Program execution time {timecosts}")
```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_4/png_4/1.png).


## Выводы

Все условия задания выполнены!

## Самостоятельная работа №2
### Напишите программу, которая будет заменять игральную кость с 6 гранями.

```python
import random

def rolldice():
    dicevalue = random.randint(1, 6)
    print(f'Кубик: {dicevalue}')

    if dicevalue == 5 or dicevalue == 6:
        print('Вы победили')
    elif dicevalue == 3 or dicevalue == 4:
        rolldice()
    else:
        print('Вы проиграли')

if __name__ == '__main__':
    rolldice()  
```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_4/png_4/2.png).

## Выводы

Все условия задания выполнены!
  
## Самостоятельная работа №3
### Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд.

```python
import datetime
import time

for _ in range(5):
    current_time = datetime.datetime.now()
    print(f"Текущее время: {current_time.strftime('%H:%M:%S')}")
    time.sleep(1)

current_time = datetime.datetime.now()
print(f"Финальное время: {current_time.strftime('%H:%M:%S')}") 
```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_4/png_4/3.png).

## Выводы

Все условия задания выполнены!

## Самостоятельная работа №4
### Напишите программу, которая считает среднее арифметическое от аргументов вызываемое функции, с условием того, что изначальное количество этих аргументов неизвестно.

```python
def calculate_average(*args):
    if len(args) == 0:
        return 0
    else:
        total = sum(args)
        return total / len(args)

if __name__ == '__main__':
    values = [13, 7, 5, 11, 9]  # Пример входных значений
    avg = calculate_average(*values)
    print(f'Среднее арифметическое: {avg}')
```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_4/png_4/4.png).

## Выводы

Все условия задания выполнены!
  
## Самостоятельная работа №5
### Создайте два Python файла, в одном будет выполняться вычисление площади треугольника при помощи формулы Герона (необходимо реализовать через функцию), а во втором будет происходить взаимодействие с пользователем (получение всей необходимой информации и вывод результатов).

```python

from document import calculate_area

def get_user_input():
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c

if __name__ == '__main__':
    print("Вычисление площади треугольника по формуле Герона.")
    a, b, c = get_user_input()
    area = calculate_area(a, b, c)
    print(f"Площадь треугольника с сторонами {a}, {b}, {c} равна: {area}")


```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_4/png_4/5.png).

## Выводы
  
Все условия задания выполнены!

## Общие выводы по теме
Функции и модули в Python предоставляют эффективные средства организации кода, повторного использования и управления сложными программами.
