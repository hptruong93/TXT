#   4
# 2   6
#1 3 5 7

#   4
# 6   2
#7 5 3 1

#root_node = four
#four.right = two
#two.right = one
#two.left = three

#four.left = six
#six.right = five
#six.left = seven




# Invert a binary tree

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
one   = TreeNode(1)
two   = TreeNode(2)
three = TreeNode(3)
four  = TreeNode(4)
five  = TreeNode(5)
six   = TreeNode(6)
seven = TreeNode(7)

root_node = four
four.left = two
two.left  = one
two.right = three

four.right = six
six.left   = five
six.right  = seven



def print_tree(root_node):
    if root_node == None:
        return
    else:
        print(root_node.value)
        print_tree(root_node.left)
        print_tree(root_node.right)

#print_tree(root_node)




def invert_binary_tree(root):
    if root == None:
        return
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)

invert_binary_tree(root_node)
print_tree(root_node)


