# написать программу которая:
# 1. запрашивает у пользователя логин
# 2. Есть функция, которая выводит сумму на счете
# 3. Декорируем эту функцию декоратором который проверяет если пользователь - 
#    админ (получили на первом этапе, то выводит сумму счета (выполняет функцию из п.2)
# 4. Если не админ - Сумму не выводить (функцию даже не выполнять), а выводить - доступ запрещен.

a = str(input("Введите ваш username: "))

def printing_cash:
    return ("Сумма на счете: 20000$")

def decorator(printing_cash):
    # @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
    