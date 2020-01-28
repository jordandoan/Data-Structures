import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            node = self.find_node(self.left, value)
        else:
            node = self.find_node(self.right, value)
        if not node:
            node = self
        if node.value < value:
            node.right = BinarySearchTree(value)
        else:
            node.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while current:
            if current.value == target:
                return True
            if current.value < target:
                current = current.right
            else:
                current = current.left
        return False
    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    def find_node(self, node, target):
        if not node:
            return None
        if node.value > target:
            new_node = self.find_node(node.left, target)
        else:
            new_node = self.find_node(node.right, target)
        if not new_node:
            return node
        else:
            return new_node
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return None
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.len():
            for _ in range(q.len()):
                node = q.dequeue()
                print(node.value)
                if node.left:
                    q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.len():
            for _ in range(s.len()):
                node = s.pop()
                print(node.value)
                if node.right:
                    s.push(node.right)
                if node.left:
                    s.push(node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return None
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node:
            return None
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
