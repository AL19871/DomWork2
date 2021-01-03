import os

def check_password(pasww):
    def check_pass_arg(func):
        def decorated_function(*args, **kwards):
            if pasww != '123':
                return 'Не авторизован'
            value = func(*args, **kwards)
            return value
        return decorated_function
    return check_pass_arg

def func_own_data():
    return 'Лашицкий Алексей'

def func_account_number():
    return '123456789'

def func_balance():
    return '100 руб.'

os.system('cls' if os.name == 'nt' else 'clear')

b = """Пункты:
1. Личная информация о владельце счета
2. Номер счета (нужна авторизация)
3. Остаток по счету (нужна авторизация)
"""

print(b)

lst_passw = ['2','3']

while True:
    while True:
        num_ind = input("Выберите номер пункта или '0' для завершения работы c меню: ")
        if int(num_ind) >= 0 and int(num_ind) <= 3:
            break
    if num_ind == '0':
        break
    if num_ind in lst_passw:
        pass_global = input("Введите пароль: ")
        if num_ind == '2':
            func_account_number_dec = check_password(pass_global)(func_account_number)
            print(func_account_number_dec())
        else:    
            func_balance_dec = check_password(pass_global)(func_balance)
            print(func_balance_dec())
    else:
        print(func_own_data())