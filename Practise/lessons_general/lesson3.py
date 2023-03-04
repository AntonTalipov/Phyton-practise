# ФУНКЦИИ
from modul_3lesson import *


# def sumNumbers(n, y='Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa+=i
#     return summa
#     print('stop')
# print(sumNumbers(5))
# def sumNumbers(n, y='Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
#     print('stop')
# print(sumNumbers(5, 'qwerty'))


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
#
#
# print(sum_str('q', 'w', 'e', 'r'))
#
# print(max1(15, 9))


# Рекурсия

# def fib(n):
#     if n in [1,2]:
#         return n
#     return fib(n-1)+ fib(n-2)
# list_1=[]
# for i in range (1,9):
#     list_1.append(fib(i))
# print(list_1)

# Быстрая сортировка

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([2, 34, 5, 2, 4, 5, 67, 34, 54, 7, 9]))


# Сортировка слияния
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list1 = [1, 4, 5, 4, 3, 3, 3, 3, 65, 2, 34, 5, 4, 86]
merge_sort(list1)
print(list1)
