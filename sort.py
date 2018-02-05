from decorators import time_it
from util import findSmallest


@time_it
def selectionSort(arr):
    """
    Selection Sort algorithm
    :param arr: an array to be sorted
    :return: the array sorted
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
