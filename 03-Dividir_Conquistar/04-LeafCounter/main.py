# Implementação do algoritmo recursivo que encontra o tamanho de uma BinaryTre
# Operação básica: Soma recursiva dos numeros de folhas (nó).

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

    def leaf_count(self):
        if self.left is None and self.right is None:
            return 1

        if self.left and self.right:
            return 1 + (self.left.leaf_count() + self.right.leaf_count())
        if self.left and not self.right:
            return 1 + self.left.leaf_count()
        if self.right and not self.left:
            return 1 + self.right.leaf_count()


tree = Node(12)
tree.insert_node(5)
tree.insert_node(24)
tree.insert_node(15)
tree.insert_node(10)
tree.insert_node(3)
tree.insert_node(1)


size = tree.leaf_count()
print("O tamanho da árvore é:", size)