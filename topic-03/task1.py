def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Помилка: ділення на нуль!"
    return x / y

print("Калькулятор. Для виходу введіть команду: exit")

while True:
    op = input("\nВведіть операцію (+, -, *, /): ")

    if op == "exit":
        print("Програму завершено.")
        break

    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

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