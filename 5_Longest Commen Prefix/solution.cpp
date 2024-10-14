#include <string>
#include <vector>
#include <iostream>

std::string longestCommonPrefix(std::vector<std::string>& strs) {
    std::string common("") ;
    std::string return_common ="";
    int i = 0;
    if(strs.size() ==1){
        return strs[0];
    }

    while (true){ 
        std::vector<char> list_first_char ;
        for(const auto& it: strs){
            if ( i >= it.size() ){
                return return_common;
            }
            list_first_char.push_back(it[i]);
        }

        for(int j=0; j<list_first_char.size()-1;j++){
            if (list_first_char[0] != list_first_char[j+1] ){
                return return_common;
            }
            common = list_first_char[0];
        }
        return_common += common;
        i+=1;

        
    };
}

int main(){
    std::vector<std::string> strs = {"aaaaaa","aaaaaabdv"};
    std::string result = longestCommonPrefix(strs);
    std::cout <<" result : " <<result << std::endl;
    return 0 ;
}