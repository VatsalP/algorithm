from dataclasses import dataclass


from .common import *
from .deque import Deque


@dataclass
class Node:
    """Node for a doubly linked list
    """
    val: T
    next: 'Node' = None
    prev: 'Node' = None


class LinkedList(Deque):
    """An imlementation of singly linked list
    """

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.len = 0

    def appendleft(self, val: T):
        """
        Appends element to front of the linked list

        :param val: value to append to the list
        """
        new_node = Node(val, self.head)
        self.head = new_node

    def append(self, val: T):
        """
        Appends element to front of the linked list

        :param val: value to append to the list
        """
        last = None
        for node in self:
            last = node
        new_node = Node(val)
        if not last:
            self.head = new_node
        else:
            last.next = new_node

    def insert(self, val: T, after: Node):
        """
        Insert element to the linked list after give node if node is present

        :param val: value to insert to the list
        :param after: the Node to insert val after
        """
        for node in self:
            if node == after:
                new_node = Node(val, node.next)
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
    def from_iterator(cls, to_iter: Iterable[T]) -> 'LinkedList':
        """
        Create a `LinkedList` from an iterable

        :param to_iter: an iterable to iter on
        :type to_iter: Iterable[T]
        :returns: A Doubly Linked List
        :rtype: `LinkedList`
        """
        ret = cls()
        node = None
        for i in iter(to_iter):
            if not node:
                ret.head = Node(i)
                node = ret.head
                ret.tail = ret.head
            else:
                new_node = Node(i)
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

    def __len__(self):
        return self.len

    def __str__(self):
        ret = []
        for i in iter(self):
            ret.append(str(i.val))
        return "->".join(ret)
