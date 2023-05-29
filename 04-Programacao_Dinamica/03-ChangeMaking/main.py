# Implementação do algoritmo ChangeMaking

def change_making(change, coins):
    if change == 0:
        return 0
    if change == 1:
        return 1
    memory = [0] + [float('inf')] * change
    for coin in coins:
        count = coin
        while count <= change:
            memory[count] = min(memory[count], memory[count - coin] + 1)
            count += 1
    if memory[change] != float('inf'):
        return memory[change]
    else:
        return -1


change = 8
coins = [1, 5, 10, 25, 50, 100]

min_coins = change_making(change, coins)
print(f"O número mínimo de moedas para o troco {change} é de {min_coins} moedas")