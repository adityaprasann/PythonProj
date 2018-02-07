class BSTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            self.root = BNode(data)
        else:
            if data <= root.data:
                if root.ltree:
                    self._insert(root.ltree, data)
                else:
                    root.ltree = BNode(data)
            elif data > root.data:
                if root.rtree:
                    self._insert(root.rtree, data)
                else:
                    root.rtree = BNode(data)


class BNode(object):

    def __init__(self, data):
        self.data = data
        self.ltree = None
        self.rtree = None


def displayInOrder(root):
    if root is not None:
        displayInOrder(root.ltree)
        print(root.data)
        displayInOrder(root.rtree)


def displayPreOrder(root):
    if root is not None:
        print(root.data)
        displayPreOrder(root.ltree)
        displayPreOrder(root.rtree)


def displayPostOrder(root):
    if root is not None:
        displayPostOrder(root.ltree)
        displayPostOrder(root.rtree)
        print(root.data)


b = BSTree()
b.insert(8)
b.insert(5)
b.insert(3)
b.insert(7)
b.insert(10)
b.insert(15)
b.insert(2)
print("Original Tree : ")
displayInOrder(b.root)
print("Original Pre Order Tree : ")
displayPreOrder(b.root)
print("Original Post Order Tree : ")
displayPostOrder(b.root)
