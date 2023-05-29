from animals import Animal, Bird, Dog, Cat, Fish, Horse
from typing import Any

class AnimalFarm:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == Fish:
            return Fish(**kwargs)
        elif animal_type == Bird:
            return Bird(**kwargs)
        elif animal_type == Horse:
            return Horse(**kwargs)
        elif animal_type == Dog:
            return Dog(**kwargs)
        elif animal_type == Cat:
            return Cat(**kwargs)
        else:
            return Animal(**kwargs)
