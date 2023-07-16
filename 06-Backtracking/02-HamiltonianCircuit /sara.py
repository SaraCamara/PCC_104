def is_valid_next_node(node, path, graph):
    # Check if the node can be added to the path
    if node in path:
        return False

    # Check if there is an edge between the last node in the path and the current node
    last_node = path[-1]
    if node not in graph[last_node]:
        return False

    return True


def hamiltonian(graph, path, start):
    # Base case: If all nodes are visited and there is an edge from the last node to the start node, return the path
    if len(path) == len(graph) and start in graph[path[-1]]:
        return path + [start]

    for node in graph[start]:
        if is_valid_next_node(node, path, graph):
            result = hamiltonian(graph, path + [node], node)
            if result is not None:
                return result

    return None


if __name__ == '__main__':
    graph = {
        0: [1, 2, 3],
        1: [0, 2, 5],
        2: [0, 1, 3, 4],
        3: [0, 2, 4],
        4: [2, 3, 5],
        5: [1, 4]
    }

    start_node = 0

    path = hamiltonian(graph, [start_node], start_node)

    if path is None:
        print("Circuito Hamiltoniano não encontrado.")
    else:
        print("Circuito Hamiltoniano:", path)


    # graph = {
    #     0: [1, 2, 3],
    #     1: [0, 2, 5],
    #     2: [0, 1, 3, 4],
    #     3: [0, 2, 4],
    #     4: [2, 3, 5],
    #     5: [1, 4]
    # }
    #
    # start_node = 0
    #
    # path = hamiltonian(graph, [start_node], start_node)
    #
    # if path is None:
    #     print("Hamiltonian Circuit not found.")
    # else:
    #     print("Hamiltonian Circuit:", path)
    #
    # graph = {
    #     0: [1, 2, 4],
    #     1: [0, 3],
    #     2: [0, 4, 5],
    #     3: [1, 5],
    #     4: [0, 2],
    #     5: [2, 3]
    # }

    # graph = {
    #     0: [1, 2],
    #     1: [0, 2],
    #     2: [0, 1]
    # }

    # graph = {
    #     0: [1, 2, 3],
    #     1: [0, 2, 3],
    #     2: [0, 1, 3],
    #     3: [0, 1, 3]
    # }
    # Example usage
    # graph = [
    #     [0, 1, 0, 1, 0],
    #     [1, 0, 1, 1, 1],
    #     [0, 1, 0, 0, 1],
    #     [1, 1, 0, 0, 1],
    #     [0, 1, 1, 1, 0]
    # ]
    # Example usage
