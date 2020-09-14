"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],
   3
   / \
  9  20
    /  \
   15   7

"""

class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


class BinaryTree(object):
    def __init__(self,root):
        self.root=TreeNode(root)

    def depthSearch(self,root: TreeNode) -> int:
        depth=0

        level= [root]
        print(len(level))
        while level:
            depth +=1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level=queue
        return depth

ins=BinaryTree(3)
ins.root.left=TreeNode(9)
ins.root.right=TreeNode(20)
ins.root.right.left=TreeNode(15)
ins.root.right.right=TreeNode(7)
print(ins.depthSearch(ins.root))
