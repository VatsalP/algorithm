from algorithm.single_list import SLinkedList


class TestSLinkedList:
    """Tests for `algortithm.single_list.SLinkedList`
    """

    def test_append(self):
        sl = SLinkedList()
        sl.append(0)
        sl.append(1)
        sl.append(2)
        assert sl.head.val == 0
        for i, node in enumerate(sl):
            assert i == node.val

    def test_appendleft(self):
        sl = SLinkedList()
        sl.appendleft(0)
        sl.appendleft(1)
        sl.appendleft(2)
        sl.appendleft(3)
        sl.appendleft(4)
        assert sl.head.val == 4
        for i, node in enumerate(sl):
            assert (len(sl) - i - 1) == node.val

    def test_from_iter(self):
        sl = SLinkedList.from_iterator(range(10))
        assert sl.head.val == 0
        for i, node in enumerate(sl):
            assert i == node.val

    def test_insert(self):
        sl = SLinkedList.from_iterator(range(4))
        l = list(sl)
        for i in range(4):
            sl.insert(-1, l[i])
        for i, node in enumerate(sl):
            if i % 2 == 0:
                assert node.val == l[i//2].val
            else:
                assert node.val == -1

    def test_delete(self):
        sl = SLinkedList.from_iterator(range(6))
        sl.delete(0)
        assert sl.head.val == 1
        assert len(sl) == 5
        sl.delete(7)
        assert len(sl) == 5
        sl.delete(2)
        sl.delete(5)
        assert sl.head.next.val == 3
        assert sl.head.next.next.val == 4
