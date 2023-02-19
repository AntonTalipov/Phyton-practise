# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def fibo(w):
    if w > 1:
        n = 1
        sum1 = 0
        sum2 = 1
        a = [0, 1]
        while n <= w:
            sum = sum1 + sum2
            a.append(sum)
            sum1 = sum2
            sum2 = sum
            n += 1
            if a[n] == w:
                print("Your position in fibo line is:", n + 1)
                break
            if w > a[n-1] and w < a[n]:
                print(-1)
                break
        print(a)
    else:
        print("Type a number more than 1")
fibo(int(input("type a number: \n")))
