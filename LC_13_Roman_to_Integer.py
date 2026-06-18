def romanToInt(x):
    new_dict ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    l = len(x)
    res = 0
    for i in range(1,l):
        if new_dict[x[i]] > new_dict[x[i-1]]:
            res = res -new_dict[x[i-1]]
        else:
            res = res + new_dict[x[i-1]]
    res = res + new_dict[x[l-1]]

    return res

# ex:
s = "LVIII"
print(romanToInt(s))