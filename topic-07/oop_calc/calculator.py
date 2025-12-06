from operations import Operations

class Calculator:
    def __init__(self):
        self.ops = Operations()

    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Помилка: потрібно вводити число!")

    def run(self):
        print("Калькулятор (ООП). Для виходу введіть 'exit'.")

        while True:
            op = input("\nОберіть операцію (+, -, *, /): ")

            if op == "exit":
                print("🔚 Програму завершено.")
                break

            a = self.get_number("Введіть перше число: ")
            b = self.get_number("Введіть друге число: ")

            result = None
            if op == "+":
                result = self.ops.add(a, b)
            elif op == "-":
                result = self.ops.sub(a, b)
            elif op == "*":
                result = self.ops.mul(a, b)
            elif op == "/":
                result = self.ops.div(a, b)
            else:
                print("Невідома операція!")
                continue

            print("Результат:", result)