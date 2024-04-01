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