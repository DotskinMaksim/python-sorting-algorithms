list = [2, 41, 64, 3, 23, 75, 1, 45]
print(list)

# Пузырьковая сортировка (Bubble Sort): Сравнивает соседние элементы и меняет их местами,
# если они находятся в неправильном порядке. Повторяет процесс, пока не будет отсортировано.

def sort_list(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]


sort_list(list)
print(list)