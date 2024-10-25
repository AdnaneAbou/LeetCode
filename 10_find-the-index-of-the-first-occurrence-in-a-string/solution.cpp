#include <string>
#include <iostream>
using namespace std;

int strStr(string haystack, string needle) {
    for(int i = 0; i < haystack.length();i++) {
        if (haystack.substr(i,needle.length()) == needle) {
            return i;
        }
    }
    return -1;
}

int main() {
    string haystack = "example";
    string needle = "xa";
    int result = strStr(haystack, needle);
    std::cout << result << std::endl;
    return 0;
}