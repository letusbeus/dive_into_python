from view import task_animal_farm
from animals import Animal, Bird, Dog, Cat, Fish, Horse
from animal_farm import AnimalFarm

if __name__ == "__main__":
    task_animal_farm()
    vanda = AnimalFarm.create_animal(Fish, name='Vanda', age=5, color='Rainbow')
    carl = AnimalFarm.create_animal(Bird, name='Carl', age=8, color='Black', voice='CRAW!')
    fido = AnimalFarm.create_animal(Dog, name='Fido', age=5, voice='Woof!', fur='Pale, long')
    tom = AnimalFarm.create_animal(Cat, name='Tom', age=2, fur='brown', voice='meow!')
    starlight = AnimalFarm.create_animal(Horse, name='starlight', age=7, hair='blond', voice='Ghrrr')
    print(vanda.get_info())
    print(fido.get_info())
    print(tom.get_info())
    print(starlight.get_info())
    print(carl.get_info())
