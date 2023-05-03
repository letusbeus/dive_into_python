from random import randint


def random_queens_positions(size=8):
    """
    Функция генерирует пару чисел заданное при вызове функции количество раз (size)
    и заполняет список только уникальными парами чисел до достижения указанной длины (size).
    """
    random_positions = []
    while len(random_positions) != size:
        pos = tuple(randint(0, size - 1) for j in range(2))
        if pos not in random_positions:
            random_positions.append(pos)
        else:
            continue
    return random_positions


def intersection_check(data: list[tuple[int, ...]]) -> bool:
    """
    Функция принимает на вход список координат х и у и проверяет, имеются ли пересечения по диагонали, вертикали и
    горизонтали между парами точек (1‑я со 2‑й, 3-й, 4-й и т.д., затем 2-я с 3-й, 4-й, 5-й и т.д. и т.д.).
    Возвращает False, если разница по модулю координат х равна разнице по модулю координат у
    (abs(x1 - x2) == abs(y1 - y1))
    ИЛИ
    если координаты х1 и х2 ИЛИ у1 и у2 совпадают (if x1 == x2 or y1 == y2), иначе возвращает True.
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if (data[i][0] == data[j][0] or data[i][1] == data[j][1]
            ) or (
                    abs(data[i][0] - data[j][0]) == abs(data[i][1] - data[j][1])):
                return False
    return True


def arrange_the_figures(position, size):
    """
    Функция генерирует "шахматную доску" - матрицу заданной размерности size, заполняет ее значениям по умолчанию ('~')
    и присваивает элементам с индексами, указанными в списке position, значение 'Q' - ставит туда ферзя.
    """
    chessboard = [['~' for x in range(size)] for y in range(size)]
    queens_positions = position
    for i in range(size):
        column, row  = queens_positions[i]
        if chessboard[row][column] != 'Q':
            chessboard[row][column] = 'Q'
        else:
            continue
    return chessboard


def print_the_desk(desk_list, board_size):
    """
    Функция принимает на вход список пар чисел, представляющих собой координаты х и у, и размер матрицы.
    Присваивает элементам матрицами с индексами, соответствующим паре чисел из списка на входе, значения 'Q'.
    Выводит полученную измененную матрицу - т.н. "шахматную доску" - в консоль.
    """
    res = arrange_the_figures(desk_list, board_size)
    for j in res[::-1]:
        print(j)


def find_successful_arrangements(size: int, qty: int):
    """
    Функция принимает на вход два параметра: размер доски size и количество необходимых успешных расстановок qty.
    Возвращает список с требуемым количеством успешных расстановок на доске заданного размера.
    """
    good_list = []
    while len(good_list) != qty:
        positions = random_queens_positions(size)
        if intersection_check(positions):
            good_list.append(positions)
    return good_list


def print_successful_arrangements(size: int, qty: int):
    """
    Функция принимает на вход размер доски size и количество необходимых успешных расстановок qty, передает их для
    генерации списка с требуемым количеством успешных расстановок на доске заданного размера
    (см. find_successful_arrangements).
    Выводит в консоль все полученные успешные расстановки в виде списков, построчно.
    Выводит в консоль шахматные доски со всеми вариантами расстановок из полученного списка (см. print_the_desk).
    """
    count = 0
    good_list = find_successful_arrangements(size, qty)
    for i in good_list:
        count += 1
        print(f'Расстановка №{count} = {sorted(i)}')
        print_the_desk(i, size)
