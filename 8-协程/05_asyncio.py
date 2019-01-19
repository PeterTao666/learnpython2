# asyncio案例
import threading
# 引入异步IO包
import asyncio

# 使用协程
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    print('Start...(%s)' % threading.currentThread())
    yield from asyncio.sleep(10)
    print('Done ... (%s)' % threading.currentThread())
    print('Hello again!(%s)' % threading.currentThread())

# 启动消息循环
loop = asyncio.get_event_loop()
# 定义任务
tasks = [hello(), hello()]
# asyncio使用wait等待task执行完成
loop.run_until_complete(asyncio.wait(tasks))
# 关闭消息循环
loop.close()
