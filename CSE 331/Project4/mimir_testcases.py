import unittest
from CircularQueue import CircularQueue, threshold_sum


class TestProject1(unittest.TestCase):

    def test_accessors(self):
        queue = CircularQueue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        assert not queue.is_empty()
        assert len(queue) == 4
        assert queue.get_total() == 10
        assert queue.tail_element() == 4
        assert queue.head_element() == 1

    def test_enqueue(self):
        queue = CircularQueue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        assert queue.data == [10, 20, 30, None]
        assert queue.size == 3
        assert queue.head == 0
        assert queue.tail == 3
        assert queue.capacity == 4

    def test_dequeue(self):
        queue = CircularQueue(6)

        for i in range(0, 5):
            queue.enqueue(i * 5)

        assert queue.data == [0, 5, 10, 15, 20, None]
        assert queue.size == 5
        assert queue.capacity == 6
        assert queue.head == 0
        assert queue.tail == 5

        queue.dequeue()

        assert queue.data == [None, 5, 10, 15, 20, None]
        assert queue.size == 4
        assert queue.capacity == 6
        assert queue.head == 1
        assert queue.tail == 5

    def test_grow(self):
        queue = CircularQueue(1)

        for i in range(0, 16):
            queue.enqueue(i)

        assert queue.data == [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        assert queue.capacity == 32
        assert queue.size == 16
        assert queue.head == 0
        assert queue.tail == 16

    def test_shrink(self):
        queue = CircularQueue()

        for i in range(0, 5):
            queue.enqueue(i)

        assert queue.data == [0, 1, 2, 3, 4, None, None, None]
        assert queue.size == 5
        assert queue.capacity == 8
        assert queue.head == 0
        assert queue.tail == 5

        for _ in range(3):
            queue.dequeue()

        print(queue.data)
        assert queue.data == [3, 4, None, None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 2

    def test_threshold_sum(self):
        assert threshold_sum([2,2,4,1,1], 4) == (4, 2)
        assert threshold_sum([1,2,2,3], 6) == (5, 3)
        assert threshold_sum([1, 2, 4, 3], 7) == (7, 3)
        assert threshold_sum([], 0) == (0, 0)
        assert threshold_sum([8,8,9,9,9,9,99,9,9], 40) == (36, 4)
        assert threshold_sum([8,7,6,5], 4) == (0, 0)

if __name__ == "__main__":
    unittest.main()
