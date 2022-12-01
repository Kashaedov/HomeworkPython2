# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,
# 10 рублевых, 3 рублевых и 1 рублевых

salary = int(input("Введи сумму зарплаты:"))
countBanknot = 0
while (salary > 0):
    if salary > 25:
        print(f'Двадцати пяти рублёвых купюр = {salary // 25} шт.')
        countBanknot += salary // 25
        salary %= 25
    elif salary >= 10:
        print(f'Десяти рублёвых купюр = {salary // 10} шт.')
        countBanknot += salary // 10
        salary %= 10
    elif salary >= 7:
        print(f'Семи рублёвых купюр = {salary // 7} шт.')
        countBanknot += salary // 7
        salary %= 7
    elif salary >= 3:
        print(f'Трех рублёвых купюр = {salary // 3} шт.')
        countBanknot += salary // 3
        salary %= 3
    else:
        print(f'Одна рублёвых купюр = {salary // 1} шт.')
        countBanknot += salary // 1
        salary %= 1
print(f'Общее минимальное количество купюр = {countBanknot} шт.')