#include <vector>
#include <iostream>
int removeDuplicates(std::vector<int>& nums) {
    int counter = 0;
    for(int i = 1; i < nums.size();i++) {
        if (nums.at(i) != nums.at(counter)) {
            counter++;
            nums.at(counter) = nums.at(i);
        }
    }

    return counter+1;
}
int main(){
    std::vector<int> nums = {1,2,3,3,3,4,5,6,7};
    int count = removeDuplicates(nums); 
    // std::cout << nums.at(0) << std::endl; 
    return 0;
}