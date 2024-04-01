# Получение предложения от пользователя
sentence = input("Введите предложение на английском: ")
# Вывод длины предложения
print("Длина предложения: ", len(sentence))
# Перевод предложения в нижний регистр
sentence_lower = sentence.lower()
print("Предложение в нижнем регистре: ", sentence_lower)
# Подсчет количества гласных
vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = sum(1 for letter in sentence_lower if letter in vowels)
print("Количество гласных в предложении: ", count_vowels)
# Замена слов "ugly" на "beauty"
sentence_replaced = sentence_lower.replace("ugly", "beauty")
print("Предложение с заменой: ", sentence_replaced)

# Проверка на начало и конец предложения
if sentence_lower.startswith("The"):
    print("Предложение начинается с 'The'")
else:
    print("Предложение не начинается с 'The'")

if sentence_lower.endswith("end"):
    print("Предложение заканчивается на 'end'")
else:
    print("Предложение не заканчивается на 'end'")