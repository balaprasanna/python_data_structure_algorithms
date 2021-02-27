
from LinkedList import SinglyLinkedList


def merge_two_sorted_linked_list(l1, l2):

    merged_ll = SinglyLinkedList()

    l1_next = l1.head
    l2_next = l2.head

    while l1_next is None or l2_next is None:

        if l1_next.val <= l2_next.val:
            merged_ll.add(l1_next.val)
            l1_next = l1_next.next
        elif l1_next.val > l2_next.val:
            merged_ll.add(l2_next.val)
            l2_next = l2_next.next

    if l1_next is not None:
        merged_ll.add(l1_next.val)
        for node in l1_next.next_node():
            if node is None:
                break
            merged_ll.add(node.val)

    if l2_next is not None:
        merged_ll.add(l2_next.val)
        for node in l2_next.next_node():
            if node is None:
                break
            merged_ll.add(node.val)

    return merged_ll


if __name__ == '__main__':
    head1 = SinglyLinkedList()
    head1.add_items([19, 15, 8, 4])
    head1.traverse()

    head2 = SinglyLinkedList()
    head2.add_items([16, 10, 8, 7])
    head2.traverse()

    m = merge_two_sorted_linked_list(head1, head2)
    print("Final merged list ")
    m.traverse()
