from util import find_smallest


def selection_sort(arr):
    """
    Selection Sort algorithm
    :param arr: an array to be sorted
    :return: the array sorted
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
