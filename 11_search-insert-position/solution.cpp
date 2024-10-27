#include <vector>
#include <iostream>
using namespace std;

int searchInsert(vector<int>& nums, int target) {
    int l = 0 ;
    int h = nums.size() -1 ;
    int mid;
    while ( l <= h) {
        mid = (h+l) / 2 ;
        if ( nums[mid] == target) {
            return mid ;
        } else if (nums[mid] > target) {
            h = mid - 1 ;
        } else {
            l = mid + 1 ;
        }
    }

    return l ;
}

int main() {
    vector<int> vec= {1,3,5,6};
    int result = searchInsert(vec,2);
    cout << result << endl;
    return 0;
}