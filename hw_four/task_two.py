import view

user_dict = {}
user_string = 'test.py'


def dict_transformation(**kwargs) -> None:
    view.task_two()
    for key, value in kwargs.items():
        user_dict[str(value)] = hash(key) if isinstance(key, (int, str, float)) else str(key)
    print(user_dict)
