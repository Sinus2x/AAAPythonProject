import abc
from pizza import Pizza
from typing import Literal


class Margherita(Pizza):
    def __init__(self, size: Literal['L', 'XL'] = 'L'):
        super().__init__(size)

    def components(cls):
        ingredients = super().components
        ingredients.append('tomatoes')
        return ingredients

    def emoji(cls):
        return '🧀'


if __name__ == '__main__':
    m = Margherita()
    print(m.emoji)