my_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7]


def count_in_list(array, numbers):
    count = 0
    for i in array:
        if i == numbers:
            count += 1
    return f'quantity {numbers} in list = {count}'


print(count_in_list(my_list, 1))

my_list2 = [7, 5, 3, 9, 1, 2, 6, 4, 8, 0, 10]


def buble_sort(array2):
    len_array = len(array2)
    for i in range(len_array):
        for k in range(len_array - i - 1):
            if array2[k] < array2[k + 1]:
                array2[k], array2[k + 1] = array2[k + 1], array2[k]
    return array2


print(f'sort: {buble_sort(my_list2)}')
