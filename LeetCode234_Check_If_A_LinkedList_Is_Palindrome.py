# https://leetcode.com/problems/palindrome-linked-list/
# Solution is working, but time limit exceeding, needs performance improvements.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_linked_list_size(head):
    ptr = head
    count = 0
    while ptr is not None:
        ptr = ptr.next
        count = count + 1
    return count


def getIndexVal(head, index):
    if head is None:
        return None

    ctr = 0
    ptr = head
    ptrval = None
    while ctr < index and ptr:
        ptrval = ptr.val
        ptr = ptr.next
        ctr += 1
    return ptrval

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sizell = get_linked_list_size(head)
        stptr = 1
        endptr = sizell
        check_flag = True
        while stptr < endptr:
            leftval = getIndexVal(head, stptr)
            rightval = getIndexVal(head, endptr)
            check_flag = check_flag and (leftval == rightval)
            stptr, endptr = stptr + 1, endptr - 1
            if not check_flag:
                return False
        else:
            return True        
