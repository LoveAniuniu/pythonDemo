class MyClass:
    def __init__ (self): 
        print("我是初始内容{0}".format(2222))

    i = 12345
    def f(self):
        return 'hello world'

# 实例化类 
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为:", x.i) 
print("MyClass 类的方法 f 输出为:", x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i) # 输出结果:3.0 -4.5

class Test:
    def prt(self):
        print(self)
        print(self. __class__)
t = Test() 
t.prt()

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("除数不能为0")

div(3,0)



