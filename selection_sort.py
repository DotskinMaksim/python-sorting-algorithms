list = [2, 41, 64, 3, 23, 75, 1, 45]
print(list)

# Сортировка выбором (Selection Sort):
# Ищет наименьший элемент в несортированной части массива и меняет его местами с текущим элементом.


def sort_list(list):
    for i in range(len(list) - 1):
        index = i  # 0
        for j in range(i + 1, len(list)):
            if list[j] < list[index]:
                index = j

        list[i], list[index] = list[index], list[i]


sort_list(list)
print(list)