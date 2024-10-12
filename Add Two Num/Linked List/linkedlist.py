class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data , end=" -> ")
            current = current.next
        print("None")


def addTwoNumbers( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    counter_1 = 1
    counter_2 = 1 
    current_node_l1 = l1.head
    current_node_l2 = l2.head
    op1 =0
    op2 =0

    while (current_node_l1 != None ):
        op1 = op1 + current_node_l1.data * counter_1
        current_node_l1 = current_node_l1.next
        counter_1 = counter_1 * 10



    while (current_node_l2 != None):
        op2 += current_node_l2.data * counter_2
        current_node_l2 = current_node_l2.next
        counter_2 = counter_2 * 10

    result = op1 + op2
    i=1
    list_return = []
    l3 = LinkedList()
    if ( result == 0 ):
        l3.append(0)
    while(((result // i)) > 0):
        list_return.append((result // i)%10)
        l3.append((result // i)%10)
        i = i * 10

    return l3

l1 = LinkedList()
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)


l1.print_list()
l2 = LinkedList()
l2.append(9)
l2.append(9)
l2.append(9)
l2.append(9)


l2.print_list()

l3 = addTwoNumbers( l1, l2)
l3.print_list()

# print((80 // 1)%10)