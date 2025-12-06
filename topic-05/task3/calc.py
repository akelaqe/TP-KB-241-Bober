from operations import calculate

print("Калькулятор. Для виходу введіть 'exit'.")

while True:
    cmd = input("\nНатисніть Enter для продовження або введіть exit для виходу: ")

    if cmd == "exit":
        print("Програму завершено.")
        break

    calculate()