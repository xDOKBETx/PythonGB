''' Задание №7
Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: «число является простым, 
если делится нацело только на единицу и на себя».
'''

# Генератор простых чисел
def prime_generator(N):
    count = 0
    num = 2

    while count < N:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Проверка, является ли число простым
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


N = int(input("Введите количество простых чисел: "))

primes = prime_generator(N)

print(*primes)
