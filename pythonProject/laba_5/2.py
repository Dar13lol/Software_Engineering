results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

# Три лучших результата
top_3_results = sorted(results)[:3]

# Три худших результата
bottom_3_results = sorted(results)[-3:]

# Все результаты, начиная с 10
results_from_10 = [result for result in results if result >= 10]

# Вывод результатов
print("Три лучших результата: ", top_3_results)
print("Три худших результата: ", bottom_3_results)
print("Все результаты, начиная с 10: ", results_from_10 [9:])
