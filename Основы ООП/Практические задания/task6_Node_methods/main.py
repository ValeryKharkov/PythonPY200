from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
         # добавить атрибуты
        self.value = value
        self.next = next_
    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return f"{self.value}" # вернуть значение узла

    #  добавить метод get_next
    def get_next(self):
        return f"{self.next}"

if __name__ == '__main__':
    first_node = Node(1)  # первый узел
    second_node = Node(2)  # второй узел

    print(first_node.get_value())# с помощью метода распечатать значение первого узла
    print(second_node.get_next())#  с помощью метода распечатать следующий узел второго узла
