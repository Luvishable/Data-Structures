class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The DLL has been created successfully.'

    # Insertion method in DoublyLL
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print('The node cannot be inserted')
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
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

    # Traversal method in Doubly Linked List
    def traverseDLL(self):
        if self.head is None:
            print('There is not any element to traverse')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse Traversal method in DoublyLL
    def reverseTraversalDLL(self):
        if self.head is None:
            print('There is not any element to traverse')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search method in DoublyLL
    def searchDLL(self, nodeValue):
        if self.head is None:
            print('There is not any element to traverse')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return 'The node does not exist in this list'

    # Delete a node from DoublyLL
    def deleteNode(self, location):
        if self.head is None:
            print('There is not any element to traverse')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print('The node has been successfully deleted')

    # Delete the entire Doubly Linked List
    def deleteDLL(self):
        if self.head is None:
            print('There is not any element to traverse')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print('The DLL has been successfully deleted')
