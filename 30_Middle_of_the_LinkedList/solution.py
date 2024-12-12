# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    slow = head
    fast = head
    i = 1 
    while fast:
        fast = fast.next
        if i % 2 == 0:
            slow = slow.next
        i += 1 

    return slow