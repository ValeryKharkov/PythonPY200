from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        # установить значение следующего узла с помощью метода set_next
        self.next = None
        self.set_next((next_))
    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
       #  метод проверки корректности связываемого узла
        if not isinstance(node, (Node, type(None))):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        # метод должен проверять корректность узла и устанавливать значение атрибуту next
        self.is_valid(next_)
        self.next = next_


if __name__ == '__main__':
    # инициализируйте два узла с любыми значеними
    first_node = Node(1)
    second_node = Node(2)
    #  свяжите первый узел со вторым
    first_node.set_next(second_node)
    print(first_node)
    print(second_node)
