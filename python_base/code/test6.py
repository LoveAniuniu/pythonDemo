a=22

print(bin(a))
print(oct(a))
print(hex(a))

print(int("0x16",16))

num1 = 5
num2 = 3
num3 = 7
num4 = 8
# print("5+3=",(num1+num2))
print("7+8={1},5+3={0}{0}".format(num1+num2,num3+num4))
print("5+3=%i"%(num1+num2))

str = r"c:\a\b\c.txt"
print(str)


ls = [3,True,"123"]
print(ls)
print(type(ls))
print(ls[1])
print(ls[0:2])
ls.append("展昭")
print(ls)
 
ls2 = ["a","b"]
ls.extend(ls2)
print(ls)
ls.append(ls2)
print(ls)
ls.insert(1,"张龙")
print(ls)
 
#修改就是找到对应的位置，重新赋值
ls[1] = "赵虎"
print(ls)
 
del ls[1]
print(ls)
 
ls.pop(3)
print(ls)
 
ls.remove(True)
print(ls)

t1 = (1,3,5,7,9)
print(t1)
print(type(t1))
 
print(t1[0])
# t1[0] = 8
 
t1 = (1,2,3,4,5)
print(t1)