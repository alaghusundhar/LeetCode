"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

Given the tree:
        4
       / \
      2   7
     / \
    1   3
"""

class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class searchTree:

    def __init__(self, root):
        self.root = TreeNode(root)

    def searchBinaryTree(self, root: TreeNode, value: int) -> TreeNode:
        trav = root
        if not root or root.value == value:
            return root.right.value
        if root.value > value:
            return self.searchBinaryTree(root.left, value)
        return self.searchBinaryTree(root.right, value)

tree=searchTree(4)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(7)
tree.root.left.left=TreeNode(1)
tree.root.left.right=TreeNode(3)
print(tree.searchBinaryTree(tree.root, 2))



