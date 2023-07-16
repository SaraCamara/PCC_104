

def hamiltonian_circuit(graph):
    path = [-1] * len(graph)  #vetor path vazio
    path[0] = 0  #começa do vértice 0
    return hamiltonian_util(graph, path, 1)


def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        if path[pos - 1] in graph[path[0]]:
            return True
        else:
            return False

    for v in graph[path[pos - 1]]: #V é o vértice relacionado a chave do graph que esta sendo analisado
        if is_valid_vertex(v, graph, path, pos):
            path[pos] = v #path recebe o vertice na posição

            if hamiltonian_util(graph, path, pos + 1):
                return path

            path[pos] = -1  # Backtracking
    return False


def is_valid_vertex(v, graph, path, pos):
    if v not in graph[path[pos - 1]]: #confere se o valor de V esta nos valores da chave (dicionario graph)
        return False
    if v in path: #confere se o V já esta no path
        return False
    return True


if __name__ == '__main__':
    graph = {
        0: [1, 2, 3],
        1: [0, 2, 5],
        2: [0, 1, 3, 4],
        3: [0, 2, 4],
        4: [2, 3, 5],
        5: [1, 4]
    }
    path = hamiltonian_circuit(graph)
    if path:
        print("Hamiltonian circuit found:", path)
    else:
        print("No Hamiltonian circuit exists.")