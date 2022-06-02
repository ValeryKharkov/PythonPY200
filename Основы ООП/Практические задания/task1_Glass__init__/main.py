from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        # инициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # Объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if not occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # Объем жидкости

if __name__ == "__main__":
    ...  # инициализировать два объекта типа Glass
    glass_1 = Glass(200, 120)
    glass_2 = Glass(500, 50)

    # попробовать инициализировать не корректные объекты
    glass_3 = Glass(-200, 120)
    glass_4 = Glass('500', 50)