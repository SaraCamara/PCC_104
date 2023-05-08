# Implementação do algoritmo QuickSort
# Operação básica: Comparação para encontrar o menor elemento em relação ao pivo


def quick_sort(array, begin, end):
    if begin < end:
        p = partition(array, begin, end)
        quick_sort(array, begin, p-1)
        quick_sort(array, p+1, end)


def partition(array, begin, end):
    pivot = array[end]
    i = begin
    for j in range(begin, end):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i


array = [-5, 2, 8, 0, 3]
begin, end = 0, len(array)-1

print("Arranjo:", array)
quick_sort(array, begin, end)
print("Arranjo ordenado:", array)