import json


def deco_save_to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {}
        for i in result:
            key = f'{i[0]}x^2 + {i[1]}x + {i[2]} = 0'
            data[key] = i[-1]
        with open('save_to_json_deco.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return result
    return wrapper
