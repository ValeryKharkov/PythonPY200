
from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume):
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume):
        self.occupied_volume = occupied_volume

    def add_water(self, water):
        if not isinstance(water, int):
            raise TypeError('Значение добавляемой воды должно быть int')
        if water <= 0:
            raise ValueError('Значение добавляемой воды должно быть > 0')

        free_volume = self.capacity_volume - self.occupied_volume
        if water > free_volume:
            raise ValueError('Значение добавляемой воды должно быть меньше free_volume')

        self.occupied_volume += water

    def remove_water(self, water):
        self.occupied_volume -= water


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса

    print(f'Исходные значения экземпляра класса: Объем стакана = {glass.capacity_volume}, Объем жидкости = {glass.occupied_volume}')
    print("Добавляем воду")
    glass.add_water(30)
    print(f'После добавления воды, объем жидкости = {glass.occupied_volume}')
    print("Выливаем воду")
    glass.remove_water(60)
    print(f'После выливания воды, объем жидкости = {glass.occupied_volume}')

# TODO Добавить методы add_water и remove_water