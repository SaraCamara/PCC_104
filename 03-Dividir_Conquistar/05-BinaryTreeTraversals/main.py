# Implementação do algoritmo recursivo que encontra o tamanho de uma BinaryTre
# Operação básica: Verificação se há elementos a esquerda ou direita na árvore

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

    # Preorder traversal: raiz, subarvore esquerda e subarvore direita
    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # Postorder traversal: subarvore esquerda, subarvore direita e raiz
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)

    # Inorder traversal: subarvore esquerda, raiz e subarvore direita
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()

tree = Node(12)
tree.insert_node(5)
tree.insert_node(24)
tree.insert_node(15)
tree.insert_node(10)
tree.insert_node(3)
tree.insert_node(1)


print("Caminhamento em Preorder é:")
tree.preorder()

print("Caminhamento em Postorder é:")
tree.postorder()

print("Caminhamento em Inorder é:")
tree.inorder()

