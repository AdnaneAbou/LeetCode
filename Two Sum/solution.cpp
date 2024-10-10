#include <vector>
#include <iostream>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    for(int i = 0; i < nums.size();i++){
        for(int j = nums.size() -1; j >= 0;j--){
            if(nums[i] + nums[j] == target && i != j){
                return std::vector<int>(i, j);
            }
        }
    }
    
}


int main(){
    std::vector<int> nums = {3,2,4};
    int target = 6;
    twoSum(nums,target);
    return 0;
};