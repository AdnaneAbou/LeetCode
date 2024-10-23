#include <vector>
#include <iostream>

int removeElement(std::vector<int>& nums, int val) {
    int counter = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != val) {
            nums[counter] = nums[i];
            counter++;
        }
    }
    return counter ;
}

int main() {
    std::vector<int> nums = {0,1,2, 2, 3,0, 4, 2};
    int val = 2;
    int counter = removeElement(nums, val);
    std::cout << val << std::endl;
    return 0;
}