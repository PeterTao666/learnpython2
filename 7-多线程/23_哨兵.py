import multiprocessing
from time import ctime

# 设置哨兵问题
def consumer(input_q):
    print("Into cinsumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print("Out of cinsumer:", ctime()) #此句执行完成再转入主进程

def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    q.join()