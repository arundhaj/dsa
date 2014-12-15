# Linked list implementation
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


class SinglyLinkedList:
    def __init__(self):
        self.first = None

    # empty()
    # size()
    # get(index)
    # indexOf(x)
    # erase(index)
    # insert(index, x)
    # traversal

    def empty(self):
        self.first = None

    def isEmpty(self):
        return self.first == None

    def insert(self, index, newNode):
        if self.isEmpty():
            # if empty list
            self.first = newNode
        else:
            currentNode = self.first
            prevNode = None
            i = 1
            while(i < index):
                prevNode = currentNode
                currentNode = currentNode.next
                i += 1

            if prevNode == None:
                # print 'first node'
                newNode.next = self.first
                self.first = newNode
            else:
                prevNode.next = newNode
                newNode.next = currentNode

    def traversal(self):
        currentNode = self.first
        while ( currentNode != None ):
            print currentNode.getData()
            currentNode = currentNode.next

    def size(self):
        i = 0
        currentNode = self.first
        while ( currentNode != None ):
            currentNode = currentNode.next
            i += 1

        return i

    def erase(self, index):
        pass


# linked list operations
linked_list = SinglyLinkedList()

insert_array = [54, 26 , 93, 17, 77, 31]

# push items into the stack
for item in insert_array:
    newnode = Node(item)
    # print newnode.getData()
    linked_list.insert(0, newnode)

linked_list.traversal()
linked_list.insert(2, Node(23))
print ' '
linked_list.traversal()
# print linked_list.size()
