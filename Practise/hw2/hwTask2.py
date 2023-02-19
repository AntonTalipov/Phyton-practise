# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

summa = int(input('Type the summ of numbers: \n'))
product = int(input('Type the product of numbers: \n'))
n1 = 1
while n1 < product:
    n2 = summa - n1
    if summa == n1 + n2 and product == n2 * n1:
        print('your numbers is:', n1, n2)
        break
    n1 += 1
