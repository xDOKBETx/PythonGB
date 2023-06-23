''' Задание №5
Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
*Превратите решение в генераторное выражение.
'''

def fizz_buzz_generator():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            yield 'FizzBuzz'
        elif num % 3 == 0:
            yield 'Fizz'
        elif num % 5 == 0:
            yield 'Buzz'
        else:
            yield num

fizz_buzz = fizz_buzz_generator()
print(*fizz_buzz, sep='\n')
