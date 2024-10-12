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
   
    int op1 = 0;
    int op2 = 0;
    int i = 1 ;
    while(l1 != nullptr){
        op1 = op1 + l1->val * i;
        l1 = l1->next;
        i = i*10;
    }
    int mul = 1;
    while(l2!= nullptr){
        op2 = op2 + l2->val * mul;
        l2 = l2->next;
        mul = mul*10;
    }
    
    if( op1 + op2 == 0)
        return new ListNode(0);

    ListNode* return_node = nullptr;
    ListNode* current_node = nullptr;

    int sum = op1 + op2;
    while (sum > 0) {
        int digit = sum % 10; // Extract the last digit
        ListNode* new_node = new ListNode(digit); // Create new node for the digit

        if (return_node == nullptr) {
            return_node = new_node; // Save the head node
            current_node = return_node;
        } else {
            current_node->next = new_node; // Link the new node
            current_node = current_node->next;
        }

        sum /= 10; // Remove the last digit from the sum
    }

    return return_node;
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