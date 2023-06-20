'''
Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

def calculate_wealth_tax(balance, tax_rate):
    tax = balance * tax_rate
    balance -= tax
    print(f"Удержан налог на богатство в размере {tax:.2f} у.е.")
    print(f"Остаток на счете после удержания налога: {balance:.2f} у.е.")
    return balance


def replenish_balance(balance, amount, transaction_count, transaction_list):
    if amount % 50 == 0:
        balance += amount

        transaction_count += 1
        if transaction_count % 3 == 0:
            bonus = balance * 0.03
            balance += bonus
            print(f"Бонус {bonus:.2f} у.е. начислен за третье действие.")

        transaction_list.append(("Пополнение", amount))
    else:
        print("Сумма пополнения должна быть кратной 50.")
    return balance, transaction_count, transaction_list


def withdraw_balance(balance, amount, transaction_count, transaction_list):
    if amount % 50 == 0:
        commission = amount * 0.015
        commission = max(commission, 30)
        commission = min(commission, 600)
        total_with_commission = amount + commission
        if balance >= total_with_commission:
            balance -= total_with_commission
            print(f"Комиссия {commission:.2f} у.е. удержана за снятие.")

            transaction_count += 1
            if transaction_count % 3 == 0:
                bonus = balance * 0.03
                balance += bonus
                print(f"Бонус {bonus:.2f} у.е. начислен за третью операцию со счётом.")

            transaction_list.append(("Снятие", amount))
        else:
            print("Недостаточно средств на счете для снятия с учетом комиссии.")
    else:
        print("Сумма снятия должна быть кратной 50.")
    return balance, transaction_count, transaction_list


def main():
    initial_amount = 0
    balance = initial_amount
    transaction_count = 0
    tax_threshold = 5000000
    tax_rate = 0.1
    transaction_list = []

    while True:
        if balance > tax_threshold:
            balance = calculate_wealth_tax(balance, tax_rate)

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
            balance, transaction_count, transaction_list = replenish_balance(balance, amount, transaction_count, transaction_list)
        elif action == 2:
            balance, transaction_count, transaction_list = withdraw_balance(balance, amount, transaction_count, transaction_list)

        if balance < 0:
            print("Баланс счета не может быть отрицательным. Снятие невозможно.")
            balance += total_with_commission

        print(f"Остаток на счете: {balance:.2f} у.е.")

    print(f"Окончательный остаток на счете: {balance:.2f} у.е.")
    print("Список операций:")
    for transaction in transaction_list:
        print(f"{transaction[0]}: {transaction[1]} у.е.")


main()
