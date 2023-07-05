# 在Python3中，列表（list）是一种有序的集合，可以包含任意类型的数据，包括数字、字符串、列表、字典等。列表可以通过索引访问其中的元素，也可以使用切片操作获取其中的子列表。列表是可变的，可以通过append()、insert()、remove()等方法来修改列表中的元素。

list1 = [1,2,'3',4]
list1[0] = 0

list1.append(5)

list1.remove("3")
print(list1)


list2 = [4,7,8,9]
print(list1 + list2)
print(list1 * 3)

# sort
list1.sort(reverse=True)
print(list1)


list3 = sorted(list1)
print(list3)


list1 = [1, 3, 5, 7, 100]

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]

list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)  # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1)  # []

fruits = ['grape', 'apple', 'strawberry', 'waxberry']

# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
