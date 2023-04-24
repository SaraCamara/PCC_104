# Implementação do algoritmo Interpolation Search.
# Operação básica: Comparar se o item atual é o item procurado.

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


def interpolation_search(sorted_array, target):
    index_min, index_max = 0, len(sorted_array)-1

    while index_min <= index_max and sorted_array[index_min] <= target <= sorted_array[index_max]:
        position = index_min + ((target-sorted_array[index_min])*(index_max - index_min)//(sorted_array[index_max]-sorted_array[index_min]))
        if target == sorted_array[position]:
            return position
        elif target < sorted_array[position]:
            index_max = position - 1
        else:
            index_min = position + 1
    return None

array = [1, 2, 5, 13, 10, 11]
target = 13
print("Arranjo:", array)
print("Valor procurado:", target)

sorted_array = selection_sort(array)
print("Arranjo ordenado:", sorted_array)

print("Implementação do algoritmo Interpolation Search.")
index_searched = interpolation_search(sorted_array, target)
if index_searched is None:
    print("Valor procurado não encontrado.")
else:
    print("A posição do valor procurado é:", index_searched)
