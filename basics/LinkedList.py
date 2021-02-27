class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def next_node(self):
        yield self.next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        curr_head = self.head
        self.head = new_node
        new_node.next = curr_head

    def add_items(self, items):
        for item in items:
            self.add(item)

    def next(self):
        h = self.head
        while True:
            if h is None:
                # print("No more nodes to traverse")
                break
            else:
                yield h
                h = h.next

    def traverse(self):
        for v in self.next():
            print("{} -> ".format(v.val), end=" ")
        print()

    def _traverse_v0(self):
        h = self.head
        while True:
            if h is None:
                print("No more nodes to traverse")
                break
            else:
                print("Value => {}".format(h.val))
                h = h.next

    def detect_loop(self):
        hash_map = set()
        for node in self.next():
            if node in hash_map:
                return True
            hash_map.add(node)
        return False

    def detect_loop_v2(self):
        """Floyd’s Cycle-Finding Algorithm"""
        p1 = self.head
        p2 = self.head
        cycle_found = False

        while True:
            if p1 is None or p1.next is None:
                break

            if p2 is None or p2.next is None or p2.next.next is None:
                break

            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                cycle_found = True
                break

        return cycle_found


if __name__ == '__main__':
    list1 = SinglyLinkedList()
    list1.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    e4 = Node("Thur")

    list1.head.next = e2
    e2.next = e3
    e3.next = e4

    e3.next = e2

    print(list1.detect_loop_v2())
    if list1.detect_loop_v2():
        print("Loop found")
    else:
        print("No loop found")
        list1.traverse()
