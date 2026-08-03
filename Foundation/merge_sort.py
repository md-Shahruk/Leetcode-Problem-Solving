# merge sort
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left_merge = merge_sort(left)
    right_merge = merge_sort(right)
    
    return merge(left_merge, right_merge)


def merge(l, r):
    res = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i = i + 1
        else:
            res.append(r[j])
            j = j + 1
    while i < len(l):
        res.append(l[i])
        i = i + 1
    while j < len(l):
        res.append([j])
        j = j + 1
    return res 

nums = [5,2,3,1]
print(merge_sort(nums))