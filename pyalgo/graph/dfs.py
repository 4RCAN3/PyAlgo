'''
module for implementation
of depth first search
'''

def dfs(graph: list, start: int, visited = None):

    """
    Here 'graph' represents the adjacency list
    of the graph, and 'start' represents the
    node from which to start
    """

    if visited is None:
        visited = set()

    visited.add(start)

    for next in (graph[start] - visited):
        dfs(graph, next, visited)

    return visited

def dfs_paths(graph: list, start: int, goal: int):

    """
    Returns all possible paths between a
    start vertex and a goal vertex
    """

    stack = [(start, [start])]

    while (stack):

        (vertex, path) = stack.pop()

        for next in (graph[vertex] - set(path)):

            if next == goal:
                yield path + [next]

            else:
                stack.append((next, path + [next]))

    return stack

'''
PyAlgo
Devansh Singh, 2021
'''