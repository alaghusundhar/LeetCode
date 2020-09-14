"""

Example of a Stack Algorithm

"""

class Stack:
    def __init__(self):
        self.items=[]
    """Function to Add Items to Stack """
    def push(self,item):
        self.items.append(item)
    """Function to Remove Last Item in Stack """
    def pop(self):
        return self.items.pop()
    """Function to Check if a Stack is Empty"""
    def isempty(self):
        return self.items==[]
    """Function to Check the last item of a Stack """
    def peek(self):
        if not self.isempty():
            return self.items[-1]
    """Function to """
    def get_stack(self):
        return self.items



stack=Stack()
stack.push("A")
stack.push("B")
print(stack.get_stack())
stack.pop()
