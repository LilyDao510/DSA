# 704. Binary Search

def binary_search(l, target):
    n = len(l)
    left, right = 0, n-1
    
    while left <= right:
        mid =(left +right)//2
        if l[mid] == target:
            return mid
        if l[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

l =[1,2,3,4,5]
target = 2

print(binary_search(l,target))



    


        