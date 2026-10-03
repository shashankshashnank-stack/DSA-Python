from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on a graph.

    BFS visits nodes level by level using a queue.
    A set is used to keep track of visited nodes so
    that each node is processed only once.
    """

    # Keep track of nodes that have already been visited.
    visited = set()

    # BFS uses a queue following the FIFO (First In, First Out) principle.
    queue = deque()

    # Start the traversal from the given node.
    visited.add(start)
    queue.append(start)

    # Continue until there are no more nodes to process.
    while queue:

        # Remove the next node from the front of the queue.
        node = queue.popleft()

        # Process the current node.
        print(node, end=" ")

        # Explore all adjacent nodes.
        for neighbour in graph[node]:

            # Add unvisited neighbours to the queue.
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Graph represented using an adjacency list.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


# Start BFS traversal from node A.
bfs(graph, 'A')
