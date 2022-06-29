from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        # #   заменить на метод
        # if not isinstance(capacity_volume, (int, float)):
        #     raise TypeError
        # if not capacity_volume > 0:
        #     raise ValueError
        # self.capacity_volume = capacity_volume  # объем стакана
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

#   создать метод, который будет инициализировать атрибут capacity_volume
    def init_capacity_volume(self, capacity_volume):
        self.capacity_volume = capacity_volume

if __name__ == "__main__":
    glass = Glass(200, 100)  #  инициализировать экземпляр класса Glass
    print(glass.capacity_volume)  #  распечатать атрибут capacity_volume
    print(glass.occupied_volume)  # распечатать атрибут occupied_volume
