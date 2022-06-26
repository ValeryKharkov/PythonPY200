from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, pointer: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param pointer: следующий узел, если он есть
        """
        self.value = value

        # установить значение следующего узла с помощью метода set_next
        self.next = None
        self.set_next(pointer)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
       # метод проверки корректности связываемого узла
        if not isinstance(node, (Node, type(None))):
            raise TypeError

    def set_next(self, pointer: Optional["Node"] = None) -> None:
        # метод должен проверять корректность узла и устанавливать значение атрибуту next
        self.is_valid(pointer)
        self.next = pointer


if __name__ == '__main__':
    #  инициализируйте два узла с любыми значеними
    first_node = Node(1)
    second_node = Node(2)
    #  свяжите первый узел со вторым
    first_node.set_next(second_node)
    print(first_node)
    print(second_node)
