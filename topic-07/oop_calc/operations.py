class Operations:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Помилка: ділення на нуль!"