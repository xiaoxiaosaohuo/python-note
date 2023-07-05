import array

arr1 = array.array('i',[1,2,3,4,5])
arr2 = array.array('i', [4, 5, 6])
print(arr1)
print(arr1 + arr2)  # 输出 array('i', [1, 2, 3, 4, 5, 6])

# visit

arr1 = array.array('i', [1, 2, 3, 4, 5])

# 访问第一个元素
print(arr1[0])  # 输出 1

# 访问最后一个元素
print(arr1[-1])  # 输出 5

# 获取子数组
print(arr1[1:3])  # 输出 array('i', [2, 3])


# modify

arr1 = array.array('i', [1, 2, 3, 4, 5])

# 修改第一个元素
arr1[0] = 0

# 在末尾添加一个元素
arr1.append(6)

# 在指定位置插入一个元素
arr1.insert(1, 1.5)

# 删除指定元素
arr1.remove(3)

print(arr1)  # 输出 array('i', [0, 1, 2, 4, 5, 6])
