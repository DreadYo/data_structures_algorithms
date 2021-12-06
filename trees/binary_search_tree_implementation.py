"""
Binary Search Trees are a non-linear data structure.
They consist of a root node and zero, one or two children where the children can again have 0, 1, or 2 nodes
as their children and so on
In most cases, the time complexity of operations on a BST, which include,
lookups, insertions and deletions, take O(log N) time
Except for the worst case, where the tree is heavily unbalanced
with all the nodes being on one side of the tree.
In that case, it basically becomes a linked list and the time complexities go up to O(n)

Lookup      -   O(logn)
Insert      -   O(logn)
Delete      -   O(logn)

"""


class Node:
    """
    A node class to store information about each node
    It stores the data and the pointers to its left and right children
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    """
    Binary Search Tree class
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            cur_node = self.root
            while cur_node:
                # left
                if value < cur_node.value:
                    if cur_node.left is None:
                        cur_node.left = new_node
                        return
                    cur_node = cur_node.left
                # right
                elif value > cur_node.value:
                    if cur_node.right is None:
                        cur_node.right = new_node
                        return
                    cur_node = cur_node.right
                # duplicate
                else:
                    print("Duplicate value")
                    return

    def lookup(self, value):
        cur_node = self.root
        while cur_node:
            if value == cur_node.value:
                return cur_node
            elif value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
        return None

    def remove(self, value):
        # check if tree is empty
        if not self.root:
            print("Tree is empty")
            return
        cur_node, parent_node = self.find_current_and_parent(value)
        # not found
        if not cur_node:
            print("Not Found")
            return
        # 1. Current node doesn't have children
        if self.is_leaf(cur_node):
            # current node is a root node
            if not parent_node:
                self.root = None
            # current node isn't a root node
            else:
                # current node is left child
                if parent_node.value > value:
                    parent_node.left = None
                # current node is right child
                elif parent_node.value < value:
                    parent_node.right = None
        # 2. Current node has only one child
        elif not self.is_has_two_children(cur_node):
            # current node has left child
            if cur_node.left:
                cur_node = cur_node.left
            # current node has right child
            else:
                cur_node = cur_node.right
            # current node is a root node
            if not parent_node:
                self.root = cur_node
            else:
                # current node is left child
                if parent_node.value > value:
                    parent_node.left = cur_node
                # current node is right child
                elif parent_node.value < value:
                    parent_node.right = cur_node
        # 3. Current node has 2 children
        elif self.is_has_two_children(cur_node):
            print("two children")
            # get next node for replace and its parent
            next_node, next_parent = self.find_next_replace(cur_node)
            print(f"next_node = {next_node.value}, next_parent = {next_parent.value}")
            if cur_node != next_parent:
                next_parent.left = next_node.right
            # current node is a root node
            if not parent_node:
                self.root = next_node
            # current node != root
            else:
                # next node is left child
                if parent_node.value > value:
                    parent_node.left = next_node
                # next node is right child
                elif parent_node.value < value:
                    parent_node.right = next_node
            # next node is a left child of current node
            if cur_node.left == next_node:
                next_node.left = None
            # if next node is not a left child of current node
            else:
                # then copy link left child from current node to next node
                next_node.left = cur_node.left
            # next node is a right child of current node
            if cur_node.right == next_node:
                next_node.right = None
            # if next node is not a right child of current node
            else:
                # then copy link right child from current node to next node
                next_node.right = cur_node.right

    def find_next_replace(self, node):
        next_node = node.right
        next_parent = node
        while next_node.left:
            next_parent = next_node
            next_node = next_node.left
        return next_node, next_parent

    def find_current_and_parent(self, value):
        cur_node = self.root
        parent_node = None
        while cur_node:
            if value == cur_node.value:
                break
            else:
                parent_node = cur_node
                if value < cur_node.value:
                    cur_node = cur_node.left
                elif value > cur_node.value:
                    cur_node = cur_node.right
        if not cur_node:
            parent_node = None
        print(f"cur_node = {cur_node}")
        print(f"parent_node = {parent_node}")
        return cur_node, parent_node

    def is_leaf(self, node):
        if node.left or node.right:
            return False
        return True

    def is_has_two_children(self, node):
        if node.left and node.right:
            return True
        else:
            return False


    def print_tree(self):
        if self.root is None:
            print("[Empty tree]")
        else:
            self.print_node(tree.root)

    def print_node(self, node):
        if node is not None:
            print("-", end="")
            self.print_node(node.left)
            print(str(node.value))
            self.print_node(node.right)


def traverse(node):
    tree = {
        "value": node.value
    }
    tree.left = None if node.left is None else traverse(node.left)
    tree.right = None if node.right is None else traverse(node.right)
    return tree


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.print_tree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)

    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    tree.print_tree()

    # print(tree.lookup(4).value)
    print(tree.lookup(9).value)
    # print(tree.lookup(1).value)
    # print(tree.lookup(170).value)
    print(tree.lookup(0))

    print("--------------------")
    tree.print_tree()
    tree.remove(9)
    tree.print_tree()



