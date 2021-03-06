"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None) # create a new node and set head and tail to None
        self.length += 1 # go ahead and increase by 1
        if not self.head and not self.tail: # if it's not the head or tail
            self.head = new_node # set both the head and tail to the new node
            self.tail = new_node
        else: # otherwise 
            new_node.next = self.head # declare that the new node next will point to the original head
            self.head.prev = new_node # declare that the original head prev will point to the new node
            self.head = new_node # now declare the head as the new node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value # declare a varibale for the value of self.head
        self.delete(self.head) # delete the head
        return value # return the value of the node that you deleted

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail: # check to see if empty DLL
            self.head = new_node # set the head and tail to the new node because it's empty
            self.tail = new_node
        else: # otherwise if it's not empty
            new_node.prev = self.tail # make the new node point (prev) to the original tail
            self.tail.next = new_node # make the original tail point (next) to the new node
            self.tail = new_node # make the new node the new tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail) # delete tail from DLL
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head: # if the node is the head
            return # then don't do anthing, it's already at the front
        value = node.value # make a variable to store node.value
        if node is self.tail: # if the node is at the end (tail)
            self.remove_from_tail() # remove it from the tail...you will add the value later
        else: # otherwise
            node.delete() # delete the node...you will add the value later
            self.length -= 1 # decrease by 1
        self.add_to_head(value) # add to the front (head), no need to increase by 1 because the method does that for you

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail: # if the node is the tail
            return # then don't do anthing, it's already at the end
        value = node.value # make a variable to store node.value
        if node is self.head: # if the node is at the front (head)
            self.remove_from_head() # remove it from the head
            self.add_to_tail(value) # and add the value as the tail
        else:
            node.delete() # delete the node...you will add the value later
            self.length -= 1 # decrease by 1
            self.add_to_tail(value) # add to the end (tail), no need to increase by 1 because the method does that for you

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail: # check to see if empty
            return # if empty, there is nothing to delete, so return
        self.length -= 1 # when deleting, decrease by 1
        if self.head == self.tail: # if DLL has 1 element, remove it
            self.head = None # by setting head and tail to None
            self.tail = None
        elif self.head == node: # if node is the head
            self.head = node.next # set DLL head pointer to next
            node.delete() # remove node connections 
        elif self.tail == node: # if node is the tail
            self.tail = node.prev # set DLL tail pointer to prev
            node.delete() # remove node connections
        else: # more than 3 nodes, not head or tail
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head: # if empty, return None
            return None
        max_value = self.head.value # declare a variable for max value, set it to the current head.value
        original = self.head # declare a variable for the original head
        while original: # loop through
            if original.value > max_value: # if the original is greater than the max
                max_value = original.value # then make the max the original value (since it's greater)
            original = original.next # set the next 
        return max_value # return the greatest value