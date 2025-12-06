from functions import add, sub, mul, div

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
        print("Результат:", add(a, b))
    elif op == "-":
        print("Результат:", sub(a, b))
    elif op == "*":
        print("Результат:", mul(a, b))
    elif op == "/":
        print("Результат:", div(a, b))
    else:
        print("Невідома операція!")