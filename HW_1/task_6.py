''' Задание №6

Напишите программу, которая запрашивает год и проверяет его на високосность. 
Распишите все возможные проверки в цепочке elif. 
Откажитесь от магических чисел.
Обязательно учтите год ввода Григорианского календаря.
В коде должны быть один input и один print 
'''


year = int(input("Введите год: "))

if year < 0:
    print("Год должен быть положительным числом")
elif year < 1582:
    if year % 4 == 0:
        print(f"{year} год - високосный (по Юлианскому календарю)")
    else:
        print(f"{year} год - невисокосный (по Юлианскому календарю)")
elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} год - високосный (по Григорианскому календарю)")
else:
    print(f"{year} год - невисокосный (по Григорианскому календарю)")
