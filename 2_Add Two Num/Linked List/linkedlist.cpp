#include <iostream>

struct Node{

    int data;
    Node* next;

    Node(int data){
        this->data = data;
        this->next = nullptr;
   }
};

struct Linkedlist{
    Node* head;

    Linkedlist(){
        head = nullptr;
    }

    void push(int data){
        Node* newNode = new Node(data);
        if (head == nullptr){
            head = newNode;
        } else {
            Node *current = head;
            while(head->next != nullptr){
                current = current->next;
            }
            current->next = newNode;
        }
    }

    void print_list(){
        Node *current = head;
        while(current != nullptr){
            std::cout << current->data << " ->";
            current = current->next;
        }

    }
};

int main(){
    Linkedlist l1;
    l1.push(2);
    l1.push(22);
    l1.print_list();
    return 0;
}