"""
double_list.py
==============

Provide implementation for a Doubly Linked List
which also implements `Deque`
"""
from dataclasses import dataclass

from .deque import Deque
from .common import *


@dataclass
class Node:
    """Node for a doubly linked list
    """
    val: T
    next: 'Node' = None
    prev: 'Node' = None


class LinkedList(Deque):
    """An imlementation of doubly linked list
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
        if self.len > 1:
            self.head.prev = new_node
            self.head = new_node
        elif self.len == 1:
            self.head = new_node
            self.tail.prev = new_node
        else:
            self.head = self.tail = new_node
        self.len += 1

    def append(self, val: T):
        """
        Appends element to front of the linked list

        :param val: value to append to the list
        """
        new_node = Node(val, None, self.tail)
        if self.len > 1:
            self.tail.next = new_node
            self.tail = new_node
        elif self.len == 1:
            self.tail = new_node
            self.head.next = new_node
        else:
            self.head = self.tail = new_node
        self.len += 1

    def insert(self, val: T, after: Node):
        """
        Insert element to the linked list after give node if node is present

        :param val: value to insert to the list
        :param after: the Node to insert val after
        """
        for node in self:
            if node == after:
                new_node = Node(val, node.next, after)
                if node.next:
                    node.next.prev = new_node
                else:
                    self.tail = new_node
                node.next = new_node
                self.len += 1
                return

    def popleft(self):
        """
        Pop leftmost element from the list
        """
        if self.len > 2:
            self.head = self.head.next
            self.head.prev = None
            self.len -= 1
        elif self.len == 2:
            self.tail.prev = None
            self.head = self.tail
            self.len -= 1
        elif self.len == 1:
            self.head = self.tail = None
            self.len -= 1
        else:
            raise IndexError("Can't popleft from an empty list")

    def pop(self):
        """
        Pop rightmost element from the list
        """
        if self.len > 2:
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
        elif self.len == 2:
            self.head.next = None
            self.tail = self.head
            self.len -= 1
        elif self.len == 1:
            self.head = self.tail = None
            self.len -= 1
        else:
            raise IndexError("Can't pop from an empty list")

    def delete(self, val: T):
        """
        Delete first given val from the linked list if present
        """
        for node in self:
            if node.val == val:
                if node == self.head:
                    if node.next:
                        self.head = node.next
                        node.prev = None
                    else:  # head == tail
                        self.head = None
                        self.tail = None
                else:
                    if node == self.tail:
                        self.tail = node.prev
                        self.tail.next = None
                    else:
                        prev = node.prev
                        node.next.prev = prev
                        prev.next = node.next
                self.len -= 1

    @classmethod
    def from_iterator(cls, to_iter: Iterable[T]) -> 'LinkedList':
        """
        Create a `LinkedList` from an iterable

        :param to_iter: an iterable to iter on
        :type to_iter: Iterable[T]
        :returns: A doubly Linked List
        :rtype: `LinkedList`
        """
        ret = cls()
        for i in iter(to_iter):
            ret.append(i)
        return ret

    def loop(self) -> Generator[T, None, None]:
        """Genertor to loop over the list values
        """
        node = self.head
        while node:
            yield node.val
            node = node.next

    def __reversed__(self) -> Generator[T, None, None]:
        """Generator to loop over list in reverse
        """
        node = self.tail
        while node:
            yield node
            node = node.prev

    def __iter__(self) -> Generator[T, None, None]:
        """Genertor to loop over the list
        """
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        """Return length of the list
        """
        return self.len

    def __str__(self):
        ret = []
        for i in iter(self):
            ret.append(str(i.val))
        return "<->".join(ret)
