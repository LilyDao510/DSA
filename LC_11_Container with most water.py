#LC 11. Container With Most Water
def maxArea(heights):
    i = len(heights)
    l,r = 0, i-1
    res = 0
    while l < r:
        area = (r-l) * min(heights[r],heights[l])
        res = max(res,area)

        if heights[r] < heights[l]:
            r -= 1
        elif heights[r] >= heights[l]:
            l += 1
    return res

heights = [1,7,2,5,4,7,3,6]
print(maxArea(heights))


