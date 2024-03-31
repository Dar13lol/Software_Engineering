# Тема 8. Введение в ООП.
Отчет по Теме #8 выполнил(а):
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
### Самостоятельно создайте класс и его объект.

```python
class Animals: #класс
    def __init__(self,year):
        self.year=year
duck = Animals(3) #объект

```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_8/png_8/1.png).


## Выводы

Все условия задания выполнены!

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса.

```python
class Animals:
    def __init__(self,year,color):
        self.year=year
        self.color=color
duck = Animals(3,"black")
print(duck.year)
print(duck.color)
```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_8/png_8/2.png).

## Выводы

Все условия задания выполнены!
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать ранее созданным классом. 

```python

class Animals:
    def __init__(self,name):
        self.name=name

class Duck(Animals): ##наследование класса Animals
    def eat(self):
        print(f"{self.name} eats")

duck = Animals("KEVIN")
print(duck.name)


```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_8/png_8/3.png).

## Выводы

Все условия задания выполнены!
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию

```python
class Animals:
    def __init__(self, name, years):
        self._name = name  # имя
        self._years = years  # возраст


    def eat(self):
        print(f" {self._name} is eating, he is {self._years} years old")

duck = Animals("KEVIN", 3)
print(duck._name)
duck.eat()

```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_8/png_8/4.png).

## Выводы

Все условия задания выполнены!
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. 


```python
class Animals:
    def area(self):
        pass
class Duck(Animals):  ##наследование класса Animals
    def __init__(self, name, years):
        self.name = name  # имя
        self.years = years  # возраст
duck = Duck("Donald", 5)

print("Duck name:", duck.name)
print("Duck age:", duck.years)

class Cat(Animals):  ##наследование класса Animals
    def __init__(self, color):
        self.color = color  # цвет

cat = Cat("White")
print("Cat color:", cat.color)

```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_8/png_8/5.png).

## Выводы

Все условия задания выполнены!
  


## Общие выводы по теме
ООП предоставляет набор концепций и методологий, позволяющих описывать, моделировать и взаимодействовать с объектами в программе.
