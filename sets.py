set1 = set([1,1,2,3])
set2 = set([1,2,3,4,5])
set3 = {1,2,3,4,5,6}
# add element
set1.add(6)
set1.update([7,8,9]) # add mutiple elements 

print(set1)

# delete element
set1.remove(6)

print(set1)

set1.discard(7)

set1.pop()
set1.pop()
print(set1)

# intersection

set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1 & set2)

print(set1 | set2)

print(set1 - set2)

print(set1 ^ set2) # 对称差集


if 3 in set1:
    print("3 is in set1")