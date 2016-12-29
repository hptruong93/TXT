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
