# 1.模块
- 一个模块就是一个包含python代码的文件，后缀名称是.py就可以，模块就是个python文件
- 为什么我们用模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当作命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 不过根据模块的规范，最好在模块中编写一下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
        
- 如何使用模块
    - 模块直接导入
        - 假如模块名称直接以数字开头，需要借助importlib帮助 
    - 语法
    
        import module_name
        module_name.function_name
        module_name.name.class_name    
    - 案列 01、01、p01、p02
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同
        - 案列 p03
        
    - 从模块中导入制定内容
        - 语法：from module_name import func_name,class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入内容，不需要前缀
        - 案例：p04
       
    - 从模块中导入所有内容
        - 语法：from module_name import *
        - 优点：不需要前缀
        - 缺点：不能防止命名污染
    - 'if __name__ == "__main__"'的使用
        - 有效避免模块代码被导入的时候被动执行的问题
        - 建议所有程序的入口都以此代码为入口
        
# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径：
    - 加载模块的时候，系统会在那些地方寻找此模块
- 系统默认的模块搜索路径
   import sys
   sys.path 属性可以获取路径列表
   # 案例：p06.py
- 添加搜索路径
    sys.path.append(dir) 
- 模块的加载顺序
    1.优先搜索内存中已经加载好的模块
    2.搜索python的内置模块
    3.搜索sys.path的路径
    
# 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

    |---包
    |---|--- __init__.py 报的标志文件
    |---|--- 模块1
    |---|--- 模块2
    |---|--- 子包（子文件夹）
    |---|---|--- __init__.py 包的标志文件
    |---|---|--- 子包模块1
    |---|---|--- 子包模块2
    
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py的内容
        - 使用方式：
                package_name.func_name
                package_name.class_name.func_name()
        - 此种方式的访问内容是
        - 案例：pkg01,p07.py
    - import package_name as p
        - 具体用法跟作用方式，跟上述简单导入一致
        - 注意的是此种方法是默认对__init__.py内容的导入
        
    - import package.module
        - 导入包中某一具体的模块
        - 使用方法
                package.module.func_name
                package.modudle.class.fun()
                package.module.class.var
        - 案例：p8.py
        
    - import package.module as pm

- form ... import 导入
    - from package import module1,module2,module3···
    - 此种导入方法不在执行'__init__'的内容
            form pkg01 import p01
            p01.sayHello()
    - form package import *  
        - 导入当前包`__init__.py`文件中所有的函数和类
        - 使用方法
                func_name()
                class_name.func_name()
                class_name.var
       - 案例：p08.py 注意此种导入的具体内容
        
- from package.module import *
    - 导入包中制定的模块的所有内容
    - 使用方法
            func_name()
            class_name.func_name()
            
- 在开发环境中经常会用其他模块，可以在当前包中直接导入其它模块中的内容
    - import 完整的包或者模块的路径
    
- `__all__`的用法
    - 在使用from package import * 的时候，* 可以 导入的内容
    - `__init__.py`中如果文件为空或者没有`__all__`,那么只可以把`__init__`中
    - `__init__.py`如果设置了`__all__`的值，那么则按照`__all__`指定的子包或者模块进行
    如此则不会`__init__`中的内容
    - `__all__=['module1','module2','package',···]`                                  
        
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突
        setName()
        Student.setName()
        Dog.setName()              
    

# 异常
- 广义上的错误分为错误和异常
- 错误指的是可以人为避免
- 异常是指在语法逻辑正确的前提下，出现的问题
- 在python里，异常是一个分类，可以处理和使用

# 异常处理
- 不能保证程序永远正确运行
- 但是，必须保证程序在最坏的情况下得到的问题被妥善处理
- python的异常处理模块
    try：
        尝试实现某个操作，
        如果没出现异常，任务就可以完成
        如果出现异常，将异常从当前代码块扔出去尝试解决问题
    except 异常类型1：
        解决方案1：用于尝试在此处处理解决问题
    
    except 异常类型2：
        解决方案2：用于尝试在此处处理异常解决问题
        
    except （异常类型1，异常类型2，...）
        解决方案：所有异常的解决方案
        
    else：
        如果没有出现任何异常，将会执行此处代码
        
    finally：
        不管有没有异常都要执行的代码
        
    - 所有异常都是继承自Exception类
    
# 用户手动引发异常
- 当某些情况，用户希望自己引发一个异常的时候，可以使用
- raise 关键字来引发

