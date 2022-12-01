# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

x = int(input("Введите целое число X:"))
i = 0
firstMax = 0
secondMax = 0
print(f"Введите {x} раз числа(о). ")
while i < x:
    numb = float(input("Введите число:", ))
    if i == 0:
        firstMax = numb
    if numb > firstMax:
        secondMax = firstMax
        firstMax = numb
    i += 1
print(f"Первое максимальное число: {firstMax}")
print(f"Второе максимальное число: {secondMax}")