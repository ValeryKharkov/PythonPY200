from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        #   инициализировать атрибуты экземпляра класса Node

        self.value = value
        self.next = next_
    #  реализовать метод __repr__ для отображения экземпляра
    def __repr__(self):
        return f"Node({self.value}, {self.next})"

if __name__ == '__main__':
    first_node = Node(1)  # инициализировать первый узел

    second_node = Node(2)  # инициализировать второй узел
    first_node.next = second_node  # через атрибут экземпляра устанавливаем первому узлу следующий узел

    print(first_node)
    print(second_node)
