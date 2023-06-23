# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()

for _ in range(20):
    print(next(fibonacci))
