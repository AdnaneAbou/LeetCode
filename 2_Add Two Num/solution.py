class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
    def print_list(self):
        while self is not None:
            print(self.val , end=" -> ")
            self = self.next
        print("\n")

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    counter_1 = 1
    counter_2 = 1 

    op1 =0
    op2 =0
    while (l1 != None ):
        op1 = op1 + l1.val * counter_1
        l1 = l1.next
        counter_1 = counter_1 * 10



    while (l2 != None):
        op2 += l2.val * counter_2
        l2 = l2.next
        counter_2 = counter_2 * 10

    result = op1 + op2
    print("result ",result)
    i=1
    if ( result == 0 ):

        return ListNode(0)
        
    l3 = ListNode()
    current  = l3
    while(((result // i)) > 0):
        new_node = ListNode((result // i)%10)
        current.next = new_node
        current = new_node
        i = i * 10

    current = l3.next 

    return current



l1 = ListNode()
l1.append(0)
# l1.append(4)
# l1.append(3)


l2 = ListNode()
l2.append(0)
# l2.append(6)
# l2.append(4)

l3 = addTwoNumbers(l1, l2)

l3.print_list()
