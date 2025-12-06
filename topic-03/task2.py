arr = [1, 3, 5]
print("Початковий список:", arr)

arr.append(7)
print("append(7) ->", arr)

arr.extend([9, 11])
print("extend([9,11]) ->", arr)

arr.insert(1, 2)
print("insert(1,2) ->", arr)

arr.remove(3)
print("remove(3) ->", arr)

copy_list = arr.copy()
print("copy() ->", copy_list)

arr.sort()
print("sort() ->", arr)

arr.reverse()
print("reverse() ->", arr)

arr.clear()
print("clear() ->", arr)