# In python a set is initialized with
the_set = set()

# Usage of set is simple
the_set.add(1)
the_set.add(2)

for num in the_set:
    print("We have number %s in the set." % num)

if 2 in the_set:
    print("2 is in the set")
the_set.remove(2)
if 2 not in the_set:
    print("2 is not in the set")

# Map in python is called dictionary
the_map = {}

# Usage of map is simple
key = 3
value = 'hello'
the_map[key] = value
the_map[7] = 'how are you'

if 3 in the_map:
    print("3 is in the map with value %s" % the_map[3])

# Remove from the map
the_map.pop(3)
if 3 not in the_map:
    print("3 is not in the map")
    
# To iterate through all elements in the map
for key, value in the_map.items():
    print("Found pair %s,%s in the map" % (key, value))
    
# Special functions for map
all_keys = the_map.keys()
all_values = the_map.values()

######################################################################
# Write a function to find the character with maximum occurence in a string using map
data = 'Praesent id libero consequat, feugiat lacus eu, mollis sapien. Ut ut lacus iaculis, gravida ex quis, suscipit ipsum. Fusce vel augue ut eros pulvinar porta. Sed eu nunc sit amet nisl egestas tempus. Maecenas finibus mollis justo, elementum bibendum risus tempus vitae. Quisque ex risus, placerat at finibus quis, pretium ac nisl. Quisque vel accumsan ex, sed pellentesque odio. Nunc vel metus vitae lacus porta pretium id ac arcu. Phasellus hendrerit, arcu at pellentesque cursus, sem diam mollis neque, nec pretium urna est eget mauris. Vestibulum nec augue tristique, tristique ante vitae, vestibulum sem. Vestibulum lectus ipsum, commodo quis scelerisque sagittis, elementum sit amet ipsum. Morbi pulvinar quis ante nec ullamcorper. Fusce ut odio tincidunt, pharetra eros non, semper mauris.'
def maximum_occurence_char(string):
    return 'a'
    
# Given an unordered array with some duplicates, create a new array without the duplicates (contains all distinct elements from 
# the original array). Hint: use set

array = [1,2,2,4,4,7,7,5,2,1,4,8,9,3,5,3,6,8,3,1]
def remove_duplicate(array):
    pass

# Use merge sort to sort 2 linked list.
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

six.next = four
four.next = five
five.next = one
one.next = three
three.next = two
head_node = six

# The idea is as follow:
# 1. Split the list into 2 small lists
# 2. Sort the two lists using recursion. Base easy case when the list has only 1 element.
# 3. Merge the two sorted list into the result
# Example: http://www.geeksforgeeks.org/merge-sort-for-linked-list/
def merge_sort_linked_list(head):
    pass

new_head = merge_sort_linked_list(head_node) # Should be sorted now

# Write a function to create a reversed map of a map. For example:
# the_map = { 1 : 2, 2 : 3, 3 : 4, 7 : 10 }
# reversed_map = { 2 : 1, 3 : 2, 4 : 3, 10 : 7 }
def create_reversed_map(the_map):
    pass

create_reversed_map({ 1 : 2, 2 : 3, 3 : 4, 7 : 10 })

# Investigate why in python a list cannot be a key for dictionary, but a string can.


