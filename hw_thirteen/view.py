import rect


def task():
    print('Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.\n'
          'Напишите к ним классы исключения с выводом подробной информации.\n'
          'Поднимайте исключения внутри основного кода.\n'
          'Например, нельзя создавать прямоугольник со сторонами отрицательной длины.\n\n'
          'Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра.\n'
          'У класса должно быть два метода, возвращающие периметр и площадь.\n'
          'Если при создании экземпляра передаётся только одна сторона, считаем, что у нас квадрат.')


def is_number(self):
    return f'The value of side can only be a number, you passed {type(self.value)}, value: {self.value}.'

def is_positive(self):
    return f'The value of side cannot be negative or zero, you passed {self.value}.'
