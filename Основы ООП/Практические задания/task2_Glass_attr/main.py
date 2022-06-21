from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.capacity_volume, glass1.occupied_volume)

    glass2 = Glass(200, 200)  # инициализировать ещё один стакан
    print(glass2.capacity_volume, glass2.occupied_volume)  # распечатать атрибуты экземпляра glass2

    print("Доливаем воды в первый стакан..., получаем:")
    #   доливаем воды в первый стакан
    glass1.occupied_volume += 150
    print(glass1.occupied_volume)


    #   сравнить id объектов
    print(glass1.occupied_volume is glass1.occupied_volume + 100)