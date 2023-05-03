x=10
y='20.3'
print(x,y)

c = 'hello world'
def func():
    c = 'Siven'
    print(c)

def func1():
    global c 
    c = 'Siven1'
    print(c)

func()
print(c)
func1()
print(c)

# Data Types
a = 19
print(type(a))

a = 3.14
print(type(a))

a = "hello world"
print(type(a))

a = [1,2,3]
print(type(a))

a = (1,2,3)
print(type(a))

a = {1,2,3}
print(type(a))

a = {'name':'Siven','age':32}
print(type(a))
