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

print("Операції: +, -, *, /")
op = input("Введіть операцію: ")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

match op:
    case "+":
        print("Результат:", add(a, b))
    case "-":
        print("Результат:", sub(a, b))
    case "*":
        print("Результат:", mul(a, b))
    case "/":
        print("Результат:", div(a, b))
    case _:
        print("Невідома операція!")