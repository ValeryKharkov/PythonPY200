from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #   инициализировать объект "Стакан"
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError

        if capacity_volume <= 0:
            raise ValueError
        if occupied_volume > capacity_volume:
            raise ValueError

if __name__ == "__main__":
    ...  #  инициализировать два объекта типа Glass
    glass_1 = Glass(200, 500)
    glass_2 = Glass('граммы', 100)
    # попробовать инициализировать не корректные объекты
    print(glass_1)
    print(glass_2)