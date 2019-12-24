print("5+3={0},5-3={1}{0}".format(5+3,5-3))

s="wanghao"
print(len(s))
print(s[2])
print(s[-2])

s =" sss "
print(s.rstrip())
print(s.lstrip())

print(s.strip())


alien_0 = {'color': 'green', 'points': 5}   

print(alien_0)

del alien_0['color']

print(alien_0)


a = set('abracadabra') 
b = set('alacazam')
print(a)
print(b)
print(a - b) # a和b的差集
print(a | b) # a和b的并集
print(a & b) # a和b的交集
print(a ^ b) # a和b中不同时存在的元素



fruits = ['banana', 'apple', 'mango']
for i in range(len(fruits)):
    print(fruits[i])


for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        if x == "B": 
            continue
        print (x + y)

num = 1 
def fun1():
    #global num #需要使用global关键字声明 print(num)
    num = 123
    print(num)
    print(num)
fun1()
