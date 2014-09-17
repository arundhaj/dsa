# Implementation of Stack based on singly linked list.
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getNext(self):
        return self.next

class StackLinkedList:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 0
            startnode = self.top
            while startnode != None:
                count += 1
                startnode = startnode.next

            return count

    # push an item to the top
    def push(self, newnode):
        if self.isEmpty():
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    # pop an item from the top
    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp

    # traverse the stack from top to bottom, it is not part of stack ADT
    def traversal(self):
        if self.isEmpty() is False:
            startnode = self.top
            while startnode != None:
                print startnode.getData()
                startnode = startnode.next

# stack operations
stack_linked = StackLinkedList()

insert_array = [54, 26, 93, 17, 77, 31]

# push items into the stack
for item in insert_array:
    newnode = Node(item)
    stack_linked.push(newnode)

# traverse the stack
# stack_linked.traversal()

# check the size of the stack
print stack_linked.size()
temp_node = stack_linked.pop()
# print temp_node.getData()
print stack_linked.size()
