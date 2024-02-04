class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating two sorted linked lists
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))
list2 = None
list1 = None

def mergeTwoLists(list1, list2):
    head = None
    curr_node = None
    l1_curr = list1
    l2_curr = list2
    if list1 is None and list2 is None:
        return list1
    if list1 is not None and list2 is None:
        return list1
    if list2 is not None and list1 is None:
        return list2

    while l1_curr is not None and l2_curr is not None:
        if head is None:
            if l1_curr.val < l2_curr.val:
                head = list1
                l1_curr = list1.next
            else:
                head = list2
                l2_curr = list2.next
            curr_node = head
            continue

        if l1_curr.val < l2_curr.val:
            curr_node.next = l1_curr
            curr_node = l1_curr
            l1_curr = l1_curr.next
        else:
            curr_node.next = l2_curr
            curr_node = l2_curr
            l2_curr = l2_curr.next
    if l1_curr is None and l2_curr:
        curr_node.next = l2_curr

    if l2_curr is None and l1_curr:
        curr_node.next = l1_curr
    return head


# Merge the two sorted lists
merged_list = mergeTwoLists(list1, list2)
current_node = merged_list
while current_node is not None:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")
