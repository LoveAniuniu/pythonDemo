import threading
import time
 
def fun1(a):
    print(a)
    for i in range(50):
        # time.sleep(1)#让线程暂停
        print(threading.current_thread().getName(), i)
 
def fun2(a):
    print(a)
    for i in range(65, 76):
        time.sleep(1)
        print(threading.current_thread().getName(), chr(i))
 
# #创建两个线程
# thread1 = threading.Thread(target=fun1,args=(1,),name="线程一")
# thread2 = threading.Thread(target=fun2,args=(2,),name="线程二")
# #启动线程
# thread1.start()
# thread2.start()
 
 
class MyThread(threading.Thread):
    def __init__(self,a,name):
        # super().__init__(name=name)
        threading.Thread.__init__(self,name=name)
        self.a = a
 
    def run(self):
        if self.a ==1:
            fun1(self.a)
        elif self.a == 2:
            fun2(self.a)
 
thread1 = MyThread(1,"线程一")
thread2 = MyThread(2,"线程二")
thread1.start()
thread2.start()