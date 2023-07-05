def add(x,y,*args,**kwargs):
    result = x + y
    print(args,type(args)) # (3,4)
    for arg in args:
        result += arg
    for key,value in kwargs.items():
        print(key,value)
        result += value
    return result

add(1,2,3,4,a=5,b=6)

def fib():
    f,s = 0,1
    while True:
        yield f
        f,s = s,f+s

for x in fib():
    
    if x > 10:
        break
    print(x,end=' ')
# help(print) 查看print函数doc
# yield关键字用于将函数转换为生成器，它可以暂停函数的执行，并返回一个值。当生成器被调用时，它会从上一次暂停的位置继续执行，直到遇到下一个yield关键字或函数结束。

#lamnda arguments:expression,在一行代码中定义简单的函数
sum = lambda x,y:x+y
print(sum(3,4))

# 作用域

def foo():
    global a # 声明全局变量
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
