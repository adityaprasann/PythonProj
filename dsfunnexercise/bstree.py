class BSTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self._insert(self.root, data)

    def _insert(self, root, data):
        if root == None:
            self.root = BNode(data)
        else:
            if (data <= root.data):
                if (root.ltree):
                    self._insert(root.ltree, data)
                else:
                    root.ltree = BNode(data)
            elif (data > root.data):
                if (root.rtree):
                    self._insert(root.rtree, data)
                else:
                    root.rtree = BNode(data)

    def displayInOrder(self, root):
        while root != None:
            self.displayInOrder(root.ltree)
            print(root.data)
            self.displayInOrder(root.rtree)


class BNode(object):

    def __init__(self, data):
        self.data = data
        self.ltree = None
        self.rtree = None


b = BSTree()
b.insert(8)
b.insert(5)
b.insert(3)
b.insert(7)
b.insert(10)
b.insert(15)
b.insert(2)
print("Original Tree : ")
b.displayInOrder(b.root)
