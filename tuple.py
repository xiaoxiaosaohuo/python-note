# tuple is immutable

tup = (1,2,3,4,5)
print(tup.count(3))  # 返回指定元素在元组中出现的次数
print(tup.index(4)) # 指定元素第一次出现的索引

# 将元组转换为列表
lst = list(tup)

# 修改列表
lst[2] = 10

# 将列表转换回元组
tup = tuple(lst)

print(tup)  # 输出 (1, 2, 10, 4, 5)
