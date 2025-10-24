def productExceptSelf(nums):
    l = len(nums)
    res =[1] * l
    for i in range(l):
        prod = 1
        for j in range(l):
            if i == j:
                continue
            prod *= nums[j]
        res[i] = prod
    return res





nums = [1,2,3,4]
print(productExceptSelf(nums))