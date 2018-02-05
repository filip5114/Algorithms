from decorators import time_it


def findSmallest(arr):
    """
    Find a smallest value in the array
    :param arr: an array
    :return: (Int) an index of the smallest item in the array
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
