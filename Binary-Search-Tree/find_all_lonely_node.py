"""
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.

"""

""" 1 
   /  \
  4    5
 / \   
3   6
"""

from typing import List

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self, root):
        self.root = TreeNode(root)

    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        count=[]
        self.dfs(root,count)
        return count

    def dfs(self,root,count):
        if root is None:
            return
        if root.left is None and root.right:
            count.append(root.right.val)
        elif root.left and root.right is None:
            count.append(root.left.val)
        self.dfs(root.left,count)
        self.dfs(root.right,count)

tree=Solution(1)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(3)
tree.root.left.right=TreeNode(4)
print(tree.getLonelyNodes(tree.root))
