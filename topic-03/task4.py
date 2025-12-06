def find_insert_position(sorted_list, value):
    for i in range(len(sorted_list)):
        if value < sorted_list[i]:
            return i
    return len(sorted_list)

# Приклад використання:
arr = [1, 3, 5, 7, 9]
print("Список:", arr)

num = 4
pos = find_insert_position(arr, num)
print(f"Елемент {num} потрібно вставити на позицію {pos}")