# Тема 7. Работа с файлами (ввод, вывод).
Отчет по Теме #7 выполнил(а):
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), 

```python
# Функция для преобразования чисел в множество с учетом правила
def process_numbers(numbers):
    result_set = set()
    for number in numbers:
        count = numbers.count(number)
        new_entry = str(number) * count
        result_set.add(new_entry)
        result_set.add(number)
    return result_set

# Списки натуральных чисел
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

# Обработка каждого списка и вывод результатов
result_1 = process_numbers(list_1)
result_2 = process_numbers(list_2)
result_3 = process_numbers(list_3)

print(result_1)
print(result_2)
print(result_3)

```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_7/png_7/1.png).


## Выводы

В данном коде выводятся строка с использованием функции `print()`.  Строка содержит неравество

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов,

```python
def add_expense(date, category, amount):
    with open('expenses.txt', 'a') as file:
        file.write(f"{date},{category},{amount}\n")
    print("Расход успешно добавлен.")


def display_expenses():
    with open('expenses.txt', 'r') as file:
        for line in file:
            print(line.strip())


# Создание файла для хранения расходов, если его нет
open('expenses.txt', 'a').close()

while True:
    print("1. Добавить расход")
    print("2. Вывести все расходы")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        date = input("Введите дату расхода: ")
        category = input("Введите категорию расхода: ")
        amount = input("Введите сумму расхода: ")

        add_expense(date, category, amount)

    elif choice == '2':
        print("Существующие расходы:")
        display_expenses()

    elif choice == '3':
        break

```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_7/png_7/2.png).

## Выводы

В данном коде выводятся строка с использованием функции `print()`.  Строка содержит переменные, которым были присвоены значения
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. 

```python
def count_statistics(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

        # Подсчет количества букв латинского алфавита
        letters_count = sum(1 for char in text if char.isalpha() and char.isascii())

        # Подсчет числа слов
        words_count = len(text.split())

        # Подсчет числа строк
        lines_count = text.count('\n') + 1  # Добавляем 1, т.к. последняя строка может быть без \n

        print(f"Input file contains: \n {letters_count} letters,\n {words_count} words, \n {lines_count} lines.")


file_path = 'input.txt'
count_statistics(file_path)

```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_7/png_7/3.png).

## Выводы

В данном коде вводится переменная а  с использованием типа данных `int`.  Строка содержит пользовательский ввод input
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал

```python
def censor_sentence(sentence, banned_words):
    censored_sentence = sentence
    for word in banned_words:
        censored_sentence = censored_sentence.replace(word, '*' * len(word))
        censored_sentence = censored_sentence.replace(word.capitalize(), '*' * len(word))
        censored_sentence = censored_sentence.replace(word.upper(), '*' * len(word))
        censored_sentence = censored_sentence.replace(word.lower(), '*' * len(word))
    return censored_sentence

with open('input.txt', 'r') as file:
    banned_words = file.read().split()

input_sentence = input("Введите предложение: ")
censored_output = censor_sentence(input_sentence, banned_words)
print(censored_output)
```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_7/png_7/4.png).

## Выводы

В данном коде выводятся строка с использованием функции `print()`.  Строка содержит слово
  
## Самостоятельная работа №5
### Документ «text_for_laba.txt» содержит некоторый текст


```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words
print(longest_words('text_for_laba.txt'))

```
### Результат.
![Меню](https://github.com/Dar13lol/Software_Engineering/blob/Laba_7/png_7/5.png).

## Выводы

В данном коде вводится переменные day, month, year.  Выводятся строка с использованием функции `print()`, она выводит строку f в формате.
  


## Общие выводы по теме
Функция print() в языке Python используется для вывода информации на консоль. Она является одним из основных способов коммуникации программы с пользователем. 
