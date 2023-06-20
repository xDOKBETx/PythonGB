''' Задания №5
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
'''


def calculate_bonus(names, rates, bonuses):
    bonus_dict = {}
    for name, rate, bonus in zip(names, rates, bonuses):
        # Преобразуем процент премии в десятичное значение
        bonus_percent = float(bonus.rstrip('%')) / 100
        # Рассчитываем сумму премии
        bonus_amount = rate * bonus_percent
        # Добавляем пару ключ-значение в словарь
        bonus_dict[name] = bonus_amount
    return bonus_dict


names = ['Алексей', 'Дмитрий', 'Михаил']
rates = [10000, 20000, 15000]
bonuses = ['10.25%', '15%', '12.5%']

result_dict = calculate_bonus(names, rates, bonuses)
print(result_dict)
