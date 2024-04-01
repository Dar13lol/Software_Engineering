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
