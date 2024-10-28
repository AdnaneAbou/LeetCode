#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using namespace std;

int lengthOfLongestSubstring(const string& s) {
    int start = 0 ;
    int max_length = 0 ; 
    unordered_map<char, int> char_index_map;

    for(int end = 0 ; end < s.length(); end++) {
        if( char_index_map.end() != char_index_map.find(s[end])) {
            start = max(start,char_index_map[s[end]] + 1);
        }
        char_index_map[s[end]] = end;
        max_length = max(max_length , end - start +1);
    }
    return max_length;
}

int main(){
    string s = "abcabcbb";
    int result = lengthOfLongestSubstring(s);
    cout << result << endl;
    return 0;
}