# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    """
    :type head: Optional[ListNode]
    :type left: int
    :type right: int
    :rtype: Optional[ListNode]
    """
    if not head or left==right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left-1):
        prev = prev.next
    
    current = prev.next
    reversed_head = None

    for _ in range(right - left +1):
        nxt = current.next
        current.next = reversed_head
        reversed_head = current
        current = nxt

    prev.next.next = current
    prev.next = reversed_head

    return dummy.next

head = ListNode(1)  
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

re = ListNode(5)
head_res = reverseBetween( head , left = 2, right = 4)

print((head_res.next.next.val))

