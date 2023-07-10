'''
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.
'''


def param(count):
    """
    Декоратор с параметром, определяющим количество запусков декорируемой функции.

    Args:
        count (int): Количество запусков.

    Returns:
        function: Декоратор.
    """
    def deco(func):
        """
        Внутренний декоратор, оборачивающий функцию.

        Args:
            func (function): Декорируемая функция.

        Returns:
            function: Обернутая функция.
        """
        res_list = []

        def wrapper(*args):
            """
            Обернутая функция, выполняющая декорированную функцию указанное количество раз.

            Args:
                *args: Аргументы декорированной функции.

            """
            nonlocal res_list
            for _ in range(count):
                res_list.append(func(*args))
            print(res_list)

        return wrapper

    return deco


@param(count=5)
def my_func(*args):
    """
    Функция, принимающая переменное количество аргументов.

    Args:
        *args: Аргументы функции.

    Returns:
        tuple: Кортеж с переданными аргументами.
    """
    return args


if __name__ == '__main__':
    my_func('Hello world')
