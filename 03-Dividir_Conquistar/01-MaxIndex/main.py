# Implementação de divisão e conquista para encontrar a posição do maior elemento de um arranjo de n elementos
# Operação básica: Comparação para encontrar o maior elemento

def maximo(array, begin, end):
    if end - begin <= 1:
        if array[begin] > array[end]:
            return begin
        else:
            return end
    else:
        mid = begin + end // 2
        max1 = maximo(array, begin, mid)
        max2 = maximo(array, mid+1, end)
        if array[max1] > array[max2]:
            return max1
        else:
            return max2


array = [9, 9, 8, 8, 8]
begin, end = 0, len(array)-1

print("Arranjo:", array)
max_index = maximo(array, begin, end)
print("A posição do elemento de maior valor do array é:", max_index)