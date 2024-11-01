In this lab, i've implemented a Binary Search Tree with insertion, deletion, search, and traversal operations. I've practiced working with recursive algorithms and tree data structures. The modular approach i've taken allows for easy testing and expansion of the BST implementation.
These methods provide comprehensive functionality for managing and analyzing a Binary Search Tree, from verifying its structure to measuring its properties and traversing its nodes.

## EXERCISE EXPLANATION:

# 1.Implement a method to find the maximum value in the BST.

TreeNode Class: Defines a node in a binary search tree (BST) with value, left, and right attributes.

BST Class: Manages the binary search tree.

insert Method: Adds a new value to the tree by finding the correct position.

find_max Method: Finds the maximum value in the tree by traversing to the rightmost node.

Example Usage: Inserts values into the BST and finds the maximum value.

# 2. Add a method to count the total number of nodes in the BST.

count_nodes Method: Counts the total number of nodes in the tree.

_count_nodes_rec Helper Method: Recursively counts nodes by traversing the tree.

# 3. Implement a level-order traversal (breadth-first search) for the BST.

TreeNode Class:

Attributes: Each node has a value, and pointers to left and right children.

Constructor: Initializes the node with the given value and children.

BST Class:
Root: Starts with an empty tree (self.root = None).

Insert Method:

Check Root: If the root is empty, set the root to a new TreeNode.

Recursive Insert: Uses _insert_rec to place the value in the correct position.

Level-Order Traversal:
Initialize Queue: Uses a deque to keep track of nodes to visit.

Traversal Loop:

Current Node: Dequeue the first node from the queue.

Add to Result: Append the node’s value to the result list.

Enqueue Children: If the current node has left and right children, enqueue them.

Return Result: The final list of values in level-order.

# 4.Create a method to find the height of the BST.
TreeNode Class:
Attributes: value, left, and right children.

Constructor: Initializes the node with given values and children.

BST Class:
Root: Starts with an empty tree (self.root = None).

Insert Method:

Check Root: If the root is empty, set the root to a new TreeNode.

Recursive Insert: Uses _insert_rec to place the value in the correct position.

Height Method:
Public Method: Calls the private _height_rec method starting from the root.

Private Recursive Method: Calculates the height of the tree.

Base Case: If the node is None, returns -1.

Recursive Case:  Recursively calculates the height of left and right subtrees, and returns 1 + max(left_height, right_height) to account for the current node.

# 5.Implement a method to check if the tree is a valid BST.
TreeNode Class:
Attributes: Each node has a value, and pointers to left and right children.

Constructor: Initializes the node with the given value and children.

BST Class:
Root: Starts with an empty tree (self.root = None).

Insert Method:

Check Root: If the root is empty, set the root to a new TreeNode.

Recursive Insert: Uses _insert_rec to place the value in the correct position.

Validation Method (is_valid_bst):
Public Method: Calls the private _is_valid_bst_rec method starting from the root, with initial low and high bounds as negative and positive infinity.

Private Recursive Method (_is_valid_bst_rec):
Base Case: If the node is None, returns True.

Validation: Ensures the node value is within the bounds (low and high).

Recursive Case: Recursively validates the left subtree with updated high bound and the right subtree with updated low bound.