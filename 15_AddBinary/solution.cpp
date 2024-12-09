#include <string>
#include <iostream>
#include <vector>
using namespace std;


vector<int> addBinary(string a, string b) {
    int i = a.length() - 1;
    int j = b.length() -1;
    int remainder = 0 ;
    vector<int> result;

    while (i >= 0 || j>= 0 || remainder > 0 ){
        int total = remainder;
        if(i>=0){
            total = total +( a[i] - '0');
            i--;
        }
        if(j>=0){
            total = total +( b[j] - '0');
            j--;
        }
        remainder = total / 2 ;
        result.emplace_back(total % 2);
    }
    return result;
}


main(){
    string example1 = "0";
    string example2 = "0";
    cout << " ff"<<example2[0] -'0' << endl;
    vector<int> res = addBinary( example1, example2);
    for( auto val : res){
        cout << val<< endl;
    }
    return 0;
}