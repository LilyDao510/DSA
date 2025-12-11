# 739. Daily Temperatures
def dailyTemp(temperatures):
    l = len(temperatures)
    result =[0]*l
    stack= []
    for i in range(l):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day

        stack.append(i)
    return result


temperatures = [73,74,75,71,69,72,76,73]

print(dailyTemp(temperatures))