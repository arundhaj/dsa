# Implementation of Queue based on singly linked list.
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return self.front == None and self.back == None

    def size(self):
        if self.isEmpty():
            return 0
        else:
            startnode = self.front
            count = 0
            while(startnode != self.back):
                count += 1
                startnode = startnode.next
            return count

    # add node at the back of the queue
    def enqueue(self, newnode):
        if self.isEmpty():
            # point both front and back pointer to the new node
            self.front = newnode
            self.back = newnode
        else:
            self.back.next = newnode
            self.back = newnode

    # remove node from the front of the queue
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None

            return temp

    # traverse the queue from front to back, it is not part of queue ADT
    def traversal(self):
        if self.isEmpty() is False:
            startnode = self.front
            while startnode != self.back:
               print startnode.getData()
               startnode = startnode.next

# Queue operations
queue_linked = QueueLinkedList()

insert_array = [54, 26, 93, 17, 77, 31]

# push items into the queue
for item in insert_array:
    newnode = Node(item)
    queue_linked.enqueue(newnode)

print queue_linked.size()

# traverse the queue
# queue_linked.traversal()

# dequeue
tempnode = queue_linked.dequeue()

# traverse the queue
# queue_linked.traversal()

print queue_linked.size()
