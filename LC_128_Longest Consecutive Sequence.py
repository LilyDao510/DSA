# 128. Longest Consecutive Sequence
def longestConsecutive(nums):
    new_nums = set(nums)
    longest = 0
    for i in new_nums:
        if (i-1) not in new_nums:
            length = 1
            while (i+length) in new_nums:
                length +=1
            longest = max(longest,length)
    return longest



# ex: 
nums = [2,20,4,10,3,4,5,6,7]
print(longestConsecutive(nums))
