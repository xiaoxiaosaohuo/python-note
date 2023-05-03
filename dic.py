
# create
# 使用大括号创建字典
dict1 = {"name": "Alice", "age": 18, "gender": "female"}

# 使用dict()函数创建字典
dict2 = dict(name="Bob", age=20, gender="male")

print(dict1)  # 输出 {'name': 'Alice', 'age': 18, 'gender': 'female'}
print(dict2)  # 输出 {'name': 'Bob', 'age': 20, 'gender': 'male'}

# visit

dict1 = {"name": "Alice", "age": 18, "gender": "female"}

# 访问指定键的值
print(dict1["name"])  # 输出 Alice

# 获取所有键
print(dict1.keys())  # 输出 dict_keys(['name', 'age', 'gender'])

# 获取所有值
print(dict1.values())  # 输出 dict_values(['Alice', 18, 'female'])

# 获取所有键值对
# 输出 dict_items([('name', 'Alice'), ('age', 18), ('gender', 'female')])
print(dict1.items())

# modify

dict1 = {"name": "Alice", "age": 18, "gender": "female"}

# 修改指定键的值
dict1["age"] = 20

# 添加一个键值对
dict1["city"] = "Beijing"

# 删除指定键值对
del dict1["gender"]

print(dict1)  # 输出 {'name': 'Alice', 'age': 20, 'city': 'Beijing'}


# in

dict1 = {"name": "Alice", "age": 18, "gender": "female"}

# 判断一个键是否在字典中
print("name" in dict1)  # 输出 True
print("city" in dict1)  # 输出 False

