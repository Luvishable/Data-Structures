"""
What is a BST?

- In the left subtree, the value of a node is less than or equal to its parent node's value.
- In the right subtree, the value of a node is greater than or equal to its parent node's value
- It performs better than binary tree in inserting and deleting nodes

Traversal of BST
- Depth First Search = Preorder Traversal, Inorder Traversal, Post Order Traversal
- Breadth First Search = Level Order Traversal
"""
from QUEUE import queueByLinkedList as queue


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has successfully been inserted"


# First rootNode then left subtree and then right subtree is visited
def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# First left subtree then rootNode and then right subtree is visited
def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# First left subtree then right subtree and then rootNode is visited
def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.rightChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# Level by level traversal is done by using queues
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print('The value found')
        else:
            searchNode(rootNode.rightChild, nodeValue)


# Deleting a node from BST
# There are 3 cases:
# 1) The node to be deleted is a leaf node
# 2) The node has 1 child
# 3) The node has 2 children

# We need a method to find the minimum value
def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    # If the key to be deleted is smaller than the root's key then it lies in  left subtree
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    # If the kye to be delete is greater than the root's key then it lies in right subtree
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    # If key is same as root's key, then this is the node to be deleted
    else:
        # Node with only one child or no child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        # Node with two children:
        # Get the inorder successor (smallest in the right subtree)
        temp = minValueNode(rootNode.rightChild)
        # Copy the inorder successor's content to this node
        rootNode.data = temp.data
        # Delete the inorder successor
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode


# Deleting entire BST
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BST has successfully deleted'

