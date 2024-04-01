"""Документ «text_for_laba.txt» содержит некоторый текст
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину
(или список слов, если таковых несколько)"""

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