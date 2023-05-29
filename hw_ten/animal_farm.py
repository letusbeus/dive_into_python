from animals import Bird, Dog, Fish, Horse
from typing import Any


class AnimalFarm:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == 'Fish':
            return Fish(**kwargs)
        elif animal_type == 'Bird':
            return Bird(**kwargs)
        elif animal_type == 'Horse':
            return Horse(**kwargs)
        elif animal_type == 'Dog':
            return Dog(**kwargs)
