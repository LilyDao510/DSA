# 14. Longest Common Prefix
# example:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longesCommonPrefix(strs):
    res =''
    l = len(strs[0])
    for i in range(l):
        for s in strs:
            if i == len(s) or strs[0][i] != s[i]:
                return res
        res += strs[0][i]
    return res

strs = ["flower","flow","floight"]
print(longesCommonPrefix(strs))