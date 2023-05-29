# Implementação do algoritmo KnapsackProblem com o método de função de memória

def knapsack(weights, values, capacity):
    n = len(weights)

    # Inicializa a matriz para guardar o valor maximo de cada subproblema
    max_value = [[-1] * (capacity + 1) for _ in range(n + 1)]

    # Função recursiva de memorização
    def knapsack_memoization(i, j):
        if max_value[i][j] >= 0:
            return max_value[i][j]

        if i == 0 or j == 0:
            value = 0
        elif j < weights[i - 1]:
            value = knapsack_memoization(i - 1, j)
        else:
            value = max(knapsack_memoization(i - 1, j),
                        values[i - 1] + knapsack_memoization(i - 1, j - weights[i - 1]))

        max_value[i][j] = value
        return value

    return knapsack_memoization(n, capacity)


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value = knapsack(weights, values, capacity)
print("O valor máximo", max_value)