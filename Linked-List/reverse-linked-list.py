
#llist = LinkedList(["a", "b", "c", "d", "e"])

head=[1,2,3,4,5]
class Solution:
    def reverseList(self, head):
        prev_node=None
        curr_node=head
        while curr_node:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node
        head=prev_node
        return head


instance_of_solution=Solution()
instance_of_solution.reverseList(head)
