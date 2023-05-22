class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            # we must stop just before the loop starts over again.
            if node == self.tail.next:
                break

    # Creation of a CircularSinglyLL
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        print("The CSLL has been created")

    # Insertion of a node in CircularSinglyLL
    def insertCSLL(self, value, location):
        if self.head is None:
            return 'The head reference is None'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return 'The node has been successfully inserted!'

    # Traversal of a node in CircularSinglyLL
    def traversalCSLL(self):
        if self.head is None:
            print('There is not any element for traversal')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Searching for a node in a CircularSinglyLL
    def searchCSLL(self, nodeValue):
        if self.head is None:
            print('There is not any node in this CSLL')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return 'The node does not exist in this CSLL'

    # Delete a node from CircularSinglyLL
    def deleteNode(self, location):
        # If the CSLL is empty
        if self.head is None:
            print("There is not any node in this CSLL")
        # CSLL not empty
        else:
            if location == 0:
                # if there is only one node in the CSLL
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                # else there is more than one node in the CSLL
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            # if the node that we wanna delete is at the end of the CSLL
            elif location == -1:
                # if the CSLL has only one node
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                # else there is more than one node
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete entire CircularSinglyLL
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None



