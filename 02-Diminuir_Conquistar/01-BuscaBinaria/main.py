# Implementação do algoritmo Busca Binária com ordenação de Selection Sort.
# Operação básica: Comparação para encontrar o elemento procurado.
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


def binary_search(sorted_array, target):
    index_min, index_max = 0, len(sorted_array)-1

    while index_min <= index_max:
        index_med = (index_min + index_max)//2

        if target == sorted_array[index_med]:
            return index_med
        elif target < sorted_array[index_med]:
            index_max = index_med - 1
        else:
            index_min = index_med + 1
    return None


array = [-5, 0, 3, 2, 1]
target = 5
print("Arranjo:", array)
print("Valor procurado:", target)

sorted_array = selection_sort(array)
print("Arranjo ordenado:", sorted_array)

print("Implementação do algoritmo Busca Binária.")
binary_searched = binary_search(sorted_array, target)
if binary_searched is None:
    print("Valor procurado não encontrado.")
else:
    print("A posição do valor procurado é:", binary_searched)
