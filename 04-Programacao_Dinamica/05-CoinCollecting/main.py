# Implementação do algoritmo CoinCollection sem programação dinâmica

def coin_collecting(coins):
    n = len(coins)
    m = len(coins[0])

    max_coins = 0  # Variavel para guardar o numero maximo de moedas coletadas

    def dfs(i, j, collected_coins):
        nonlocal max_coins

        if i == n - 1 and j == m - 1:  # Posição inferior direita
            max_coins = max(max_coins, collected_coins)
            return

        if i < n - 1:  # Baixo
            dfs(i + 1, j, collected_coins + coins[i + 1][j])
        if j < m - 1:  # Direita
            dfs(i, j + 1, collected_coins + coins[i][j + 1])

    # Inicia da posição superior esquerda
    dfs(0, 0, coins[0][0])

    return max_coins


coins = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

max_coins = coin_collecting(coins)
print("O máximo de moedas coletadas foi:", max_coins)