# 关于自定义异常
- 只要是raise异常，则推荐自定义异常
- 在自定义异常的时候，一般包含以下内容：
    - 自定义发生异常的异常代码
    - 自定义发生异常后的问题提示
    - 自定义发生异常的行数
- 最终的目的是，一旦发生异常，方便码农快速定位错误现场       

# 常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- sring
- 上述所有模块使用理论上都应该先导入，string是特例
- calendar、time、datetime的区别参考中文意思

# calendar
- 跟日历相关的模块
- 使用需要先导入：import calendar
    - calendar：获取一年的日历字符串
    - 参数：w = 每个日期之间的间隔字符数
            l = 每周所占的行数
            c = 每个月之间的间隔字符数
            例子：cal = calendar.calendar（2017）
                  print（cal，w=5，l=7，c=0）
                  
                  
                  
# time模块
- 时间戳：一个时间表示，根据不同语言，可以是整数或者浮点数。
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
    - 32位操作系统能够支持到2038年
    - 使用方法：time.time（）
- UTC时间
    - UTC又称为世界协调时间，以应该的格林尼治天文台所在地区的时间作为参考的时间，也叫做
      世界标准时间
    - 中国时间是 UTC+8 东八区
- 夏令时
    - 夏令时就是在夏天的时候将时间调快一个小时，本意是督促大家早起早睡节省蜡烛，每天变成25个小时，本质没变还是24小时
- 时间元组
    - 一个包含时间内容的普通元组
    
- 需要单独导入 import time
- 时间模块的属性
    - timezone:当前时区和UTC时间相差的的秒数，在没有夏令时的情况下的间隔，东八区是-28800
    - altzone:获取当前时区于UTC时间相差的秒数，在有夏令时的情况下，
    - daylight：测当前是否是夏令时
    - localtime：得到当前时间的时间结构
        - 可以通过点号操作符得到相应的属性元素的内容
        - 使用方法：time.localtime()
    - asctime() ：返回元组的正常字符串之后的时间格式
        - 格式：time.asctime（时间元组）
        - 返回值：字符串 Tue Jun 6 11:11:00 2017
        - 使用举例：t = time.localtime（）
                    tt = time.asctime（t）
    - ctime（）：获取字符串化的当前时间
        - 使用举例：t = time.ctime（） 
                     print（t）
    - mktime（）：使用时间元组获取对应的时间戳
        - 格式：time.mktime（时间元组）
        - 返回值：浮点数时间戳
        - 使用举例：lt = time.localtime（）
                     ts = time.mktime（lt）
                     print(ts)
    - clock:获取cpu时间，3.0-3.3版本直接使用，3.6版本调用有问题
    - sleep(n)：使程序进入睡眠，n秒后继续
        - 使用举例：for i in range(10):
                        print(i)
                        time.sleep(1)
    - strftime：将时间元组转化为自定义的字符串格式
        - 参数百度
        - 使用举例：t = time.localtime（）
                    ft = time.strftime（“%Y年%m月%d日 %H：%M”，t）
                    print（ft）
