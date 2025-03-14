def search(nums, target):
    left,right = 0, (len(nums)-1)
    
    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# test
nums = [-2,0,2,7,10]
target = 10

print(search(nums,target))