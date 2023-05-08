# Implementação do algoritmo MergeSort
# Operação básica: Comparação para encontrar o menor elemento

def merge_sort(array, begin, end):
    if begin < end:
        mid = (begin + end) // 2
        merge_sort(array, begin, mid)
        merge_sort(array, mid + 1, end)
        merge(array, begin, mid, end)

def merge(array, begin, mid, end):
    i = begin
    j = mid + 1
    aux = []
    while i <= mid and j <= end:
        if array[i] < array[j]:
            aux.append(array[i])
            i += 1
        else:
            aux.append(array[j])
            j += 1
    aux += array[i:mid+1]
    aux += array[j:end+1]
    array[begin:end+1] = aux


array = [-5, 2, 8, 0, 3]
begin, end = 0, len(array)-1

print("Arranjo:", array)
merge_sort(array, begin, end)
print("Arranjo ordenado:", array)
