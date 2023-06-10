'''Задание №9

Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке. 
'''

for i in range(2, 11):
    for j in range(2, 6):
        multiplication = i * j
        print(f"{j} x {i} = {multiplication:2}\t", end="")
    print()

print()

for i in range(2, 11):
    for j in range(6, 10):
        multiplication = i * j
        print(f"{j} x {i} = {multiplication:2}\t", end="")
    print()
