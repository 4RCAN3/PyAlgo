'''
module for implementation
of breadth first search
'''

def bfs(graph: list, start: int):

    """
    Here 'graph' represents the adjacency list
    of the graph, and 'start' represents the
    node from which to start
    """

    visited, queue = set(), [start]

    while (queue):

        vertex = queue.pop(0)

        if (vertex not in visited):

            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited

def bfs_paths(graph: list, start: int, goal: int):

    """
    Returns all possible paths between a
    start vertex and a goal vertex, where
    the first path is the shortest path
    """

    queue = [(start, [start])]

    while (queue):

        (vertex, path) = queue.pop(0)

        for next in (graph[vertex] - set(path)):

            if (next == goal):
                yield path + [next]

            else:
                queue.append((next, path + [next]))

    return queue

'''
PyAlgo
Devansh Singh, 2021
'''