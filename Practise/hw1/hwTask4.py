# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("enter the number of slices by length: \n"))
m = int(input("enter the number of slices by width: \n"))
k = int(input("number of slices: \n"))
if k>=n and k%n==0 or k>=m and k%m==0:
    print("yes")
else:
    print("no")

