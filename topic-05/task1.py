import random

options = ["stone", "scissor", "paper"]

print("Гра: камінь, ножиці, папір!")
print("Введіть одне з: stone, scissor, paper")

user = input("Ваш вибір: ").lower()

if user not in options:
    print("Помилка! Потрібно ввести: stone, scissor або paper")
else:
    comp = random.choice(options)
    print("Комп'ютер вибрав:", comp)

    if user == comp:
        print("Нічия!")
    elif (user == "stone" and comp == "scissor") or \
         (user == "scissor" and comp == "paper") or \
         (user == "paper" and comp == "stone"):
        print("Ви перемогли!")
    else:
        print("Ви програли!")