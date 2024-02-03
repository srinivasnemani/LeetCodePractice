# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if curr is None:
            return head
        if curr.next is not None:
            next = curr.next

        while curr:
            curr_val = curr.val
            next = curr.next
            if next is not None:
                next_val = next.val

            curr.next = prev
            prev = curr
            curr = next

        return prev


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link the nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Print the original linked list
current_node = node1
while current_node is not None:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")

# Reverse the linked list using the reverseList method
solution = Solution()
reversed_head = solution.reverseList(node1)

# Print the reversed linked list
current_node = reversed_head
while current_node is not None:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")
