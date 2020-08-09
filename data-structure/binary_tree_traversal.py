"""
Binary Tree Algorithm

1.) Pre Order Traversal
2.) In Order Traversal
3.) Post Order Traversal

"""

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):

    def __init__(self,root):
        self.root=Node(root)

    def preorder_traversal(self,start,traversal):
        """Pre Order Traversal """
        if start:
            traversal+=(str(start.value) + "-")
            traversal=self.preorder_traversal(start.left,traversal)
            traversal=self.preorder_traversal(start.right,traversal)
        return traversal

    def inorder_traversal(self,start,traversal):
        """In Order Traversal Left ->root->right """
        if start:
            traversal=self.inorder_traversal(start.left,traversal)
            traversal+=(str(start.value) + "-")
            traversal=self.inorder_traversal(start.right,traversal)
        return traversal

    def postorder_traversal(self,start,traversal):
        """Post Order Traversal left->right->root """
        if start:
            traversal=self.postorder_traversal(start.left,traversal)
            traversal=self.postorder_traversal(start.right,traversal)
            traversal+=(str(start.value) + "-")
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preorder_traversal(tree.root,"")
        elif traversal_type=="inorder":
            return self.inorder_traversal(tree.root,"")
        elif traversal_type=="postorder":
            return self.postorder_traversal(tree.root,"")
        else:
            print("Traversal type %s is not supported",traversal_type)


tree=BinaryTree(1)
tree.root.left=Node(4)
tree.root.right=Node(5)
tree.root.left.left=Node(3)
tree.root.left.right=Node(6)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
#main()



