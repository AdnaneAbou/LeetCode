#include <iostream>
int RBinarySearch(int arr[] ,int l ,int h , int target) {

    if (l > h) {
    return -1;
    }

    int mid = ( l + h ) / 2;
    if ( target == arr[mid] ) { 
        return mid;
    }
    if (target < arr[mid]) {
        h = mid - 1;
        return RBinarySearch(arr,0,h,target);
    } else {
        l = mid + 1;
        return RBinarySearch(arr,l,h,target);
    }
}


int main() {
    int arr[] = { 0, 1, 3, 4, 5,55,60,75};
    int result = RBinarySearch(arr,0,sizeof(arr)/sizeof(arr[0])-1 ,55);

    std::cout << result << "\n";
    return 0;
}