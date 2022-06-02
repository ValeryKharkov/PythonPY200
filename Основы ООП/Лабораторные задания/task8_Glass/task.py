# TODO Добавить методы add_water и remove_water
class Moto:
    def __init__(self, environment: str, speed: int, price: int):
        """
        Конструктор атрибутов
        :param environment: назначение, среда обитания
        :param speed: скорость
        :param price: стоимость
        """

        self.environment = environment
        self.speed = speed
        self.price = price
        pass

    def __repr__(self):
        return f"Назначение: {self.environment}. Скорость: {self.speed}. Стоимость: {self.price}."

boxer = Moto('offroad', 80, 100000)
pulsar = Moto('city', 100, 150000)

print(boxer)
print(pulsar)






