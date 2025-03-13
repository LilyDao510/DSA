# 217. Contains Duplicate
def hasDuplicate(nums):
    set =[]
    for i in nums:
        if i in set:
            return True
        set.append(i)
    return False

# nums = [1,2,3,4,4]
nums = [1,2,3,4]
print(hasDuplicate(nums))


# 242. Valid Anagram

def isAnagram(self, s: str, t: str) -> bool:
    n = len(s)
    
    m = len(t)

    if n != m:
        return False
    
    counts ={}
    countt ={}

    for i in range(n):
        counts[s[i]] = 1 + counts.get(s[i],0)
        countt[t[i]] = 1 + countt.get(t[i],0)
    return counts == countt

s = "anagram", t = "nagaram"

# 1. Two Sum
def twoSum(nums,target):
    l = len(nums)
    dict = {}
    for i in range(l):
        diff = target - nums[i]
        if diff in dict:
            return [dict[diff],i]
        else:
            dict[nums[i]] = i

nums =[1,2,3,4,5] 
target = 8
print(twoSum(nums,target))  

# 20. Valid Parentheses

# S1:

def isValid(s):
    if "()" or "{}" or "[]" in s:
        s = s.replace("()","")
        s = s.replace("[]","")
        s = s.replace("{}","")

    return s ==""

s ="())[]{}"

print(isValid(s))

# S2:
def isValid(s):
    stack =[]
    dict = {'(':')', '{':'}','[':']'}

    for i in s:
        if i in dict:
            stack.append(i)
        elif len(stack) == 0 or i != dict[stack.pop()]:
            return False
    return len(stack) == 0

s ="()[{}"
print(isValid(s))
