from linkedList import LinkedList


def remove_duplicates(linked_list):
    if linked_list.head is None:
        return
    currentNode = linked_list.head
    visited = {currentNode.value}
    while currentNode.next:
        if currentNode.next.value in visited:
            currentNode.next = currentNode.next.next
        else:
            visited.add(currentNode.next.value)
            currentNode = currentNode.next
    return linked_list


if __name__ == '__main__':
    customLL = LinkedList()
    customLL.generate(10, 0, 99)
    print(customLL)
    remove_duplicates(customLL)
    print(customLL)
