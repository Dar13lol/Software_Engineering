# Функция для удаления двоек и замены троек на четверки
def process_grades(grades):
    filtered_grades = [grade for grade in grades if grade != 2]  # Удаляем двойки
    updated_grades = [4 if grade == 3 else grade for grade in filtered_grades]  # Заменяем тройки на четверки
    return updated_grades

# Списки оценок 
grades_lists = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
]

# Обрабатываем каждый список оценок
updated_grades_lists = [process_grades(grades) for grades in grades_lists]

# Вывод результатов
for i, updated_grades in enumerate(updated_grades_lists, 1):
    print(f"Обновленный массив {i}: {updated_grades}")
