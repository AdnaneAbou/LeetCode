#include <string>
#include <vector>
#include <iostream>

using namespace std;

int lengthOfLastWord(string s) {
    int counter = 0 ;
    int i = s.size() -1;

    while ( i>=0 && s[i] == ' '){
        i--;
    }
    while ( i>=0 && s[i] != ' '){
        counter++;
        i--;
    }

    return counter ;
};

int main() {
    string str = " adn nrnrn ang   ";
    int result = lengthOfLastWord(str); 
    cout << result << endl;
    return 0;
}