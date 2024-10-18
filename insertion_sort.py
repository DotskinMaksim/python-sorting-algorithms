list = [2, 41, 64, 3, 23, 75, 1, 45]
print(list)

# Сортировка вставками (Insertion Sort): Сортирует элементы по одному,
# перемещая их в правильное место относительно уже отсортированной части.


def sort_list(list):
    for i in range(1,len(list)):
        x=list[i]
        j = i
        while j >0 and list[j-1]>x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x


sort_list(list)
print(list)