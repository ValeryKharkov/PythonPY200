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
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

# TODO реализовать класс DoubleLinkedNode


class DoubleLinkedNode(Node):
    def __init__(self, value = None, next_ = None, prev_ = None):
        super().__init__(value, next_)
        self.prev = prev_
    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DoubleLinkedNode"]):
        self._prev = prev_

    def __repr__(self) -> str:
        next_repr: str = str(None) \
            if self.next is None \
            else f"DoubleLinkedNode({self.next.value}, {None}, {None})"
        prev_repr: str = str(None) \
            if self.prev is None \
            else f"DoubleLinkedNode({self.prev.value}, {None}, {None})"
        return f"DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})"


if __name__ == '__main__':

    node_1 = DoubleLinkedNode(1)
    node_2 = DoubleLinkedNode(2)
    node_3 = DoubleLinkedNode(3)
    node_4 = DoubleLinkedNode(4)

    node_1.next = node_2
    node_2.next = node_3
    node_2.prev = node_1
    node_3.next = node_4
    node_3.prev = node_2
    node_4.prev = node_3

    print(repr(node_1))
    print(repr(node_2))
    print(repr(node_3))
    print(repr(node_4))