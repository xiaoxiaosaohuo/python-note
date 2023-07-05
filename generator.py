import sys
def generator_function():
    for i in range(10):
        yield i



gen = generator_function()
print(next(gen))
print(next(gen))

my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))

f = [x for x in range(1, 10)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)
print(sys.argv)

# 生成器表达式
f = (x ** 2 for x in range(1, 1000)) 
# 是一个生成器表达式。生成器表达式使用圆括号括起来，并返回一个生成器对象。生成器对象是一个可迭代对象，它可以逐个生成值，而不是一次性生成所有值。这种方式可以节省内存，因为它只在需要时生成值，而不是一次性生成所有的值。您可以使用next()函数或for循环逐个获取生成器对象的值。
# 生成器表达式适用于需要逐个处理大量数据的情况，因为它们可以减少内存消耗。

# 列表推导式
f = [x ** 2 for x in range(1, 1000)] 
# 是一个列表推导式。列表推导式使用方括号括起来，并返回一个列表对象。列表对象是一个包含所有生成值的列表。这意味着在执行列表推导式时，会一次性生成所有的值并存储在内存中。这种方式适用于需要一次性获取所有值并进行随机访问的情况。

# 列表推导式适用于数据量较小或需要一次性获取所有值的情况。

#斐波那契额

def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a