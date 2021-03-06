import sys
sys.path.append('./stack')
from stack import Stack
sys.path.append('./my_queue') # change name of file to my_queue because Python 3 already has a queue module
from my_queue import Queue # Python finds that queue.py file before it finds your queue.py

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: # is this value less than self.value (ROOT)
            if self.left is None: # if left is empty (none)
                self.left = BSTNode(value) # create a new node and put it on the left
            else:
                self.left.insert(value) # otherwise, compare it to the current value and possibly insert on the left
        elif value >= self.value: # is this value greater than or equal to self.value (ROOT)
            if self.right is None: # if right is empty (none)
                self.right = BSTNode(value) # create a new node and put it on the right
            else:
                self.right.insert(value) # otherwise, compare it to the current value and possibly insert on the right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None: # if the right side is None
            return self.value # then that is the highest value
        else: # otherwise keep going
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # call the function
        if self.left is not None: # if it's not none on the left side
            self.left.for_each(fn) # then CALL the function, and pass in fn
        if self.right is not None: # if it's not none on the right side
            self.right.for_each(fn) # then CALL the function, and pass in fn
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node): # think, most left is next in line
        if node.left is not None: # if left has a value
            self.in_order_print(node.left) # do recursion on this left node
        print(node.value) # once done recursing, print the value...proceed to the right side
        if node.right is not None: # if right has a value
            self.in_order_print(node.right) # do recursion on this right node
        return # ya done

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue() # do not use recursion, use a queue
        queue.enqueue(node) # start queue with root node
        while len(queue) > 0: # while loop that checks size of queue
            node = queue.dequeue() # FIFO
            print(node.value) # print the current node's value
            if node.left is not None: # pointer variable that updates at the beginning of each loop
                queue.enqueue(node.left) # push it on the queue, go through the loop again
            if node.right is not None: # pointer variable that updates at the beginning of each loop
                queue.enqueue(node.right) # push it on the queue, go through the loop again

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack() # use a stack
        stack.push(node) # start your stack with your root node
        while len(stack) > 0: # while loop that checks stack size
            if node is None: # check to see if empty
                return # get outta here
            node = stack.pop() # LIFO
            print(node.value) # print the current node's value
            if node.left is not None: # pointer variable that updates at the beginning of each loop
                stack.push(node.left) # push it on the stack, go through the loop again
            if node.right is not None: # pointer variable that updates at the beginning of each loop
                stack.push(node.right) # push it on the stack, go through the loop again

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
