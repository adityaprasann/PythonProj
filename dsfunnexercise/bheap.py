class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,ele):
        self.heapList.append(ele)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, idx):
        while idx // 2 > 0:
            cur = self.heapList[idx]
            par = self.heapList[idx//2]
            if cur < par:
                self.swap(idx, idx//2)
            idx = idx // 2

    def swap(self, idx, paridx):
        t = self.heapList[paridx]
        self.heapList[paridx] = self.heapList[idx]
        self.heapList[idx] = t

    def delMin(self):
        ret = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return ret

    def percDown(self,idx):
        while idx * 2 <= self.currentSize:
            minIdx = self.findMin(idx)
            cur = self.heapList[idx]
            par = self.heapList[minIdx]
            if cur > par:
                self.swap(idx, minIdx)
            idx = minIdx

    def findMin(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

bh = BinHeap()


bh.insert(18)
bh.insert(19)
bh.insert(21)
bh.insert(17)
bh.insert(27)
bh.insert(33)
bh.insert(11)
bh.insert(14)
bh.insert(9)
bh.insert(5)

print(bh.heapList)

print(bh.delMin())

print(bh.heapList)