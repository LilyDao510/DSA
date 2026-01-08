# a = [1,2,3]
# b=['a','b','c']
# ab= list((zip(a,b)))
# ab.sort(reverse=True)
# print(ab)

def carFleet(target,position,speed):
    cars = list(zip(position,speed))
    cars.sort(reverse=True)

    stack=[]
    for pos,spe in cars:
        time = (target-pos)/spe

        if not stack or time>stack[-1]:
            stack.append(time)

    return len(stack)

target = 10
position = [1,4]
speed = [3,2]

print(carFleet(target,position,speed))