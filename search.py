def binary_search(item_list, item):
    """
    Binary Search algorithm

    :param item_list: an ordered array
    :param item: item to be found in the array
    :return: (Int) index of the item in the array. If not found then returns None
    """
    low = 0
    high = len(item_list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = item_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

