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
