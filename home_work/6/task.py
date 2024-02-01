def binary_search(arr, number):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":

    array = [150, 254, 452, 257, 257, 25, 15]
    print(array)
    search_index = int(input("Введите искомый элемент: "))
    result = binary_search(array, search_index)
    print(f"Индекс элемента(первого найденного): {result}")
