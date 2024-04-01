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
