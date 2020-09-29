class node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.count = 1


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            cur_node.count += 1

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value), cur_node.count)
            self._print_tree(cur_node.right)


tree = BST()
with open("letter frequency.txt") as f:
    for line in f:
        for ch in line:
            if ch.isalpha():
                tree.insert(ch.upper())

tree.print_tree()
