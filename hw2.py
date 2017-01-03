Phuoc sensei

# A linked list has the following structure:

class Node():
    def __init__(self, value):
        self.next = None
        self.value = value
        
# Example of creating linked list:
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

three.next = four
four.next = five
five.next = six

# Given the head node of a linked list, print the value of all nodes in the linked list in order
def print_linked_list(head_node):
    pass
# For example, using print_linked_list(three) should print
# 3
# 4
# 5
# 6


# Given the head node of a linked list, reverse the linked list without creating any additional list. This method should return
# the head node of the reversed linked list (i.e. the last node of the original linked list)
def reverse_list(head_node):
    pass
    
# Example, using print_linked_list(reverse_list(three)) should produce:
# 6
# 5
# 4
# 3


# Given two ordered arrays, merge them into a third ordered array by creating a new array. Return this newly created array
# Example: merge([1,5,7], [3,6,7]) should produce [1,3,5,6,7,7]
def merge(arr1, arr2):
   pass


# Implement a stack with a link list.
head_node = Node(1)

# Push method modifies the linked list so that a new value is put at the head of the linked list.
# The method returns a new linked list whose top value is the new top value in the stack.
def stack_push(head, value):
    if head is None:
        return Node(value)
    
    new_head = Node(value)
    new_head.next = head
    return new_head

# Pop method modifies the linked list so that the value at the head of the list is removed.
# The method returns a new linked list whose top value is the new top value in the stack.
# If the list has only 1 element (and so is the stack), return None as there is nothing left in the stack.
# No need to take care of the case where we pop from an empty stack.
def stack_pop(head):
    pass

# Peek method does not modify the linked list. It returns the value of the node at the head of the list (i.e. the top of stack).
def stack_peek(head, value):
    pass
