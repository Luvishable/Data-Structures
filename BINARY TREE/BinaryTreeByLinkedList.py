from QUEUE import queueByLinkedList as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# In pre-order traversal, we first visit the root node, then left subtree and right subtree
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# In in-order traversal, we first need left subtree, then root node and then right subtree
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# In post-order traversal, first we'll visit left subtree, then right subtree and then root node
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    inOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# We visit level by level
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)


# Searching a node in a binary tree(we are gonna use levelOrderTraversal to find the given node)
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return 'Binary tree does not exist'
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.data == nodeValue:
            return 'Success'
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
    return 'Not Found'


# When inserting a node in Binary Tree, there are two scenarios:
# - A root node is  blank
# - The tree exists and we have to look for a first vacant place
# We are gonna use levelOrderTraversal because levelOrderTraversal uses queue and it is more performant than stack (other
# traversal methods use recursion,thus, stack is utilized)
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return 'Successfully inserted!'
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return 'Successfully inserted!'


# Deleting a node from binary tree
# When we do levelOrderTraversal, the last node that we will visit will be the deepest node in the binary tree.
# When we are doint deletion, we replace the node that we want to delete with the deepest node in that binary tree
def getDeepestNode(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
    deepestNode = root.value
    return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value is dNode:
            root.value = None
            return
        if root.value.rightChild:
            if root.value.rightChild is dNode:
                root.value.rightChild = None
                return
            else:
                customQueue.enqueue(root.value.rightChild)
        if root.value.leftChild:
            if root.value.leftChild is dNode:
                root.value.leftChild = None
                return
            else:
                customQueue.enqueue(root.value.leftChild)


def deleteNodeBT(rootNode, nodeToDelete):
    if not rootNode:
        return 'The Binary Tree does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeToDelete:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has successfully been deleted"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete the node"


# Deleting the entire binary tree
# When we assign rootNode, rootNode.leftChild and rootNode.rightChild to None, then the children become eligible
# for garbage collector
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The Binary Tree has successfully been deleted'




