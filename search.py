from decorators import time_it


@time_it
def binary_search(itemList, item):
    """
    Binary Search algorithm

    :param itemList: an ordered array
    :param item: item to be found in the array
    :return: (Int) index of the item in the array. If not found then returns None
    """
    low = 0
    high = len(itemList) - 1

    while low <= high:
        mid = (low + high)//2
        guess = itemList[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
