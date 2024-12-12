# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    current = head
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current 
        current = nxt
    return  prev


def reverList_recursive(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if not head:
        return None
    
    newHead = head

    if head.next:
        newhead = reverList_recursive(head.next)
        head.next.next = head
    head.next = None
    return newHead

