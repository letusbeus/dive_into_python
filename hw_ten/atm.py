import view

class atm:
    bank_account = 0
    count = 0
    start = 0
    operations = []

    def __init__(self, money: int | float = 0):
        self.money = money

    def operation_logs(self, val: int | float):
        self.operations.append(val)
    def add_money(self, money: int | float):
        while not money % 50 == 0:
            # view.multiplicity_message()
            money = int(input())
        self.operation_logs(self.bank_account + money)
        self.bank_account += money

    def get_money(self, money: int | float):
        while not money % 50 == 0:
            view.multiplicity_message()
            money = int(input())
        if money <= 2_000:
            self.bank_account -= (money + 30)
            self.operation_logs(-self.bank_account)
        elif 2_001 <= money <= 40_000:
            self.bank_account -= money * 1.015
            self.operation_logs(-self.bank_account)
        else:
            self.bank_account -= (money + 600)
            self.operation_logs(self.bank_account)

    # Выход из программы
    @staticmethod
    def bank_exit():
        return view.goodbye()

    # Распечатать баланс счета
    def print_bank(self):
        """
        Выводит информацию о счете в банкомате
        :return: str
        """
        return f'На вашем счете: {self.bank_account} руб.'

    # Проверка и списание налога на богатство (10%)
    def check_bank(self):
        """
        Проверка налога на богатство при сумме на счете более 5 млн. (10%)
        :return: None
        """
        if self.bank_account >= 5_000_000:
            self.bank_account = self.bank_account * 0.90
            return self.bank_account, f'С Вас вычли 10% налога на богатство, баланс счета: {self.bank_account}'
        else:
            return self.bank_account, None

    # Проверка корректности ввода
    def check_input_value(self, val: str, flag=0) -> int:
        """
        Проверка корректности ввода данных
        :param val: int|float
        :param flag: int
        :return: int
        """
        while isinstance(val, (int | float)):
            val = input('Банкомат принимает только Целые числа и числа с плавающей точкой, введите снова!\n'
                        '|--->: ')
        if flag == 1:
            while self.bank_account - int(val) < 0:
                val = input(f'У вас недостаточно денег для снятия! в банке {self.bank_account}!\n'
                            '|--->: ')
        return int(val)

    # Счетчик операций и начисление процентов на остаток
    def count_checker(self, count_cur):
        """
        Счетчик операций и начисление процентов на остаток
        :param count_cur: int
        :return: None
        """
        if count_cur < 2:
            self.count += 1
            return self.count, self.bank_account
        if count_cur >= 2:
            self.count = 0
            self.bank_account = self.bank_account * 1.03
            return self.bank_account, self.bank_account, f'Начислены проценты!) Баланс счета: {self.bank_account}'

    def show_log(self):
        """
        Выводит лог операций по счету
        :return:
        """

        if len(self.operations) > 0:
            info = ''
            for idx, operation in enumerate(self.operations, 1):
                if operation > 0:
                    info += f'{idx:4}. Enrollment {operation} y.e.\n'
                elif operation < 0:
                    info += f'{idx:4}. Withdrawal {operation} y.e.\n'
                else:
                    continue
            return view.operations_message() + info
        else:
            return view.no_operations_message()

    # match/case пользовательского ввода
    @staticmethod
    def user_choice(value: int):
        """
        'match/case' - выборы пользователя
        :param value: int
        :return: str
        """
        match value:
            case 1:
                return 'Пополнить счет'
            case 2:
                return 'Снять деньги со счета'
            case 3:
                return 'Проверить счет'
            case 4:
                return 'Выйти'
            case 5:
                return 'Посмотреть Лог операций'

    # match/case работы программы ввода
    def start_bank(self, value: str):
        """
        'match/case' - пользовательских выборов
        :param value: str
        :return: int|float
        """
        match value:
            case 'Пополнить счет':
                print(view.multiplicity_message())
                money = self.check_input_value(input())
                return self.add_money(money)
            case 'Снять деньги со счета':
                money = self.check_input_value(input('Введите сумму для снятия: '), 1)
                return self.get_money(money)
            case 'Проверить счет':
                return self.print_bank()
            case 'Выйти':
                return self.bank_exit()
            case 'Посмотреть Лог операций':
                return self.show_log()
