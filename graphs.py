from collections import deque


def bfs(graph, starting_node):
    """
    BFS algorithm for graphs.
    :param graph: dict() representing graph
    :return: nearest node matching requirements
    """
    search_queue = deque()
    search_queue += graph[starting_node]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person.endswith('ek'):
                return person
            else:
                search_queue += graph[person]
    return None