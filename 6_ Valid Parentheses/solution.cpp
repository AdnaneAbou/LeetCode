#include <iostream>
#include <vector>

class Stack{
private:
    std::vector<char> stack; 
public:

    void push(char & str){
        stack.push_back(str);
    }

    char pop(){
        if(!stack.empty()) {
            char str = stack.back();
            stack.pop_back();
            return str;
        } else {
            std::cerr << "Stack empty!" << std::endl;
        }
    }
    char peek(){
        if(!stack.empty()) {
            return stack.back();
        } else {
        std::cerr << "Stack empty!" << std::endl;
        }

    }

    bool isEmpty(){
        return stack.empty();
    }
};

bool isValid(std::string s){
    Stack stack;
    stack.push(s[0]);
    for(int i =1 ; i < s.size() ; i++){
        if (stack.peek() == '(' &&  s[i] == ')'){
            stack.pop();
        } else if (stack.peek() == '{' &&  s[i] == '}'){
            stack.pop();
        } else if (stack.peek() == '[' &&  s[i] == ']'){
            stack.pop();
        } else {
            stack.push(s[i]);
        } 
    }

    if (stack.isEmpty()) {
        return true;
    } else {
        return false;
    }
}

int main(){
    std::string exp = "()[]}{";
    bool result = isValid(exp);
    std::cout << result << std::endl;
    return 0;
}