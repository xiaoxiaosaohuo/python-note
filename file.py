import requests
import json
import time
# r open a file for reading
# w open a file for writing
# x open a file for exclusive creation, if the file already exists, the operation fails
# a open a file for appending at the end of the file without truncating it
# t open in text mode
# open in binary mode
# + open a file for updating(reading and writing)
file1 = open('test.txt')

# read the file
read_content = file1.read()
print(read_content)
file1.close()


# Exception handling in files

try:
    file1 = open('test.txt','r')
    read_content = file1.read()
    print(read_content)
finally:
    file1.close()



with open('test.txt','r') as file1:
    read_content = file1.read()
    print(read_content)

# write to files

with open('test2.txt','w') as file2:
    file2.write('programming is fun.\n')
    file2.write("let's go")

# create the generator object
squares_generator = (i * i for i in range(5))
for i in squares_generator:
    print(i)

def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())


def openfile():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def openfile():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)

## 读写二进制文件


def binaryfile():
    try:
        with open('1.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('2.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


## JSON


def json():
    mydict = {
        'name': 'deny',
        'age': 38,
        'qq': 957658,
        'friends': ['nick', 'maya'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


# json模块主要有四个比较重要的函数，分别是：

# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象


def fetchData():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])
