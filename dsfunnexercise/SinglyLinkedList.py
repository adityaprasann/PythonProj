class SNode(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

    def reverse(head):
        current = head
        previous = None
        nextnode = None
        while current:
            nextnode = current.nextnode
            current.nextnode = previous

            previous = current
            current = nextnode
        return previous


    def printlist(head):
        while head:
            print(head.value)
            head = head.nextnode

    def cycle_check(node):
        slow = node
        fast = node
        while fast != None and fast.nextnode != None:
            slow = slow.nextnode
            fast = fast.nextnode.nextnode
            if slow == fast:
                return True
        return False

    def nth_to_last_node(pos,node):
        normal = node
        factor = node
        x=1
        while x <= pos:
            factor = factor.nextnode
            x += 1
        while factor:
            factor = factor.nextnode
            normal = normal.nextnode
        return normal

a = SNode(1)
b = SNode(2)
c = SNode(3)

a.nextnode = b
b.nextnode = c

s = SNode
s.printlist(a)

s.printlist(s.reverse(a))

print(s.cycle_check(a))

a.nextnode = b
b.nextnode = c
c.nextnode = a

print(s.cycle_check(a))

a = SNode(1)
b = SNode(2)
c = SNode(3)
d = SNode(4)
e = SNode(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print((s.nth_to_last_node(2, a)).value)