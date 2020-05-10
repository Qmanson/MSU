"""
PROJECT 2 - Linked List Recursion
Name:
PID:
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self.value = value  # element at the node
        self.next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    """
    Inserts a new node into the back of the linked list
    :param node: the node to insert
    :param value: the value to of the node to be inserted
    :return: [LinkedNode] the node at current location
    """
    if node is None:
        node = LinkedNode(value, None)
    else:
        node.next = insert(value, node.next)
    return node


def to_string(node):
    """
    Converts the linked list into a string
    :param node: the node to start the linked list
    :return: [String] String form of the linked list
    """
    if node is None:
        return ""
    elif node.next is None:
        return str(node)
    else:
        return str(node) + ", " + to_string(node.next)


def remove(value, node):
    """
    Removes a node from a linked list
    :param node: the node to start
    :param value: the value to find and remove
    :return: [LinkedNode] the current node
    """
    if node is None:
        return
    else:
        if node.value is value:
            return node.next
        else:
            node.next = remove(value, node.next)
            return node


def remove_all(value, node):
    """
    Removes all nodes that contain value
    :param node: the node to start
    :param value: the value to find and remove
    :return: [LinkedNode] the current node
    """
    if node is None:
        return
    else:
        if node.value is value:
            return remove_all(value, node.next)
        else:
            node.next = remove_all(value, node.next)
            return node


def search(value, node):
    """
    Searches for a node with value
    :param node: the node to start
    :param value: the value to find
    :return: [LinkedNode] the first node with value
    """
    if node is None:
        return None
    else:
        if node.value is value:
            return node
        else:
            return search(value, node.next)
    pass


def length(node):
    """
    Finds the total number of nodes in the linked list
    :param node: the node to start
    :return: [int] the size of the linked list
    """
    if node is None:
        return 0;
    else:
        return 1 + length(node.next)


def sum_list(node):
    """
    Sums up all the values of the nodes in the linked list
    :param node: node that starts the list
    :return: [int] sum of all values in linked list
    """
    if node is None:
        return 0
    else:
        return node.value + sum_list(node.next)


def count(value, node):
    """
    Counts how many nodes are in the linked list with value
    :param node: the node to start
    :param value: the value to find
    :return: [int] number of nodes with value
    """
    if node is None:
        return 0
    else:
        if node.value is value:
            return 1 + count(value, node.next)
        else:
            return count(value, node.next)


def reverse(node):
    """
    Changes the linked list to have values in opposite order
    :param node: the node to start
    :return: [LinkedNode] the current node
    """
    if node is None:
        return node
    elif node.next is None:
        return node
    else:
        other = reverse(node.next)
        node.next.next = node
        node.next = None
        return other



def remove_fake_requests(head):
    """
    Changes the linked list to have values in opposite order
    :param head: the node to start
    :return: [LinkedNode] the current node
    """
    if head is None or head.next is None:
        return head
    if head.next.value == head.value:
        while head.value == head.next.value:
            head = head.next
            if head.next is None:
                return None
        head = remove_fake_requests(head.next)
    else:
        head.next = remove_fake_requests(head.next)
    return head