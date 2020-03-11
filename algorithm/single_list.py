from typing import TypeVar, Generator, Iterable, Type

T = TypeVar("T")


class SNode:
    """Node for a singly linked list
    """

    def __init__(self, val: T, next_node: 'SNode' = None):
        self.val = val
        self.next = next_node


class SLinkedList:
    """An imlementation of singly linked list
    """

    def __init__(self):
        self.head: SNode = None

    def appendleft(self, val: T):
        """
        Appends element to front of the linked list

        :param val: value to append to the list
        """
        new_node = SNode(val, self.head)
        self.head = new_node

    def append(self, val: T):
        """
        Appends element to front of the linked list

        :param val: value to append to the list
        """
        last = None
        for node in self:
            last = node
        new_node = SNode(val)
        if not last:
            self.head = new_node
        else:
            last.next = new_node

    def insert(self, val: T, after: SNode):
        """
        Insert element to the linked list after give node if node is present

        :param val: value to insert to the list
        :param after: the SNode to insert val after
        """
        for node in self:
            if node == after:
                new_node = SNode(val, node.next)
                node.next = new_node
                return

    def delete(self, val: T):
        """
        Delete first given val from the linked list if present
        """
        if self.head.val == val:
            self.head = self.head.next
            return
        prev = None
        for node in self:
            if node.val == val:
                prev.next = node.next
                return
            prev = node

    @classmethod
    def from_iterator(cls, to_iter: Iterable[T]) -> 'SLinkedList':
        """
        Create a `SLinkedList` from an iterable

        :param to_iter: an iterable to iter on
        :type to_iter: Iterable[T]
        :returns: A Singly Linked List
        :rtype: `SLinkedList`
        """
        ret = cls()
        node = None
        for i in iter(to_iter):
            if not node:
                ret.head = SNode(i)
                node = ret.head
            else:
                new_node = SNode(i)
                node.next = new_node
                node = new_node
        return ret

    def __iter__(self) -> Generator[T, None, None]:
        """Genertor to loop over the list
        """
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        ret = []
        for i in iter(self):
            ret.append(str(i.val))
        return "->".join(ret)
