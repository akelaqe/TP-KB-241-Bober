import requests

allowed = ["EUR", "USD", "PLN"]

print("Конвертер валют (у гривню) за курсом НБУ")
print("Доступні валюти: EUR, USD, PLN")

currency = input("Введіть валюту: ").upper()

if currency not in allowed:
    print("Помилка! Доступні тільки EUR, USD, PLN")
else:
    amount = float(input("Введіть кількість: "))

    response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    rate_list = response.json()

    rate = None
    for item in rate_list:
        if item["cc"] == currency:
            rate = item["rate"]
            break

    if rate:
        print(f"{amount} {currency} = {amount * rate} грн за курсом НБУ")