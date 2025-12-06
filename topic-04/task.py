def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"


# Функція безпечного введення чисел
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: потрібно вводити число! Спробуйте ще раз.")


# Основний нескінченний цикл роботи калькулятора
print("Калькулятор. Для виходу введіть 'exit'.")

while True:
    op = input("\nОберіть операцію (+, -, *, /): ")

    if op == "exit":
        print("Програму завершено.")
        break

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
        print("Невідома операція! Доступні: +, -, *, /")