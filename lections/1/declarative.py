from functools import reduce

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('dec = ', sum(arr))

res = reduce(lambda x, y: x+y, arr)
print('dec2 = ', res)
