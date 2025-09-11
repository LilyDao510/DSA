#20. Valid Parentheses
# Solution - Stack:
# def isValid(s:str):
#     stack =[]
#     dictS ={'(':')', '{':'}','[':']'}
#     for i in s:
#         if i in dictS:
#             stack.append(i)
#         elif len(stack) == 0 or i != dictS[stack.pop()]:
#             return False
#     return len(stack)==0

# solution _bruce force 

def isValid(s:str):
    while "()" in s or "{}" in s or "[]" in s:
            s= s.replace("()","")
            s= s.replace("{}","")
            s= s.replace("[]","")
    return s==""

s = "([])[]"
print(isValid(s))




           
            
            


