def change(b):
    print("inside",b)
    b = 4
    return b
 
a = 1
print(change(a))
 
print(a)
 
def change(b):
    print(b)
    b.append(4)
    b = [1,2,3,4,5]
    return b
 
a = [1,2,3]
change(a)
 
print(a)