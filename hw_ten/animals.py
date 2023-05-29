class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        """
        Получаем данные об экземпляре класса: имя, возраст, остальные поля при наличии
        """
        info = f'{"Type:":8}{type(self).__name__}\n'
        fields = vars(self)
        for field, value in fields.items():
            info += f'{(field.capitalize() + ":"):8}{value.capitalize() if isinstance(value, str) else value}\n'
        return info


class Fish(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


class Bird(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.color = color
        self.voice = voice


class Horse(Animal):
    def __init__(self, name, age, hair, voice):
        super().__init__(name, age)
        self.hair = hair
        self.voice = voice


class Dog(Animal):
    def __init__(self, name, age, fur, voice):
        super().__init__(name, age)
        self.fur = fur
        self.voice = voice


class Cat(Animal):
    def __init__(self, name, age, fur, voice):
        super().__init__(name, age)
        self.fur = fur
        self.voice = voice


if __name__ == '__main__':
    print('Not for separate use')
