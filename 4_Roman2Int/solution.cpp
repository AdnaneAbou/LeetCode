#include <iostream>
#include <map>
#include <string>

int romanToInt(std::string s ){
    std::map<std::string, int> myMap;

    myMap["I"] = 1;
    myMap["V"] = 5;
    myMap["X"] = 10;
    myMap["L"] = 50;
    myMap["C"] = 100;
    myMap["D"] = 500;
    myMap["M"] = 1000;

    int res = 0;
    int i = 0;

    while( i < s.length()){

        if (i < s.length()-1 && (s[i] == 'I' &&( s[i+1] == 'V' || s[i+1] == 'X'))){
            res +=  myMap[std::string(1,s[i+1])] -  myMap[std::string(1,s[i])];
            i += 2;
            continue;
        }

        if (i < s.length()-1 && (s[i] == 'X' && (s[i+1] == 'L' || s[i+1] == 'C'))){
            res +=  myMap[std::string(1,s[i+1])] -  myMap[std::string(1,s[i])];
            i += 2;
            continue;
        }

        if (i < s.length()-1 && (s[i] == 'C' && (s[i+1] == 'D' || s[i+1] == 'M'))){
            res +=  myMap[std::string(1,s[i+1])] -  myMap[std::string(1,s[i])];
            i += 2;
            continue;
        }

        res += myMap[std::string(1,s[i])];
        i += 1;

        
    }

    return res;
}


int main() {
    
    int res = romanToInt("MCMXCIV");
    std::cout << res << std::endl;

    return 0;
}