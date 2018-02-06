def sum_array(arr):
    """
    Sum elements of array using recursion
    :param arr: (list[int]) integer array
    :return: sum of array elements
    """
    if not arr:
        return 0
    else:
        return arr.pop(0) + sum_array(arr)


def count_array(arr):
    """
    Count array length using recursion
    :param arr: array
    :return: (Int) length of array
    """
    if not arr:
        return 0
    else:
        arr.pop()
        return 1 + count_array(arr)


def find_largest_nr(arr):
    """
    Finds largest number in array using recursion
    :param arr: array of numbers
    :return: largest number in array, 0 if empty
    """
    if len(arr) == 1:
        return arr.pop()
    elif not arr:
        return 0
    else:
        pivot = arr.pop(len(arr)//2)
        larger_nr_array = []
        for nr in arr:
            if nr > pivot:
                larger_nr_array.append(nr)
        if not larger_nr_array:
            larger_nr_array = [pivot]
        return find_largest_nr(larger_nr_array)
