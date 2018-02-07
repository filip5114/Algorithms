from collections import deque

import util


def bfs(graph, starting_node):
    """
    BFS algorithm for graphs.
    :param graph: dict() representing graph
    :param starting_node: point starting node
    :return: nearest node matching requirements
    """
    search_queue = deque()
    search_queue += graph[starting_node]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person.endswith('ek'):
                return person
            else:
                search_queue += graph[person]
    return None


def dijsktra(graph, costs, parents):
    """
    Dijsktra algorithm. Find the lowest cost route in the graph to get from point A to point B
    :param graph: dict() containing graph structure
    :param costs: dict() containing costs for nodes
    :param parents: dict() containing parent-child structure of nodes
    :return: dict() containing lowest costs to get to every node
    """
    processed = []
    node = util.find_lowest_cost_node(costs, processed)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = util.find_lowest_cost_node(costs, processed)
    return costs
