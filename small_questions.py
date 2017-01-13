# Invert a binary tree

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)

root_node = four
four.left = two
two.left = one
two.right = three

four.right = six
six.left = five
six.right = seven

  
def invert_binary_tree(root):
  pass
