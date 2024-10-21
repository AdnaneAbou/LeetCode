#include <iostream>

struct ListNode{
    int val;
    ListNode* next;

    ListNode(): val(0), next(nullptr) {}
    ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x , ListNode* next): val(x), next(next) {}

    void append(int val) {
        ListNode* new_node= new ListNode(val);
        ListNode* current = this;
        while(current->next != nullptr) {
            current = current->next;
        }
        current->next = new_node;
    }
    void print_list() {
        ListNode* current= this;
        while(current != nullptr) {
            std::cout << current->val << " ->" ;
            current = current->next;
        }
        std::cout << std::endl;
    }
};

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode* head = new ListNode(0);
    ListNode* current = head;

    while (list1 != nullptr && list2 != nullptr) {
        if(list1->val <= list2->val) {
            current->next = list1;
            list1= list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }

    if (list1 != nullptr ) {
        current->next = list1;
    } else if (list2 != nullptr) {
        current->next = list2;
    }

    return head->next;
}

int main() {
    ListNode* list1 = new ListNode(1 , new ListNode(3 , new ListNode(5 )));
    list1->print_list();

    ListNode* list2 = new ListNode(1 , new ListNode(5 , new ListNode(7 )));
    list2->print_list();

    ListNode* result = mergeTwoLists(list1, list2); 

    result->print_list();

    return 0;
}