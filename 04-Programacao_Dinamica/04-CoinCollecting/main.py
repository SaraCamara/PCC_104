# Implementação do algoritmo CoinCollection com programação dinâmica

def coin_collecting(coins):
    n = len(coins)
    m = len(coins[0])

    # Inicializa uma matrix para guardar o numero maximo de moedas coletadas em cada posição
    max_coins = [[0] * m for _ in range(n)]

    # Calcula a quantidade maxima de moedas coletadas para cada posição
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                max_coins[i][j] = coins[i][j]
            elif i == 0:
                max_coins[i][j] = max_coins[i][j - 1] + coins[i][j]
            elif j == 0:
                max_coins[i][j] = max_coins[i - 1][j] + coins[i][j]
            else:
                max_coins[i][j] = max(max_coins[i - 1][j], max_coins[i][j - 1]) + coins[i][j]

    return max_coins[n - 1][m - 1]


coins = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

max_coins = coin_collecting(coins)
print("O máximo de moedas coletadas foi:", max_coins)

