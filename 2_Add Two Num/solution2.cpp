/**
 * Definition for singly-linked list.*/
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy_head = new ListNode(0);
    ListNode* current = dummy_head;
    int carry = 0;

    while (l1 != nullptr || l2 != nullptr || carry > 0) {
        int sum = carry;
        
        if (l1 != nullptr) {
            sum += l1->val;
            l1 = l1->next;
        }
        
        if (l2 != nullptr) {
            sum += l2->val;
            l2 = l2->next;
        }

        carry = sum / 10;
        current->next = new ListNode(sum % 10);
        current = current->next;
    }

    return dummy_head->next;
}



int main(){
    ListNode* l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    ListNode* l2 = new ListNode(5, new ListNode(6, new ListNode(4))); // represents 465

    ListNode* result = addTwoNumbers(l1, l2); // should represent 807

    // Print result
    while (result != nullptr) {
        std::cout << result->val << " "; // Output: 7 0 8
        result = result->next;
    }

    return 0;
}
