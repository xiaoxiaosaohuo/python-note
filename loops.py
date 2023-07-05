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

# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

for i in range(5):
    
    for _ in range(i + 1):
        print('*', end='')
    print()
