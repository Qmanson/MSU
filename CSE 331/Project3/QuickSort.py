"""
PROJECT 3 - Quick/Insertion Sort
Name: Quincy Manson
PID: A57034941
"""

from Project3.InsertionSort import insertion_sort


def quick_sort(dll, start, end, size, threshold):
    """
      Preforms quick sort on a list a given doubly linked list.
     :param dll: The doubly linked list that must be modified
     :param start: start Node of the DLL
     :param end: end node of the DLL
     :param size: size of the DLL
     :param threshold: size of the DLL when insertion sort is preformed
      """
    if start is None or end is None or size == 1 or size == 0:
        return
    if size <= threshold:
        insertion_sort(dll, start, end)
    else:
        part = partition(start, end)
        pivot = part[0]
        part_size = part[1]
        quick_sort(dll, start, pivot.get_previous(), part_size, threshold)
        quick_sort(dll, pivot.get_next(), end, size - part_size - 1, threshold)


def partition(low, high):
    """
    Removes the middle of a given doubly linked list.
    :param low: low value for DLL
    :param high: high value for DLL
    :return: The pivot Node, Size of left half of list
    """
    if low is None or low is high:
        return None, 0
    thelow = low
    key = low
    count = 0
    while key is not high:
        if key.get_value() <= high.get_value():
            temp = key.get_value()
            key.set_value(thelow.get_value())
            thelow.set_value(temp)
            thelow = thelow.get_next()
            count += 1
        key = key.get_next()
    temp = thelow.get_value()
    thelow.set_value(high.get_value())
    high.set_value(temp)

    return thelow, count
