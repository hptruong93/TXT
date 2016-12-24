
if __name__ == "__main__":
    
    ############### Array
    # Access time is O(1)
    arr = [1, 3, 5, 4, 7, 6, 7, 2, None]

    # Insert takes O(n) on average
    new_arr = [1, 6, 3, 5, 4, 7, 6, 7, 2]
    
    ############### Linked list / Singly linked list
    # Access time is O(n)
    # X1 X2 ... Xn
    # X1 --> X2, X2 --> X3, X3 --> X4, ..., Xn-1 --> Xn
    # Only provided head_node

    ###12345XX
    #1#2#346X5

    # Insert takes O(n) on average
    # 1 -> 2 -> 4 -> 5
    # 4 -> 1 -> 2 -> 4 -> 5    takes 1 step
    # 1 -> 2 -> 3 -> 4 -> 5    takes 2 steps
    # 1 -> 2 -> 4 -> 5 -> 3    takes 4 steps

    ############### Doubly Linked list
    # 1 <-> 2 <-> 4 <-> 5
    # Both head_node and tail_node might be provided
    # Access time O(1) & insert takes O(n) on average
    
    ############### Min heap
    # L1:       X1
    #          /   \
    # L2:    X2    X3
    #        / \   / \
    # L3:   X4 X5 X6  X7

    # X5 > X2 > X1   Don't know about X4 & X5
    # X6 > X3 > X1   Don't know about X6 & X7

    # Access time takes depth of heap O(log(n))
    # Insert time takes O(log(n))

    # L1:        5
    #          /   \
    # L2:     7     9
    #        /     / \
    # L3:   9     10  10
    # Insert 6
    # L1:        5
    #          /   \
    # L2:     6      9
    #        / \      \
    # L3:   9   7     10
    # Insert 3
    # L1:        3
    #          /   \
    # L2:     6      5
    #        / \    / \
    # L3:   9   7  9  10


    ############### Tree: binary tree, n-ary tree
    # L1:       X1
    #          /   \
    # L2:    X2    X3
    #        / \   /
    # L3:   X4 X5 X6
    #
    # X1: tree root; X1, X2, ... tree nodes
    # X4, X5, X6: leaf nodes
    # X1 is parent of X2, X2 is child of X1

    # Access time: depth of the tree. If balanced ~O(log(n)) where n is number of nodes in tree
    # Max Access time: O(n) where tree is a linked list

    # X1 --> X2 --> X3 --> X4

    ############### Tree: binary search tree
    # L1:       X1
    #          /   \
    # L2:    X2    X3
    #        / \   /
    # L3:   X4 X5 X6
    #
    # Left child is smaller than its parent. Right child is larger than its parent.
    # X2 < X1, X3 > X1. 
    # X4 < X2, X5 > X2, X6 < X3

    # Left branch (left child and its children) have to be less than (or equals to) the current node
    # Right branch (right child and its children) have to be greater than the current node

    # L1:        8
    #          /   \
    # L2:     3     10
    #        / \   /  \
    # L3:   1   6 9   14

    # Access time O(log(n))
    # Insert time O(log(n))
    # Unbalanced tree.

    # 1 --> 3 --> 6 --> 8 --> 9 --> 10 --> 14
    # in_order(8)
    #     in_order(3)
    #         in_order(1)
    #             in_order(None)
    #             print 1
    #             in_order(None)
    #         print 3
    #         in_order(6)

    # Preorder
    # 8 --> 3 --> 1 --> 6 --> 10 --> 9 --> 14
    # Postorder
    # 1 --> 6 --> 3 --> 8 --> 9 --> 14 --> 10

    ############### Tree traversal
    # Given only the root node
    ######## In order traversal
    def in_order(node):
        if node is None:
            return
        in_order(node.left)
        print node.value
        in_order(node.right)

    ######## Pre-order traversal
    def pre_order(node):
        if node is None:
            return
        print node.value
        pre_order(node.left)
        pre_order(node.right)

    ######## Post-order traversal
    def post_order(node):
        if node is None:
            return
        post_order(node.left)
        post_order(node.right)
        print node.value

    ############### Stack: bottom & top. Operations: push, pop, peek --> FILO (first in last out) queue
    # push: insert an element into stack = put on top.
    # pop: remove the top element in stack
    # peek: see the top element in stack without removing it
    # Access time: O(1) because only access top element
    # Insert time: O(1) because only access top element

    # .567274936 --> pop .56727493
    # .567274936 --> peek = 6 Stack is still .567274936
    # .5672 --> push(2) .56722

    ############### Queue: head & tail. Operations: enqueue, dequeue, peek --> FIFO (first in first out)
    # enqueue: put item after tail
    # dequeue: remove item at head
    # peek: see the item at head without removing it
    # Access time: O(1) because only access head element
    # Insert time: O(1) because only access tail element

