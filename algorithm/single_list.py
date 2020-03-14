"""
single_list.py
==============

Implementation for a Singly Linked List
"""
from dataclasses import dataclass

from .common import *


@dataclass
class SNode:
    """Node for a singly linked list
    """
    val: T
    next: 'SNode' = None


class SLinkedList:
    """An imlementation of singly linked list
    """

    def __init__(self):
        self.head: SNode = None
        self.len = 0

    def appendleft(self, val: T):
        """
        Appends element to front of the linked list

        :param val: value to append to the list
        """
        new_node = SNode(val, self.head)
        self.head = new_node
        self.len += 1

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
        self.len += 1

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
                self.len += 1
                return

    def delete(self, val: T):
        """
        Delete first given val from the linked list if present
        """
        if self.head.val == val:
            self.head = self.head.next
            self.len -= 1
            return
        prev = None
        for node in self:
            if node.val == val:
                prev.next = node.next
                self.len -= 1
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
        ret.len = 0
        for i in iter(to_iter):
            if not node:
                ret.head = SNode(i)
                node = ret.head
            else:
                new_node = SNode(i)
                node.next = new_node
                node = new_node
            ret.len += 1
        return ret

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
        return "->".join(ret)
