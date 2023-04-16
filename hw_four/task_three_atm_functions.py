import time
from hw_four import view

balance = 0
o_counter = 0
operations = []


def check_balance():
    global balance
    view.balance_message(balance)


def tax_charge():
    global balance
    if balance >= 5_000_000:
        view.tax_message()
        balance = round(balance * 0.9, 2)
        check_balance()
        return balance


def save_operation(data: str) -> None:
    global operations, balance
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    operations.append(f'{time_str} {data} Current balance {round(balance, 2)} y. e.')


def deposit_cash():
    global balance, o_counter
    cash = int(input())
    if multiplicity_check(cash):
        balance += cash
        d_string = f'You deposited {cash} y. e.'
        update_globals(d_string)
    else:
        view.multiplicity_message()
        deposit_cash()


def withdraw_cash():
    global balance, o_counter
    cash = int(input())
    if multiplicity_check(cash):
        if (fee(cash) + cash) <= balance:
            balance -= (fee(cash) + cash)
            w_string = f'You withdrawed {cash} y. e.'
            update_globals(w_string)
        else:
            view.check_balance_message()
            withdraw_cash()
    else:
        view.multiplicity_message()
        withdraw_cash()


def update_globals(data: str):
    global balance, o_counter
    print(data)
    view.balance_message(balance)
    o_counter += 1
    accrual()
    save_operation(data)
    return balance


def read_operations():
    global operations
    if len(operations) > 0:
        view.operations_message()
        print(*operations, sep='\n')
    else:
        view.no_operations_message()


def fee(cash):
    if cash <= 2000:
        return 30
    elif cash >= 40000:
        return 600
    else:
        return round(cash * 0.015, 2)


def accrual() -> float:
    global balance, o_counter
    if o_counter == 3:
        view.accrual_message()
        balance = round(balance * 1.03, 2)
        view.balance_message(balance)
        o_counter = 0
    return balance


def multiplicity_check(amount: int | float) -> bool:
    return True if amount % 50 == 0 else False
