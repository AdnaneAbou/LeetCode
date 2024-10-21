# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        new_node = ListNode(val)
        current = self
        while current.next is not None :
            current = current.next
        current.next = new_node

    def print_list(self):
        while self:
            print(self.val ,end=' ->')
            self = self.next
        print("\n")
        
def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    current1 = list1
    current2 = list2
    head = ListNode()
    current = head
    
    while current1 is not None and current2 is not None:
        if current1.val <= current2.val:
            current.next = current1
            current1 = current1.next

        else:
            current.next = current2
            current2 = current2.next

        current = current.next
    
    if current1 is not None:
        current.next = current1
    elif current2 is not None:
        current.next = current2
 

    return head.next



list1 = ListNode(1)
list1.append(2)
list1.append(4)
list1.print_list()

list2 = ListNode(4)
list2.append(8)
list2.append(7)

list2.print_list()
list3 = mergeTwoLists(list1, list2)
list3.print_list()