
##Exercises 
#1 Implement a method to find the maximum value in the BST.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

# Example Usage
bst = BST()
bst.insert(15)
bst.insert(12)
bst.insert(20)
bst.insert(6)
bst.insert(10)
print(bst.find_max())  

# 2.Add a method to count the total number of nodes in the BST.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def count_nodes(self):
        return self._count_nodes_rec(self.root)

    def _count_nodes_rec(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_rec(node.left) + self._count_nodes_rec(node.right)

# Example Usage
bst = BST()
bst.insert(15)
bst.insert(12)
bst.insert(20)
bst.insert(6)
bst.insert(10)
print(bst.count_nodes())  

#3. Implement a level-order traversal (breadth-first search) for the BST.
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def level_order_traversal(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

# Example Usage
bst = BST()
bst.insert(15)
bst.insert(12)
bst.insert(20)
bst.insert(6)
bst.insert(10)
print(bst.level_order_traversal())  


#4. Create a method to find the height of the BST.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def height(self):
        return self._height_rec(self.root)

    def _height_rec(self, node):
        if node is None:
            return -1  # Height of an empty tree is -1
        left_height = self._height_rec(node.left)
        right_height = self._height_rec(node.right)
        return 1 + max(left_height, right_height)

# Example Usage
bst = BST()
bst.insert(15)
bst.insert(12)
bst.insert(20)
bst.insert(6)
bst.insert(10)
print(bst.height())  # Output: 2


#5. Implement a method to check if the tree is a valid BST.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def is_valid_bst(self):
        return self._is_valid_bst_rec(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_rec(self, node, low, high):
        if not node:
            return True
        if not (low < node.value < high):
            return False
        return (self._is_valid_bst_rec(node.left, low, node.value) and 
                self._is_valid_bst_rec(node.right, node.value, high))

# Example Usage
bst = BST()
bst.insert(15)
bst.insert(12)
bst.insert(20)
bst.insert(6)
bst.insert(10)
print(bst.is_valid_bst())  
