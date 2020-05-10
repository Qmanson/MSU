"""
Project 4- Solution
"""


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.total = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size and self.total == other.get_total()

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"
        result = ""
        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + (", ").join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        """
        Determines if the queue is empty
        :return: true if queue is empty
        """
        return self.size == 0

    def __len__(self):
        """
        Gives the length of the queue
        :return: [int] size of queue
        """
        return self.size

    def get_total(self):
        """
        Gives the total sum of the queue
        :return: sum of queue values
        """
        return self.total

    def head_element(self):
        """
        Value of the head element
        :return: element of the head value
        """
        return self.data[self.head]

    def tail_element(self):
        """
        Value of the tail element
        :return: element of the tail value
        """
        return self.data[self.tail-1]

    def enqueue(self, val):
        """
        Adds value to end of queue
        :param: val Value to be added
        :return: None
        """
        if self.size + 1 > self.capacity:
            self.grow()
        if (self.tail >= self.capacity) and (self.data[0] is None):
            self.data[0] = val
            self.size += 1
            self.tail = 1
        else:
            self.data[self.tail] = val
            self.size += 1
            self.tail += 1
        if self.size >= self.capacity:
            self.grow()
        self.total += val
        return None

    def dequeue(self):
        """
        Removes value from head of queue
        :return: value being removed
        """
        if self.size is 0:
            return None
        else:
            result = self.data[self.head]
            self.data[self.head] = None
            self.size -= 1
            if ((self.head + 1) >= self.capacity) and (self.data[0] is not None):
                self.head = 0
            else:
                self.head += 1
            if (self.capacity > 7) and (self.size <= self.capacity // 4):
                self.shrink()
            self.total -= result
            return result

    def grow(self):
        """
        Doubles the capacity of queue and
        sets the queue in order from start
        """
        new_list = [None] * self.capacity * 2
        pos = self.head
        new_pos = 0
        if not self.is_empty():
            while pos != (self.tail-1):
                new_list[new_pos] = self.data[pos]
                new_pos += 1
                if (pos + 1) >= self.capacity:
                    pos = 0
                else:
                    pos += 1
            new_list[new_pos] = self.data[self.tail-1]
        self.data = new_list
        self.head = 0
        self.tail = self.capacity
        self.capacity = self.capacity * 2

    def shrink(self):
        """
        Halves the capacity of queue and
        sets the queue in order from start
        """
        new_list = [None] * (self.capacity // 2)
        pos = self.head
        new_pos = 0
        while pos != (self.tail - 1):
            new_list[new_pos] = self.data[pos]
            new_pos += 1
            if (pos + 1) >= self.capacity:
                pos = 0
            else:
                pos += 1
        new_list[new_pos] = self.data[self.tail - 1]
        self.data = new_list
        self.head = 0
        self.tail = new_pos + 1
        self.capacity = self.capacity // 2


def threshold_sum(nums, threshold):
    """
    Finds highest sequence of  numbers with the
    highest sum less than or equal to the threshold value
    :param: nums set of numbers to find threshold sum
    :param: threshold number to find sum less then
    :return: touple greatest sum and its length
    """
    queue = CircularQueue()
    summ = 0
    length = 0
    for val in nums:
        queue.enqueue(val)
        if queue.get_total() <= threshold:
            if queue.get_total() > summ:
                summ = queue.get_total()
                length = queue.__len__()
            if queue.get_total() == summ:
                if queue.__len__() > length:
                    summ = queue.get_total()
                    length = queue.__len__()
        else:
            num = queue.__len__()-1
            while queue.get_total() > threshold:
                queue.dequeue()
                if queue.get_total() <= threshold:
                    if queue.get_total() > summ:
                        summ = queue.get_total()
                        length = queue.__len__()
                    if queue.get_total() == summ:
                        if queue.__len__() > length:
                            summ = queue.get_total()
                            length = queue.__len__()
                if queue.get_total()-val <= threshold:
                    if queue.get_total()-val > summ:
                        summ = queue.get_total()-val
                        length = queue.__len__()
                    if queue.get_total()-val == summ:
                        if queue.__len__() > length:
                            summ = queue.get_total()-val
                            length = queue.__len__()
    return summ, length
