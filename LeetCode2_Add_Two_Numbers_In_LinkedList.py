class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode):

    if l1.next is None:
        return l1
    l1_original_head = l1
    a2 = l1.next
    a1 = l1
    while a2.next:
        a2nxt_original = a2.next
        a2.next = a1
        a1, a2 = a2, a2nxt_original
    a2.next = a1
    l1_original_head.next = None
    l1_new_head = a2
    return l1_new_head




# Function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Function to print a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Example usage:
list1 = createLinkedList([1, 2])
list2 = createLinkedList([5, 6, 7])

flag = addTwoNumbers(list1, list2)
# flag = getIndexVal(list1, 7)

printLinkedList(flag)
