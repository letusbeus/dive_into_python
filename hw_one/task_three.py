"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""


def guess_the_number():
    from random import randint

    lower_limit = 0
    upper_limit = 1000
    max_tries = 10
    num = randint(lower_limit, upper_limit)
    tries = 0

    print(f"Угадайте число от {lower_limit} до {upper_limit} за {max_tries} попыток.")

    while tries < max_tries:
        guess = int(input("Попробуйте угадать число: "))
        tries += 1
        if guess < num:
            print("Загаданное число больше")
        elif guess > num:
            print("Загаданное число меньше")
        else:
            print(f"Поздравляем, вы угадали число {num} за {tries} попыток!")
            break
    else:
        print(f"К сожалению, вы не угадали число {num} за {max_tries} попыток. Попробуйте ещё раз.")
