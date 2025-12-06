from functions import add, sub, mul, div
from datetime import datetime


def log(action, x, y, result):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} | {x} {action} {y} = {result}\n")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: потрібно вводити число!")


def calculate():
    print("Операції: +, -, *, /")
    op = input("Введіть операцію: ")

    a = get_number("Введіть перше число: ")
    b = get_number("Введіть друге число: ")

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Невідома операція!")
        return

    print("Результат:", result)
    log(op, a, b, result) 