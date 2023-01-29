"""За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами..
Input:
n = 700
m = 750
Output:2"""
n=int(input("distance per day: \n")) #distance per day
m=int(input("all distance: \n")) #all distance
print(-(-m//n))



