from hw_four.task_three_atm_functions import *
from hw_four import view

menu = {
    '1': check_balance,
    '2': deposit_cash,
    '3': withdraw_cash,
    '4': read_operations,
    '5': exit
}


def atm():
    view.task_three()
    view.welcome()
    while True:
        view.menu_commands()
        program = input()
        try:
            program = menu[program]
            if program == exit:
                view.goodbye()
                exit(0)
            elif program == check_balance:
                check_balance()
            elif program == deposit_cash:
                tax_charge()
                view.deposit_message()
                deposit_cash()
            elif program == withdraw_cash:
                tax_charge()
                view.withdraw_message()
                withdraw_cash()
            elif program == read_operations:
                read_operations()
        except KeyError:
            view.menu_error()
