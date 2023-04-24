# Implementação do algoritmo Binary Search Tree e os métodos buscar e inserir
# Operação básica do método de busca e inserção: Comparação do valor com o nó.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert_node(self, key):
        if key < self.value:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert_node(key)
        elif key > self.value:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert_node(key)

    def search_node(self, key):
        if key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search_node(key)
        elif key > self.value:
            if self.right is None:
                return False
            else:
                return self.right.search_node(key)
        else:
            return True


tree = Node(12)
tree.insert_node(5)
tree.insert_node(10)
tree.insert_node(24)
tree.insert_node(15)
tree.insert_node(12)

if tree.search_node(11):
    print("Nó na árvore.")
else:
    print("Nó buscado não esta na árvore.")
