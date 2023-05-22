# Description: Return the nth element from the last in a singly linked list

from linkedList import LinkedList


def nth_from_last(linked_list, n):
    pointer1 = linked_list.head
    pointer2 = linked_list.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

