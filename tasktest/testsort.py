import random


a = []
for i in range(8):
    rand = random.randint(-10, 10)
    a.append(rand)

print(a)

print('-----')


def sorter(a):

    if len(a) <= 1:
        return a
    
    mid = a[0]
    left = []
    right = []
    for i in a[1:]:
        if i < mid:
            left.append(i)
        else:
            right.append(i)
        
    result = sorter(left) + [mid] + sorter(right)
    return result







def sorter_in_place(a):

    if len(a) <= 1:
        return a

    k = 0
    n = 1

    for elem in a:
       
        while elem > a[n]:
            a[k], a[n] = a[n], a[k]
            t = n
            k = n
            n = t + 1
        k += 1
        n += 1






    # mid = a[0]
    # left = []
    # right = []
    # for i in a[1:]:
    #     if i < mid:
    #         left.append(i)
    #     else:
    #         right.append(i)
        
    result = a
    return result















result = sorter_in_place(a)
print(a)
print('-----')
a.sort()
print(a)
print('-----')
print(result)

if a == result:
    print("yes")
else:
    print('no')