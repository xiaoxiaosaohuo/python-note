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
