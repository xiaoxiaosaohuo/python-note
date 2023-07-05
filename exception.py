try:
    x = int(input("请输入一个整数："))
    y = 10 / x
    print("结果为：", y)
except ValueError:
    print("输入的不是整数！")
except ZeroDivisionError:
    print("除数不能为零！")
else:
    print("没有出现异常！")
finally:
    print("程序执行完毕！")
