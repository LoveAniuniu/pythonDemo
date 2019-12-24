import os

srcfile = "/Users/ouhiroshi/personalSoftWare/pythonWorkSpace/pythonDemo/python_base/note/fool.txt"
fpath,fname=os.path.split(srcfile) #分离文件名和路径
if not os.path.exists(fpath): # 判断当前路径是否存在，没有则创建new文件夹
    os.makedirs(fpath)
# 如果此文件存在则打开，否则创建此文件 
print(fpath,fname)
f = open(srcfile,"w")
f.write( "ccccc" )
# 关闭打开的文件 
f.close()
# 打开一个文件
f = open(srcfile, "r")
str = f.read() 
print(str)
# 关闭打开的文件 
f.close()


fpath,fname = os.path.split(srcfile)
if not os.path.exists(fpath):
    os.makedirs()

f = open(srcfile,'w')
f.write("dddsfsfsfs")

f.close()

f = open(srcfile,'r')
for line in f:
    print(line,end='')

import re
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string)) 
print(re.search(pattern2, string))
print(re.search(r"r[A-Z]n", "dog runs to cat")) 
print(re.search(r"r[a-z]n", "dog runs to cat")) 
print(re.search(r"r[0-9]n", "dog r2ns to cat")) 
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))

  