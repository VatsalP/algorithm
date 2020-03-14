"""
deque.py
========

Provides `Deque` abstract class to be implemented by
other Classes.
"""
from abc import ABC, abstractmethod

from .common import *

class Deque(ABC):
    """
    Deque Abstact Base Class

    Providing interface for other Datastructure to implement
    a Double ended queue
    """
    @abstractmethod
    def append(self, val: T):
        """Append val to right of the deque
        """
        pass

    @abstractmethod
    def appendleft(self, val: T):
        """Append val to the left of the deque
        """
        pass

    @abstractmethod
    def pop(self):
        """Pop the right most elem of the deque
        """
        pass

    @abstractmethod
    def popleft(self):
        """Pop the left most elem of the deque
        """
        pass
