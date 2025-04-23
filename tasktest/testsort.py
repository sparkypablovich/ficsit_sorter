import random


a = []
for i in range(8000):
    rand = random.randint(-100000, 100000)
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



result = sorter(a)
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