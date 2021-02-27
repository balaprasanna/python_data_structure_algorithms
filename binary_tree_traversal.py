

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.same = None
        self.count = 1

    # def __repr__(self):
    #     return f"{self.left} - {self.val} - {self.right}"

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
            else:
                self.count += 1
                if self.same is None:
                    self.same = Node(val)
                else:
                    self.same.insert(val)
        else:
            self.val = val


class Tree:

    INORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.insert(val)

    def insert_many(self, lst):
        for v in lst:
            self.insert(v)

    def inorder(self, traverse_type, node, store=None):
        if node is None:
            return

        if traverse_type == self.INORDER:
            self.inorder(traverse_type, node.left, store)
            if store: store.append(node.val)
            else: print(node.val, end=" ")
            self.inorder(traverse_type, node.right, store)

        if traverse_type == self.PRE_ORDER:
            if store: store.append(node.val)
            else: print(node.val, end=" ")
            self.inorder(traverse_type, node.left, store)
            self.inorder(traverse_type, node.right, store)

        if traverse_type == self.POST_ORDER:
            self.inorder(traverse_type, node.left, store)
            self.inorder(traverse_type, node.right, store)
            if store: store.append(node.val)
            else: print(node.val, end=" ")

    def inorder_traversal(self):
        result = []
        self.inorder(traverse_type=self.INORDER, node=self.root, store=result)
        print()
        return result

    def inorder_traversal_with_same(self, node):
        if node is None:
            return
        self.inorder_traversal_with_same(node.left)
        print(node.val, end=" ")
        self.inorder_traversal_with_same(node.same)
        self.inorder_traversal_with_same(node.right)

    def print_tree(self, node, sb="", padding="", pointer=""):
        if node is None:
            return ""

        sb += f"{padding}"
        sb += f"{pointer}"
        sb += f"{node.val}"
        sb += "\n"

        paddingBuilder = padding
        paddingBuilder += "│  "

        paddingForBoth = paddingBuilder
        pointerForRight = "└──"
        pointerForLeft = "├──" if node.right is not None else "└──"

        sb += self.print_tree(node.left, sb, paddingForBoth, pointerForLeft)
        sb += self.print_tree(node.right, sb, paddingForBoth, pointerForRight)

        return sb

    def preorder_traversal(self):
        result = []
        self.inorder(traverse_type=self.PRE_ORDER, node=self.root, store=result)
        print()
        return result

    def postorder_traversal(self):
        result = []
        self.inorder(traverse_type=self.POST_ORDER, node=self.root, store=result)
        print()
        return result

    def __repr__(self):
        return f"{self.root}"


if __name__ == '__main__':
    t = Tree()
    t.root = Node(5)
    t.root.left = Node(2)
    t.root.left.left = Node(1)
    t.root.left.right = Node(3)
    t.root.right = Node(8)
    t.root.right.left = Node(6)
    t.root.right.right = Node(10)
    # tree
    #         5
    #     2       8
    # 1       3  6   10

    # t.insert_many([1, 2, 3, 4, 0])

    t.inorder_traversal()
    t.preorder_traversal()
    t.postorder_traversal()

    t2 = Tree()
    t2.insert(5)
    t2.insert(2)
    t2.insert(1)
    t2.insert(3)
    t2.insert(8)
    t2.insert(6)
    t2.insert(10)

    t2.inorder_traversal()

    t3 = Tree()
    t3.insert_many([1,5,7,1,3,6,20,6,2])
    t3.inorder_traversal_with_same(t3.root)

    print(t3.print_tree(t3.root))
