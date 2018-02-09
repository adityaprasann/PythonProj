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


def displayInOrder(root, res):
    if root is not None:
        displayInOrder(root.ltree, res)
        res.append(root.data)
        displayInOrder(root.rtree, res)
    return res


def displayPreOrder(root, res):
    if root is not None:
        res.append(root.data)
        displayPreOrder(root.ltree, res)
        displayPreOrder(root.rtree, res)
    return res


def displayPostOrder(root, res):
    if root is not None:
        displayPostOrder(root.ltree, res)
        displayPostOrder(root.rtree, res)
        res.append(root.data)
    return res

def displayLevelOrder(root, res):
    curr = [root]
    while curr:
        nextLvl = []
        tempres = []
        for n in curr:
            tempres.append(n.data)
            if(n.ltree):
                nextLvl.append(n.ltree)
            if(n.rtree):
                nextLvl.append(n.rtree)
        curr = nextLvl
        res.append(tempres)
    return res

def trimTree(root, min, max):
    if not root:
        return
    root.ltree = trimTree(root.ltree, min, max)
    root.rtree = trimTree(root.rtree, min, max)

    if(min <= root.data <= max):
        return root
    if(root.data <= min):
        return root.rtree
    if(root.data >= max):
        return root.ltree


def isValidBST(root, floor=float('-inf'), ceil=float('inf')):
    if root is None:
        return True
    else:
        return (floor <= root.data <= ceil) and isValidBST(root.ltree, floor, root.data) and isValidBST(root.rtree,
                                                                                                        root.data, ceil)


def isValidBSTSort(root):
    out = displayInOrder(root, [])
    if out == sorted(out):
        return True
    return False


b = BSTree()
b.insert(8)
b.insert(5)
b.insert(3)
b.insert(7)
b.insert(10)
b.insert(15)
b.insert(2)
print("Original Tree : ")
print(displayInOrder(b.root, []))
print("Original Pre Order Tree : ")
print(displayPreOrder(b.root, []))
print("Original Post Order Tree : ")
print(displayPostOrder(b.root, []))
print("Original Level Order Tree : ")
print(displayLevelOrder(b.root, []))
print("Valid BST ck : ")
print(isValidBST(b.root))

nb = BNode(8)
nb.ltree = BNode(9)
nb.ltree.ltree = BNode(1)
nb.ltree.rtree = BNode(2)
nb.rtree = BNode(7)
nb.rtree.ltree = BNode(12)
nb.rtree.rtree = BNode(9)
print(isValidBST(nb))
print(isValidBSTSort(b.root))
print(isValidBSTSort(nb))

print(displayInOrder(trimTree(b.root, 3, 10),[]))