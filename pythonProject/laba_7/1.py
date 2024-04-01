from collections import Counter
import re

# Чтение данных из файла
with open('article.txt', 'r') as file:
    data = file.read()

# Преобразование текста в список слов
words = re.findall(r'\w+', data.lower())

# Подсчет количества слов
word_count = len(words)

# Определение самого часто встречающегося слова
word_freq = Counter(words)
most_common_word = word_freq.most_common(1)[0][0]

# Вывод результатов
print(f"Количество слов в статье: {word_count}")
print(f"Самое часто встречающееся слово: {most_common_word}")
