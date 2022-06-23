from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):  #  наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data) #  расширяем конструктор, чтобы в связном списке был driver
        self.driver = driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        self.clear()  #  считать данные из драйвера
        data = self.driver.read()
        for value in data:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        ...  # записать данные с помощью драйвера
        self.driver.write(self)

if __name__ == '__main__':
    ll = LinkedListWithDriver()  #  инициализировать пустой LinkedListWithDriver
    print("Считать данные из файла input.txt")
    #  инициализировать драйвер и считать данные
    ll.driver = SimpleFileFactoryMethod.get_driver()
    ll.read()
    print(ll)

    print("Записать данные в файл по умолчанию")
    # заменить драйвер и записать данные
    ll.driver = SimpleFileFactoryMethod.get_driver()
    ll.write()