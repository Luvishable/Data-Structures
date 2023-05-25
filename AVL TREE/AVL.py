"""
An AVL tree is a self-balancing Binary Search Tree where the difference between heights of left and right subtrees
cannot be more than one for all nodes.

INSERTION IN AVL TREE

=> When inserting a node in AVL Tree, there are two cases: Rotation required and rotation not required
=> Rotation is required when the tree is disbalanced.

Left-Left Condition:
=> In this insertion type, we make right rotation in order to make the tree balanced
rotateRight(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalanced.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    update the height of disbalancedNode and newRoot
    return newRoot
=> Time Complexity: O(1)
=> Space Complexity: O(1)


Left-Right Condition:
=> Step1: rotate Left disbalancedNode.leftChild
   Step2: rotate Right disbalancedNode

rotateLeft(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    update the height of disbalancedNode and newRoot
    return newRoot

rotateRight(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalanced.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    update the height of disbalancedNode and newRoot
    return newRoot

=> Time Complexity: O(1)
=> Space Complexity: O(1)

NOTE: There are also 2 more conditions which is Right - Right and Right - Left. Since the logic is same and just the
reverse, I did not write them all.

"""

from QUEUE import queueByLinkedList as queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('The value found')
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print('The value found')
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print('The value found')
        else:
            searchNode(rootNode.rightChild, nodeValue)


# The next four functions are helper for insertNode method
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.RightChild))
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.RightChild))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"