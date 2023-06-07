import view


def check_user_input():
    view.task_one()
    view.task_one_welcome_message()
    while True:
        user_number = input()
        if user_number.isdigit():
            user_number = int(user_number)
            return user_number
        else:
            view.task_one_warning_message()


def convert_to_hex():
    num_to_be_converted = check_user_input()
    num_to_check = num_to_be_converted
    hex_string = ""
    while True:
        hex_string += "0123456789abcdef"[num_to_be_converted % 16]
        num_to_be_converted //= 16
        if num_to_be_converted == 0:
            view.conversion_confirmation()
            print("0x" + hex_string[::-1])
            break
    view.built_in_conversion()
    print(hex(num_to_check), end='\n\n')
