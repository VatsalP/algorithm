from algorithm.double_list import LinkedList


class TestLinkedList:
    """Tests for `algortithm.double_list.LinkedList`
    """

    def test_append(self):
        dl = LinkedList()
        dl.append(0)
        dl.append(1)
        dl.append(2)
        dl.append(3)
        assert dl.head.val == 0
        assert dl.tail.val == 3
        prev = None
        for i, node in enumerate(dl):
            assert i == node.val
            assert prev == node.prev
            prev = node

    def test_appendleft(self):
        dl = LinkedList()
        dl.appendleft(0)
        dl.appendleft(1)
        dl.appendleft(2)
        dl.appendleft(3)
        dl.appendleft(4)
        assert dl.head.val == 4
        for i, node in enumerate(dl):
            assert (len(dl) - i - 1) == node.val

    def test_from_iter(self):
        dl = LinkedList.from_iterator(range(10))
        assert dl.head.val == 0
        for i, node in enumerate(dl):
            assert i == node.val

    def test_insert(self):
        dl = LinkedList.from_iterator(range(4))
        l = list(dl)
        for i in range(4):
            dl.insert(-1, l[i])
        for i, node in enumerate(dl):
            if i % 2 == 0:
                assert node.val == l[i//2].val
            else:
                assert node.val == -1

    def test_delete(self):
        dl = LinkedList.from_iterator(range(6))
        dl.delete(0)
        assert dl.head.val == 1
        assert len(dl) == 5
        dl.delete(7)
        assert len(dl) == 5
        dl.delete(2)
        dl.delete(5)
        assert dl.head.next.val == 3
        assert dl.head.next.next.val == 4
