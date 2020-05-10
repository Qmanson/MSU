"""
PROJECT 3 - Quick/Insertion Sort
Name: Quincy Manson
PID: A57034941
"""


def _insertion_wrapper(insertion_sort):
    """
    DO NOT EDIT
    :return:
    """
    def insertion_counter(*args, **kwargs):
        if args[0].size > 1:
            args[0].c += 1
        insertion_sort(*args, **kwargs)
    return insertion_counter

# ------------------------Complete function below---------------------------
@_insertion_wrapper
def insertion_sort(dll, low, high):
    """
     Preforms insertion sort on a list a given doubly linked list.
     :param dll: The doubly linked list that must be modified
     :param low: low value of the DLL
     :param high: high value of the DLL
     """
    node = low
    if high is not None:
        while node is not high.get_next():
            next_node = node.get_next()
            if node is not low:
                key = node.get_previous()
                while node.get_value() < key.get_value():
                    temp = key.get_value()
                    key.set_value(node.get_value())
                    node.set_value(temp)
                    if key is not low:
                        node = key
                        key = key.get_previous()
            node = next_node
