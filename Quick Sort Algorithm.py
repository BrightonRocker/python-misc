def quick_sort(list_):
    indexing_length_ = len(list_)
    if indexing_length_ <= 1:
        return list_
    else:
        pivot = list_.pop()

    items_greater = []
    items_lower = []

    for items in list_:
        if items > pivot:
            items_greater.append(items)

        else:
            items_lower.append(items)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,6,7,8,9,8,7,6,2,3,4,5,0]))

################################################################

def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted_ = False

    while not sorted_:
        sorted_ = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted_ = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

print(bubble([4,6,8,3,2,5,7,8,9]))

################################################################

def insertion_sort(list_b):
    indexing_length_1 = range(1, len(list_b))
    for i in indexing_length_1:
        value_to_sort = list_b[i]

        while list_b[i-1] > value_to_sort and i > 0:
            list_b[i], list_b[i-1] = list_b[i-1], list_b[i]
            i = i - 1

    return list_b

print(insertion_sort([7,8,9,3,5,6,2,3,4]))


################################################################



def selection_sort(list_c):
    indexing_length_2 = range(0, len(list_c)-1)

    for i in indexing_length_2:
        min_value = i

        for j in range(i+1, len(list_c)):
            if list_c[j] < list_c[min_value]:
                min_value = j

            if min_value != i:
                list_c[min_value], list_c[i] = list_c[i], list_c[min_value]

    return list_c

print(selection_sort([6,7,8,7,6,5,4,5,6,7,6,7,8,9,7,9,0]))





################################################################



