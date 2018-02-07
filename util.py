def find_smallest(arr):
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


def find_lowest_cost_node(costs, processed_nodes=[]):
    """
    Function finds the node with the lowest cost which is not yet processed.
    :param costs: dict() containing nodes with costs
    :param processed_nodes: list containing processed nodes
    :return: node with the lowest cost
    """
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed_nodes:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
