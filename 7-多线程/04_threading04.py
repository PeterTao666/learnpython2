'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
练习带参数的多线程启动方法
'''
import time
# 导入threading包
import threading

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop1 at:', time.ctime())
    # 把参数打印出来
    print("我是参数", in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop1 at:', time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop2 at:', time.ctime())
    # 把参数in1和in2打印出来，代表使用
    print("我是参数", in1, "和参数", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop2 at:', time.ctime())

def main():
    print("Starting at:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("来一瓶82年的拉菲", ))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("来一瓶茅台飞天", "还是来两瓶二锅头好了"))
    t2.start()
    # 加入jion
    t1.jion()
    t2.jion()
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
