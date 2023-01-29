# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no



# print("type a bill number")
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# f=int(input())
# if (a+b+c)==(d+e+f):
#     print("You bill",a,b,c,d,e,f,"is happy")
# else:
#     print("Sorry, it`s not a happy bill")


print("type numbers of your bill:")
a = [int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
if (a[0] + a[1] + a[2] + a[3] + a[4] + a[5]) > 36:
    print("incorrect number")
else:
    if (a[0] + a[1] + a[2]) == (a[3] + a[4] + a[5]):
        print("Congratulations! It`s a happy bill")
    else:
        print("This bill isn`t happy")
