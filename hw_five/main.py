from os.path import abspath

import task_one, task_two, task_three

user_file = abspath(__file__)  # здесь можно задать абсолютный путь либо использовать значение по умолчанию
print(task_one.split_path(user_file))

names = ['John', 'Adam', 'Ivan']
salaries = [15000, 20000, 25000]
bonuses = ['10.0%', '7.25%', '5%']
print(task_two.bonus_calc(names, salaries, bonuses))

task_three.gen_fib(15)
