# 协程
- 参考资料
    - http://python.jobbole.com/86481/
    - http://python.jobbole.com/87310/
    
# 迭代器
- 可迭代（Iterable)：直接作用于for循环的变量
- 迭代器（Iterator)：不但可以作用于for循环，还可以被next调用
- list是典型的可迭代对象，但不是迭代器
- 通过isinstance判断
- Iterable和Iterator可以转换
    - 通过iter函数
- 举例：
        # 可迭代
        # l = [i for i in range(10)]
        # l是可迭代的
        # for idx in l:
            print(idx)
        # range是个迭代器
        # for i in rang(5):
            print(i)
- 举例：
        # siinstance案例
        # 判断某个变量是否是一个实例
        
        # 判断是否是可迭代
        # from collections import Iterable
          l1 = [1,2,3,4,5]
          
          print(isinstance(l1,Iterable))
          
          from collections import Iterator
          print(insinstance(l1, Iterator)  
- 举例
        # iter函数
        # s = 'i love yuanyuan' 
          print(isinstance(s, Iterable))
          print(isinstance(s, Iterator))
          
          s_ier = iter(s)
          print(isinstance(s_iter, Iterable))
          print(isinstance(s_iter, Iterator))
          
# 生成器
- generator:一边循环一边计算下一个元素的机制/算法
- 需要满足三个条件：
    - 每次调用都生产出for循环需要的下一个元素
    - 如果达到最后一个后，爆出StopIteration异常
    - 可以被next函数调用
- 如何生成一个生成器
    - 直接是使用
        - 举例：
                # 直接使用生成器
                L = [x*x for x in range(5)] #放在中括号中是列表生成器
                g = (x*x for x in range(5)) #放在小括号内就是生成器
                print(type(L))
                print(type(g))
                
    - 如果函数中包含yield， 则这个函数就叫生成器
    - next调用函数，遇到yield返回
        - 举例：
                # 函数案例
                def odd():
                    print('Step1')
                    print('Step2')
                    print('Step3')
                    return None
                odd()    
                    
                    
                # 生成器案列  
                def odd():
                    print('Step1')
                    yield 1
                    print('Step2')
                    yiele 2
                    print('Step3')
                    yield 3
                   
                # odd()是调用生成器
                g = odd()
                one = next(g)
                print(one)
                
                two = next(g)
                print(two)
                
                three = next(g)
                print(three)
                
                # for循环调用生成器
                def fib(max):
                    n, a, b = 0, 0, 1
                    while n < max:
                        print(b)
                        a,b = b, a+b
                        n += 1
                    return "Done"
                fib(5）
                
                # 斐波那契数列的生成器写法
                def fib(max):
                    n, a, b = 0, 0, 1
                    while n < max:
                        yield b
                        a,b = b, a+b
                        n += 1
                    # 需要注意，爆出异常是返回值是return的返回值
                    return "Done"
                    
                g = fib(5)
                
                for i in range(6):
                    rst = next(g)
                    print(rst) 
                  
                # ge = fib(10)
                
                # 直接for循环调用
                ge = fib(10)
                '''
                生成器的典型用法是在for中使用
                比较常用的典型生成器就是range
                '''
                for i in ge:
                    print(i)
                    
# 协程
- 历史历程
    - Python3.4引入协程，用yield实现
    - 3.5 引入协程语法
    - 实现的协程比较好的包有asyncio，tornado，gevent
- 定义：协程是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序
- 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成生成器
- 协程的实现
    - yield返回
    - send调用
    - 举例：01_协程实现.py
- 协程的四个状态
    - inspect,getgeneratorstate(...)函数确定,该函数会返回下述字符串中的一个
    - GEN_CREATED:等待开始执行
    - GEN_RUNNING:解释器正在执行
    - GEN_SUSPENED:在yield表达式处暂停
    - GEN_CLOSED：执行结束
    - next 预激（prime）
    - 举例：02_协程状态.py
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给next函数或send方法的调用方（即触发协程的对象）
    - 止协程的一种方式：发送某个哨符值，让协程退出。内置的None和Ellipsis等常量经常用作哨符值
- yield from
    - 调用协程为了得到返回值，协程必须正常终止 
    - 生成器正常终止会发出StopIteration异常，异常对象的value属性保存返回值
    - yield from 从内部捕获StopIteration异常
    - 举例：03_yield_from.py
    - 委派生成器
        - 包含yield from表达式的生成器函数
        - 委派生成器在yiel from表达式处暂停，调用方可以直接把数据发给生成器
        - 子生成器在把产出的值发给调用方
        - 子生成器在最后，解释器会抛出Iteration，并且把返回值附加到异常对象上
        - 举例：04_委派生成器.py    
       
# asyncio
- python3.4开始引入标准库中，内置对异步io的支持
- asynico本身是一个消息循环
- 步骤：
    - 创建消息循环
    - 把协程导入
    - 关闭
    - 举例:05_asyncio.py  
           06_asyncio02.py 
           
# async and await
- 为了更好的表示异步IO
- python3.5引入
- 让协程代码更简洁
- 使用上，可以简单的进行替换
    - 用async替换@asyycio.corountine
    - await 替换 yield from
    - 举例：07_async.py
    
# aiohttp
- asyncio实现单线程的并发IO,在客户端用处不大
- 在服务器端可以asyncio+corountine配合，因为http是IO操作
- asyncio实现TCP，UDP，SSL等协议
- aiohttp是给予asyncio实现的http框架
- 安装：pip install aiohttp
- 举例：08_aiohttp.py

# concurrent.futures
- python3新增的库
- 利用multiprocesiong实现真正的并行计算
- 核心原理：以子进程的形式，并行运行多个python解释器
  从而令python程序可以利用多核CPU来提升执行速度。
  由于子进程与主解释器相分离，所以他们的全局解释器锁也是相互独立的，每个子进程都能够完成完整的使用一个CPU内核。
  - concurrent.futures.Executor
    - ThreadPoolExecutor
    - ProcessPoolExecutor 
    - 执行的时候需要自行选择
  - submit(fn, args, kwargs)
    - fn:异步执行的函数
    - args，kwargs参数
- 举例：09_concurrent.py

# current中map函数
- map(fn, \*iterables, timeout=None)
    - 跟map函数类似
    - 函数需要异步执行
    - timeout：超时时间
    - 案列：10_map.py    
- Future
    -     
                       
                    
                                            
                       