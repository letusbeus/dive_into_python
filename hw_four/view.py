def task_one(given_list):
    print('1. Напишите функцию для транспонирования матрицы.\n'
          'Original matrix:', given_list)


def task_one_result(given_list):
    print('Transposed matrix: ', given_list, sep='')


def task_two():
    print('2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, '
          'где ключ — значение переданного аргумента, а значение — имя аргумента.\n'
          'Если ключ не хешируем, используйте его строковое представление.')


def task_three():
    print('3. Возьмите задачу о банкомате из семинара 2. '
          'Разбейте её на отдельные операции — функции.\n'
          'Дополнительно сохраняйте все операции поступления и снятия средств в список.\n')


def welcome():
    print('Welcome to the main menu.\nPlease select an operation: ')


def goodbye():
    print('Goodbye!')


def menu_commands():
    print('1 - Check balance\n2 - Deposit cash\n3 - Withdraw cash\n4 - Read operations\n5 - Exit', end='\n')


def menu_error():
    print('Incorrect operation. Please check your input and try again: ')


def balance_message(data):
    print(f'Your account balance: {data} y. e.')


def deposit_message():
    print('How much do you want to deposit? ')


def withdraw_message():
    print('How much do you want to withdraw? ')


def operations_message():
    print('Your operations:')


def no_operations_message():
    print('No activity in current session.')


def accrual_message():
    print('3% accrued on the balance. ', end='')


def check_balance_message():
    print('There are not enough funds on the account to withdraw')


def multiplicity_message():
    print('Enter an amount that is a multiple of 50: ')


def tax_message():
    print('Luxury tax 10 % has been collected.')
