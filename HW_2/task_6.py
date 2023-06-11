'''Задание №6
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
'''

initial_amount = 0
balance = initial_amount
transaction_count = 0
tax_threshold = 5000000
tax_rate = 0.1

while True:
    if balance > tax_threshold:
        # Вычисление налога на богатство
        tax = balance * tax_rate
        balance -= tax
        print(f"Удержан налог на богатство в размере {tax:.2f} у.е.")

    print("Выберите действие:")
    print("1. Пополнение")
    print("2. Снятие")
    print("3. Выход")
    action = int(input("Введите номер действия: "))

    if action == 3:
        break

    if action not in [1, 2]:
        print("Неверный номер действия. Пожалуйста, выберите из списка.")
        continue

    amount = int(input("Введите сумму: "))

    if action == 1:
        if amount % 50 == 0:
            # Пополнение счета
            balance += amount

            transaction_count += 1
            if transaction_count % 3 == 0:
                # Начисление бонуса за каждую третью операцию
                bonus = balance * 0.03
                balance += bonus
                print(f"Бонус {bonus:.2f} у.е. начислен за третье действие.")
        else:
            print("Сумма пополнения должна быть кратной 50.")
    elif action == 2:
        if amount % 50 == 0:
            total_with_commission = amount + (amount * 0.015)
            if balance >= total_with_commission:
                # Снятие средств с комиссией
                commission = amount * 0.015
                commission = max(commission, 30)
                commission = min(commission, 600)
                balance -= total_with_commission
                print(f"Комиссия {commission:.2f} у.е. удержана за снятие.")

                transaction_count += 1
                if transaction_count % 3 == 0:
                    # Начисление бонуса за каждую третью операцию
                    bonus = balance * 0.03
                    balance += bonus
                    print(f"Бонус {bonus:.2f} у.е. начислен за третью операцию со счётом.")
            else:
                print("Недостаточно средств на счете для снятия с учетом комиссии.")
        else:
            print("Сумма снятия должна быть кратной 50.")

    if balance < 0:
        print("Баланс счета не может быть отрицательным. Снятие невозможно.")
        balance += total_with_commission

    print(f"Остаток на счете: {balance:.2f} у.е.")

print(f"Окончательный остаток на счете: {balance:.2f} у.е.")
