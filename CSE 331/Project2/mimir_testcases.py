import unittest
from LinkedList import insert, remove, remove_all, to_string, search, sum_list, \
    count, reverse, length, remove_fake_requests


class TestProject2(unittest.TestCase):
    def test_insert(self):
        linked_list = insert(0)
        insert(1, linked_list)
        insert(2, linked_list)

        for i in range(0, 3):
            assert linked_list.value == i
            linked_list = linked_list.next

    def test_to_string(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)
        insert(3, list1)

        assert to_string(list1) == "0, 1, 2, 3"

    def test_length(self):
        list1 = insert(1)
        insert(2, list1)
        insert(3, list1)

        assert length(list1) == 3

    def test_search(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)

        assert search(2, list1)
        assert not search(3, list1)

    def test_count(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)

        assert count(0, list1) == 1
        assert count(1, list1) == 1
        assert count(2, list1) == 1

    def test_sum_list(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)
        insert(3, list1)

        assert sum_list(list1) == 6

    def test_remove(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)
        insert(3, list1)

        list1 = remove(1, list1)
        for i in [0, 2, 3]:
            assert list1.value == i
            list1 = list1.next

        assert list1 == None

    def test_remove_all(self):
        list1 = insert(0)
        insert(1, list1)
        insert(0, list1)
        insert(2, list1)
        insert(3, list1)
        insert(0, list1)

        list1 = remove_all(0, list1)
        test_list = list1
        for i in [1, 2, 3]:
            assert test_list.value == i
            test_list = test_list.next

        assert test_list == None

    def test_reverse(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)
        insert(3, list1)

        list1 = reverse(list1)

        for i in [3, 2, 1, 0]:
            assert list1.value == i
            list1 = list1.next

    def test_fake_requests(self):
        requests = insert(170144)
        insert(567384, requests)
        insert(604853, requests)
        insert(783456, requests)
        insert(783456, requests)
        insert(903421, requests)

        real_requests = remove_fake_requests(requests)
        for i in [170144, 567384, 604853, 903421]:
            assert real_requests.value == i
            real_requests = real_requests.next


if __name__ == "__main__":
    unittest.main()
