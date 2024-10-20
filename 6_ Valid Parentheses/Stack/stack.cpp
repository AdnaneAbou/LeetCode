#include <vector>
#include <iostream>

class Stack {
private:   
    std::vector<int> stack;
public:
    void push(int data){
        stack.push_back(data);
    }

    int pop() {
        if(!is_empty()) {
            int top = stack.back();
            stack.pop_back();
            return top;
        } else {
            std::cerr << "Stack is empty!" << std::endl;
            return -1;
        }
    }
    int peek() {
        if(!is_empty()) {
            return stack.back();
        } else {
            std::cerr << "Stack is empty!" << std::endl;
            return -1;
        }
    }

    bool is_empty()const {
        return stack.empty();
    }

};



int main(){
    Stack stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);

    std::cout << stack.peek()<< std::endl; 
    std::cout << stack.pop()<< std::endl; 
    std::cout << stack.peek()<< std::endl; 
    std::cout << stack.pop()<< std::endl; 
    std::cout << stack.peek()<< std::endl; 

    return 0;
}
