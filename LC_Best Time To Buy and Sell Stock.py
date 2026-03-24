# Brute force 
# def Best_time(price):
#     n = len(price)
#     output = 0
#     for i in range(n):#price[i] == buy
#         for j in range(i+1,n): # price[j] == sell
#             gap = price[j] - price[i]
#             output = max(output,gap)
#     return output

# price =[10,1,5,6,7,1]

# print(Best_time(price))
# time = o(n2)
# space= o(1)

# 2 pointer:

def Best_time(price):
    b, s = 0,1
    l = len(price)
    output = 0

    while s < l:
        if price[s] > price[b]:
            gap = price[s] - price[b]
            output = max(output,gap)

        else:
            b = s
        s += 1
    return output

price =[10,1,5,6,7,1]
print(Best_time(price))

