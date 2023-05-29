from atm import atm
from view import task_animal_farm, task_cashier, task_cashier_desc
from animals import Animal, Bird, Dog, Cat, Fish, Horse
from animal_farm import AnimalFarm

if __name__ == "__main__":
    # task_animal_farm()
    # vanda = AnimalFarm.create_animal(Fish, name='Vanda', age=5, color='Rainbow')
    # carl = AnimalFarm.create_animal(Bird, name='Carl', age=8, color='Black', voice='CRAW!')
    # fido = AnimalFarm.create_animal(Dog, name='Fido', age=5, voice='Woof!', fur='Pale, long')
    # tom = AnimalFarm.create_animal(Cat, name='Tom', age=2, fur='brown', voice='meow!')
    # starlight = AnimalFarm.create_animal(Horse, name='starlight', age=7, hair='blond', voice='Ghrrr')
    # print(vanda.get_info())
    # print(fido.get_info())
    # print(tom.get_info())
    # print(starlight.get_info())
    # print(carl.get_info())

    task_cashier()
    task_cashier_desc()
    my_bank = atm(0)

    while True:
        start = int(input(f'{"Добро пожаловать в банк"}\n'
                          f'{"Вы в меню"}\n'
                          f'{"Введите цифру желаемой услуги"}\n'
                          f'1 - Пополнить счет\n'
                          f'2 - Снять деньги со счета\n'
                          f'3 - Вывести текущий баланс\n'
                          f'4 - Выйти из банкомата\n'
                          f'5 - Посмотреть Лог операций\n'
                          f'Вводить сюда ---->: '))
        my_bank.bank_account, *_ = my_bank.check_bank()
        if _[0]:
            print(_[0])
        result = my_bank.start_bank(my_bank.user_choice(start))
        if start == 4:
            print(result)
            quit()
        elif start == 1 or start == 2:
            bank_account = result
            count, *_ = my_bank.count_checker(my_bank.count)
            if _:
                print(_[0])
        else:
            print(result)
