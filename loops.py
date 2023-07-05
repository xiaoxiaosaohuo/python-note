# 遍历列表中的元素
lst = [1, 2, 3, 4, 5]
for x in lst:
    print(x)

# 遍历字符串中的字符
s = "hello"
for c in s:
    print(c)

# 遍历数字序列
for i in range(1, 6):
    print(i)


# 使用while循环计算1到100的和
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(sum)


# 使用break语句在循环中提前退出
lst = [1, 2, 3, 4, 5]
for x in lst:
    if x == 3:
        break
    print('break',x)

# 使用continue语句跳过当前循环中的某些代码块
lst = [1, 2, 3, 4, 5]
for x in lst:
    if x == 3:
        continue
    print('continue',x)

# 使用pass语句在循环中占位,不做任何操作。
lst = [1, 2, 3, 4, 5]
for x in lst:
    pass

