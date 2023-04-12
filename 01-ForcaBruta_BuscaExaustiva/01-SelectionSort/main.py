# Implementação do algoritmo Selection Sort
# Operação básica: Comparação para encontrar o menor elemento

def selection_sort(array):
    size = len(array)
    for position in range(size):
        index_min = position
        for step in range(position+1, size):
            if array[step] < array[index_min]:
                index_min = step
        if index_min != position:
            array[position], array[index_min] = array[index_min], array[position]
    return array


array = [-5, 2, 8, 0, 3]
print("Arranjo:", array)
sorted_array = selection_sort(array)
print("Arranjo ordenado:", sorted_array)