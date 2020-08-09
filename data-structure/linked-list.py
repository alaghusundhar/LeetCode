"""
Linked List Algorithm to

1.) Add a New LinkedList
2.) Remove a Existing from LinkedList
3.) Find a Data from the Linkedlist
4.) Get the Size of the LinkedList
"""


class Node:
    def __init__(self,d,n=None):
        self.data=d
        self.next_node=n

    def get_next(self):
        return self.next_node
    def set_next(self,n):
        self.next_node=n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data=d

class LinkedList:

    def __init__(self,r=None):
        self.root=r
        self.size=0

    def get_size(self):
        return self.size

    def add(self,d):
        """Add a new Node"""
        new_node=Node(d,self.root)
        self.root=new_node
        self.size+=1

    def remove(self,d):
        """ Remove a data from the Linked List """
        this_node=self.root
        previous_node=None
        while this_node is not None:
            if this_node.get_data() ==d:
                if previous_node is not None:
                    previous_node.set_next(this_node.get_next())
                else:
                   self.root=this_node.get_next()
                self.size-=1
                return True
            else:
                previous_node=this_node
                this_node=this_node.get_next()
        return False

    def find(self,d):
        this_node=self.root
        while this_node is not None:
            if this_node.get_data() ==d:
                return d
            elif this_node.get_next()==None:
                return False
            else:
                this_node=this_node.get_next()


def main():
    myList= LinkedList()
    myList.add(4)
    myList.add(5)
    myList.add(9)
    myList.add(1)
    print("Size of the Linked List is %s",str(myList.get_size()))
    myList.remove(9)
    print("Size of the Linked List is %s", str(myList.get_size()))
    myList.remove(25)
    print("Size of the Linked List is %s", str(myList.get_size()))
    print("FInd Number 4 %s",myList.find(4))


main()