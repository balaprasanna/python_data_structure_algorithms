
from base import Sorting


class BinaryTreeMap:

    class Node:
        def __init__(self, val):
            self.val = val
            self.freq = 1
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self, values=None):
        self.root = None
        if values:
            for v in values:
                self.insert_util(v)

    # def insert(self, val):
    #     if self.root is None:
    #         self.root = self.Node(val)
    #         return
    #
    #     curr_node = self.root
    #     while curr_node:
    #         if val < curr_node.val:
    #             if curr_node.left:
    #                 curr_node = curr_node.left
    #             else:
    #                 new_node = self.Node(val)
    #                 new_node.parent = curr_node
    #                 curr_node.left = new_node
    #                 return
    #         elif val > curr_node.val:
    #             if curr_node.right:
    #                 curr_node = curr_node.right
    #             else:
    #                 new_node = self.Node(val)
    #                 new_node.parent = curr_node
    #                 curr_node.right = new_node
    #                 return
    #         else:
    #             # duplicate keys - so increment by 1
    #             curr_node.freq += 1
    #             return

    def insert_util(self, val):
        if self.root is None:
            self.root = self.Node(val)
            return
        else:
            self.insert_recursive(curr_node=self.root, val=val)

    def insert_recursive(self, curr_node, val):
        if val < curr_node.val:
            if curr_node.left:
                self.insert_recursive(curr_node.left, val)
            else:
                new_node = self.Node(val)
                new_node.parent = curr_node
                curr_node.left = new_node
        elif val > curr_node.val:
            if curr_node.right:
                self.insert_recursive(curr_node.right, val)
            else:
                new_node = self.Node(val)
                new_node.parent = curr_node
                curr_node.right = new_node
        else:
            # duplicate keys - so increment by 1
            curr_node.freq += 1

    def in_order_traversal(self):
        arr = []
        self._inorder(self.root, arr)
        return arr

    def _inorder(self, node, arr):
        if node is None:
            return

        self._inorder(node.left, arr)
        # to handle duplicates
        for _ in range(node.freq):
            arr.append(node.val)
        self._inorder(node.right, arr)

    def locate_node(self, node, key):
        if node is None:
            return
        if key < node.val:
            return self.locate_node(node.left, key)
        elif key > node.val:
            return self.locate_node(node.left, key)
        else:
            return node

    def get(self, key, default_value_if_not_found=None):
        node = self.locate_node(node=self.root, key=key)
        if node:
            return node.freq
        else:
            return default_value_if_not_found

    def put(self, key):
        self.insert_util(key)


class CountingSort(Sorting):

    def sort(self, arr):
        # tree_map = BinaryTreeMap(arr)
        # return tree_map.in_order_traversal()
        tm = BinaryTreeMap()
        for val in arr:
            tm.put(val)

        for val in arr:
            print(f"val = {val}, freq = {tm.get(val)}")

        return tm.in_order_traversal()


if __name__ == '__main__':
    CountingSort().test(10)