# datetime模块
    - datetime提供日期和时间的运算和表示
    - datetime常见属性
        - datetime.date：一个理想的日期，提供year，month，day属性
            - 使用举例：print（datetime，date（2018,3,26））
        - datetime.time：提供一个理想和的时间，包括hour，minute，sec，mircrosec等内
         - datetime.datetime:提供日期跟时间的组合 
            - 使用方法：form datetime import datetime
            - 常用类方法：
                - today
                - now
                - utcnow
                - fromtimestamp:从时间戳中返回本地时间
            - 使用举例：dt = datetime(2018,3,26)
                        print(dt.today())
                        print(dt.now())
                        
                        print(dt.fromtimestamp(time.time()))
        
        - datetime.timedelta:提供一个时间差，时间长度
            - 使用方法：from datetime import datetime,timedelta
                        t1 = datetime.now()
                        print(t1.strftime("%Y-%m-%d %H:%M:%S"))
                        # td表示一小时的时间长度
                        td = timedelta(hours=1)
                        #当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
                        print((t1+td).strftime(%Y-%m-%d %H:%M:%S")) 
        - timeit:时间测量工具
            - 使用举例1：测量程序运行时间间隔实验
                def p():
                    time.sleep(3.6)
                t1 = time.time()
                p()
                print(time.time() - t1)
            - 使用举例2：
                import timeit
                c = '''
                sum = []
                for i in range(1000):
                    sum.append(i)
                '''
                
                # 利用timeit调用代码，执行100000次，查看运行时间
                t1 = timeit.timeit(stmt="[i for i in range(1000)],number=100000)
                #测量代码C执行100000次运行结果
                t2 = timeit.timeit(stmt=c，number= 10000)
                print(t1)
                print(t2)
            - 使用举例3：timeit 可以执行一个函数，来测量一个函数的的执行时间
                def doIt():
                    num = 3
                    for i in range(num):
                        print("Repeat for {0}".format(i))
                # 执行函数，重复10次
                t = timeit.timeit(stmt=doIt,number=10)
                print(t)
            - 使用举例4：
                s = '''
                def doIt(num)：
                    for i in range(num):
                        print("Repeat for {0}".format(i))
                # 执行doIt（num）
                # setup负责把环境变量准备好
                # 实际相当于给timeit创造了一个小环境
                # 在创作的小环境中，代码执行的顺序大致是
                #
                '''
                det doIt(num):
                    ···
                num = 3
                doIt(num)
                '''
                
                t = timeit.timeit("doIt(num)",setup=s+"num=3",number=10)
                print(t)
                
# os - 操作系统相关
- 跟操作系统相关，主要是文件的操作
- 于系统相关的操作，主要包含在三个模块里
    - os：操作系统目录相关
    - os.path:系统路径相关操作
    - shutil：高级文件操作，目录树的操作，文件赋值、删除、移动                    
- 路径：
    - 绝对路径：总是从根目录上开始
    - 相对路径：基本以当前环境为开始的一个地方
    
# os 模块    
    - getcwd()：获取当前的工作目录
        - 格式：os.getcwd()
        - 返回值：当前工作目录的字符串
        - 当前工作目录就是程序在进行文件相关操作，默认查找文件目录
        - 使用前需导入os 模块                                  
    - chdir():改变当前的工作目录
        - change directory
        - 格式：os.chdir（路径）
        - 返回值：无
    - listdir（）：获取一个目录中所有子目录和文件的名称列表
        - 格式：os.listdir(路径)
        - 返回值：所有子目录和文件名称的列表
    - makedirs（）：递归创建文件夹
        - 格式：os.makedirs（递归路径）
        - 返回值：无
        - 递归路径:多个文件夹层层包含的路径就是递归路径，例如：a/b/c
    - system():运行系统shell命令
        - 格式：os.system(系统命令)
        - 返回值：打开一个shell或者终端界面
        - ls是列出当前文件和文件夹的系统命令
        - 举例：rst = os.system("ls") 
                print(rst)
        - 一般推荐使用subprosess代替
    - getenv（）：获取指定的系统环境变量值
        - 相应的还有putenv（）
        - 格式：os.getenv（"环境变量名"）
        - 返回值：指定环境变量名对应的值
    - exit（）：退出当前程序
        - 格式：exit（）
        - 返回值：无
       
# 值部分
- os.curdir:当前目录
- os.pardir:父目录
    - linux系统：. 代表当前目录；..代表父目录
- os.sep:当前系统的路径分隔符
    - windows: "\"
    - linux: "/"
- os.linesep:当前系统的换行符号
    - windows："\r\n"
    - unix,linux,macos:"\n"
- os.name：当前系统的名称
    - windows:nt
    - mac、unix、linux：posix                       
- os.path模块：跟路径相关的模块
    - abspath() 将路径转化为绝对路径
        - 格式：os.path.abspath('路径')
        - 返回值：路径的绝对路径形式
        - 举例:
            absp = os.path.abspath('.')
            print（absp）
    - basename（）：获取路径中的文件名部分
        - 格式：os.path.basepath('lujing')
        - 返回值：文件名字符串
        - 举例：
                bn = op.basename('/home/tlxy')
                print(bn)
                输出：tlxy
    - jion（）：将多个路径并合成一个路径
        - 格式：os.path.jion(路径1，路径2···)
        - 返回值：组合之后的新路径字符串
        - 举例：
                bn = "/home/tlxy"
                fn = "dana.haha"
                p = os.path.jion(bd,fn)
                print(p)
                输出：/home/tlxy/dana.haha
    - split():将路径切割为文件夹部分和当前文件部分
        - 格式：os.path.split(路径)
        - 返回值：路径和文件名组成的元组
        - 举例：
                t = os.path.split('/home/tlxy/dana.haha')
                print(t)
                d,p = os.path.split('/home/tlxy/dana.haha')
                print(d,p)
                输出：（'/home/tlxy','dana.haha'）
                       /home/tlxy dana.haha
    - isdir():检测是否是目录
        - 格式：os.path.isdir(路径)
        - 返回值：布尔值
        - 举例：
                rst = os.path.isdir('/home/tlxy/dana.haha')
                rst
                输出：False
    - exists():检测文件或者目录是否存在
        - 格式：os.path.exists(路径)
        - 返回值：布尔值
        - 举例：e = exists('/home/tlxy/haha')
                 e
                 输出:False
                 
# shutil 模块
    - copy（）：复制文件
        - 格式：shutil.copy（来源路径，目录路径）
        - 返回值：返回目标路径
        - 拷贝的同时，可以给文件重命名
        - 举例：
            import shutil
            rst = shutil.copy('/home/tlxy/')
            print(rst)
            输出：/home/tlxy/haha.haha
    - copy2()复制文件，保留元数据（文件信息）
        - 格式：shutil.copy2(来源路径，目标路径)
        - 返回值：返回目标路径
        - 注意：copy于copy2的唯一区别在于copy2复制文件时尽量保留原数据
        
    - copyfile（）：将一个文件夹中的内容复制到另外一个文件当中
        - 格式：shutil.copyfile(源路径，目标路径)
        - 返回值：无
        - 举例：rst = shutil.copyfile("dana.haha","haha.haha)
                print(rst)
                输出：haha.haha
    - move():移动文件/文件夹
        - 格式：shutil.move(源路径，目标路径)
        - 返回值：目标路径
                rst = shutil.move('/home/tlxy/dana.haha','/home/tlxy/dana')
                print(rst)
                输出：/home/tlxy/dana/dana.haha
                
# 归档和压缩
- 归档：把多个文件或者文件夹合并到一个文件当中
- 压缩：用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
    - make_archive()：归档操作
        - 格式：shutil.make_archive（‘归档之后的目录和文件名’，‘后缀’，'需要归档的文件夹’）
        - 返回值:归档之后的地址
        - 举例：
                # 是想得到一个叫做tuling.zip的归档文件
                rst = shutil.make_archive('/home/tlxy/tuling','zip','/home/tlxy/dana')
                print(rst)
                输出：/home/tlxy/tuling.zip
    - unpack_archive():解包操作
        - 格式：shutil.unpack_archive('归档文件地址','解包之后地址’)
        - 返回值：解包之后的地址
        
# zip：压缩包
- 模块名称叫 zipfile
    - zipfile.ZipFile(file[,mode[,compression[,allowZip64]]])
    - 创建一个ZipFile对象，表示一个zip文件。参数file表示文件的路径或者类文件对象
        - 举例：
                zf = zipfile.ZipFile('/home/tlxy/tuling.zip')
    - ZipFile.getinfo(name):
        - 获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息。
        - 举例：
                rst = zf.getinfo("dana.haha")
                print(rst)
    - ZipFile.namelist()
        - 获取zip文档内所有文件的名称列表。
        - 举例：nl = zf.namelist（）
                print(nl)
                输出：['haha.haha','2-oop.iqpynb','dana.haha']
    - ZipFile.extractall([path[,members[,pwd]]])
        - 解压zip文档中的所有文件到当前目录。参数member是的默认值为zip文档内所有文件名称列表
        - 举例：rst = zf.extratall("/home/tlxy/dana)
                print(rst)
                
# random
- 随机数
- 所有的随机模块都是伪随机
- random()：获取0-1之间的随机小数
    - 格式：random.random（）
    - 返回值：随机0-1之间的小数
    - 举例：
            print(random.random())
            输出：0.45491379
    - choice（）：随机返回序列中的某个值
        - 格式：random.choice(序列)
        - 返回值：序列中的某个值
        - 举例：
                l = [str(i)+'haha' for i in range(10)]
                print(l)
                rst = random.choice(l)
                print(rst)
                输出：5haha
    - shuffle（）：随机打乱列表
        - 格式：random.shuffle(列表)
        - 返回值：打乱顺序之后的列表
        - 举例：
                l1 = [i for i in range(10)]
                print(l1)
                random.shuffle(l1)
                print(l1)
                输出：[0,1,2,3,4,5,6,7,8,9]
                      [4,9,0,5,3,7,8,2,1,6]
    - randint(a,b):返回一个a到b之间的随机整数，包含a和b
        - print（random.randint(0,100)）
        - help(random.randint)
                              
                      
                                               
                
                
                            
              
                                    
               
                        
                
                
        
         
           
                             
                 
                
                        
                
                
                
                                                     
                                         
                 
             
                   
                        
                        
                        
             
                    
                                              
                                                            
                          
   
 