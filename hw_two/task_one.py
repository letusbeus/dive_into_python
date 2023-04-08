"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def check_user_input():
    welcome_message()
    while True:
        user_number = input()
        if user_number.isdigit():
            user_number = int(user_number)
            return user_number
        else:
            warning_message()


def convert_to_hex():
    num_to_be_converted = check_user_input()
    num_to_check = num_to_be_converted
    hex_string = ""
    while True:
        hex_string += "0123456789abcdef"[num_to_be_converted % 16]
        num_to_be_converted //= 16
        if num_to_be_converted == 0:
            convert_confirmation()
            print("0x" + hex_string[::-1])
            break
    built_in_conversion()
    print(hex(num_to_check))


def warning_message():
    print('Only integers are allowed, please check your input and try again: ')


def welcome_message():
    print('Please enter a number to convert to hexadecimal: ')


def convert_confirmation():
    print('The result of the number conversion: ', end='')


def built_in_conversion():
    print('Conversion using the built-in function: ', end='')
