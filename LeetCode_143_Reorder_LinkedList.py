class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def reverse_linked_list(l1: ListNode):
    if not l1:
        return l1
    if l1.next is None:
        return l1

    # At least two nodes
    l1_old_head = l1
    p1 = l1
    p2 = l1.next
    p2_old_nxt = p2

    while p2.next:
        p2_old_nxt = p2.next
        p1_old_nxt = p2
        p2.next = p1
        p1 = p1_old_nxt
        p2 = p2_old_nxt
    else:
        p2.next = p1

    l1_old_head.next = None
    new_head = p2_old_nxt
    return new_head


def reorder_list(l1: ListNode):

    if not l1 or l1.next is None:
        return None

    slowptr = l1
    fastptr = l1.next

    while slowptr.next and fastptr.next:
        fastptr = fastptr.next
        slowptr = slowptr.next

        if fastptr.next is not None:
            fastptr = fastptr.next
        else:
            break

    print(f"The slow ptr is {slowptr.val}")
    print(f"The fast ptr is {fastptr.val}")

    halfptr = slowptr.next
    slowptr.next = None
    second_half_reversed = reverse_linked_list(halfptr)

    p1 = l1
    p2 = second_half_reversed

    # printLinkedList(p1)
    # printLinkedList(p2)


    while p1 and p2:
        p1_old_nxt = p1.next
        p2_old_nxt = p2.next
        p1.next = p2
        p1.next.next = p1_old_nxt

        p1 = p1_old_nxt
        p2 = p2_old_nxt
    if p1 and not p2:
        p1.next = p2
    if p2 and not p1:
        p2.next = p1

    return l1


# Example usage:
list1 = createLinkedList([1, 2,3,4, 5])
list2 = createLinkedList([5, 6, 7])
flag = reorder_list(list1)

printLinkedList(flag)
