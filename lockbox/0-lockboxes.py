def depth_first_search(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited and neighbor < len(graph):
            depth_first_search(graph, neighbor, visited)

    return visited


def canUnlockAll(boxes):
    visited = depth_first_search(graph=boxes, node=0)
    for i in range(1, len(boxes)):
        if i in visited:
            continue
        return False

    return True
