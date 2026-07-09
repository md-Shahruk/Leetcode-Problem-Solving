
'''
- if array sorted then think for binary search
- if not sort,then do it sort
- Time: O(logn) but worst case O(n) becasue high = high - 1
- So, insted of using high = high - 1 we can do high = mid - 1
'''
def binarySearch(nums, target):
    low, high = 0, len(nums) - 1 
    while low <= high:
        mid = (low + high) // 2 
        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            #high = high - 1
            high = mid - 1
        else:
            #low = low + 1
            low = mid + 1
    return -1 


nums = [-1,0,3,5,9,12]
target = 9

print(binarySearch(nums, target))