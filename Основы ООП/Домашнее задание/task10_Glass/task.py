# написать класс Glass согласно условию
class Glass:
    def __init__(self, material: str):
        """
        Создание класса с одним атрибутом и одним методом
        :param material: материал объекта
        """
        self.material_attr = material

    def get_material(self):
        return self.material_attr


if __name__ == "__main__":
    result = Glass('paper')
    print(result)
# TODO что сделать, что бы консоль печатала "paper"