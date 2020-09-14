"""
   5
   / \
  3   6
 / \   \
2   4   7
"""

# Definition for a binary tree node.

key=3
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def __init__(self,root):
        self.root=TreeNode(root)

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if root is None:
            return root

        if root.value < key:
            







tree=Solution(5)
tree.root.left=TreeNode(3)
tree.root.right=TreeNode(6)
tree.root.left.left=TreeNode(2)
tree.root.left.right=TreeNode(4)
tree.root.right.right=TreeNode(7)
print(tree.deleteNode(tree.root,3))
