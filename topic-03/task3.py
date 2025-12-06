data = {"name": "Bob", "age": 25}
print("Початковий словник:", data)

data.update({"age": 30, "city": "Kyiv"})
print("update({'age':30,'city':'Kyiv'}) ->", data)

print("keys() ->", list(data.keys()))
print("values() ->", list(data.values()))
print("items() ->", list(data.items()))

del data["name"]
print("del data['name'] ->", data)

data.clear()
print("clear() ->", data)