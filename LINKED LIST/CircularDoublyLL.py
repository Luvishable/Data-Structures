class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return 'The CDLL is created successfully'

    # Insertion method on CircularDoublyLL
    def insertNode(self, value, location):
        if self.head is None:
            print('The CDLL does not exist')
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return 'The node has successfully been inserted'

    # Traversal of Circular CircularDoublyLL
    def traversalCDLL(self):
        if self.head is None:
            print('The CDLL does not exist')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Reverse Traversal of CircularDoublyLL
    def reverseTraversalCDLL(self):
        if self.head is None:
            print('The CDLL does not exist')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    # Search CircularDoublyLL
    def searchCDLL(self, nodeValue):
        if self.head is None:
            print('The CDLL does not exist')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return 'The value does not exist in CDLL'
                tempNode = tempNode.next

    # Delete a node from CircularDoublyLL
    def deleteNode(self, location):
        if self.head is None:
            print('There is not any node to delete')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print('The node has successfully been deleted')

    # Delete entire CircularDoublyLL
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            # Firstly 'unplug' the Linked List :)
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print('The CDLL has successfully been deleted')
