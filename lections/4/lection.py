DIVISION_NUM = 5
arr = [i for i in range(10)]
res_arr = []
for i in arr:
    res_arr.append(i % 5)
print(res_arr)

d = 5
arr = [i for i in range(11)]
print(list(map(lambda x: x % d, arr)))


def fibonacci(n):
    if 0 <= n < 2:
        print(n, end=' ')
        return n
    else:
        print(n, end=' ')
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f'Число фибоначчи = {fibonacci(3)}')
print('Python есть функционал, позволяющий работать с ленивыми вычислениями')


def lazy_function():
    num = 0
    while True:
        yield num
        num += 1


lazy = lazy_function()
print(next(lazy), end=' ')
print(next(lazy), end=' ')
print(next(lazy))

print('Каррирование дробит функцию на более мелкие функции')


def add(x):
    def add_x(y2):
        return x + y2

    return add_x


print(add(2)(5))
print('Похоже на замыкание')
y = add(2)
print(add(2))
print(y(5))


def sum_squares(list_my):
    return sum(map(lambda x: x ** 2, list_my))


print(f'Сумма квадратов списка: {sum_squares([2, 2, 3])}')

print('Структурно-процедурная')


def sum_squares2(my_list):
    current_sum = 0
    for el in my_list:
        current_sum += el ** 2
    return current_sum


print(f'Сумма квадратов списка: {sum_squares2([2, 2, 3])}')

print('ООП')


class ListMy3:
    def __init__(self, list_my4):
        self.list_my4 = list_my4

    def sum_squares3(self):
        sum_my = 0
        for el in self.list_my4:
            sum_my += el ** 2
        return sum_my


my_list5 = ListMy3([2, 2, 3])
print(f'Сумма квадратов списка: {my_list5.sum_squares3()}')


def compose(f, g):
    return lambda x: f(g(x))


print(f'непонятно зачем это надо: {compose(2, 2)}')
