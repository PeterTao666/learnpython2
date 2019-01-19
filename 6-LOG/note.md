# LOG
- 参考技术博客： https://www.cnblogs.com/yyds/6901864.html
- python：logging模块
    - logging模块提供模块级别的函数记录日志
    - 包括四大组件
    
# 1 .日志相关概念
- 日志：记录关键信息
- 日志的级别(level)
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作=>不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# 2 logging模块
- 日志级别
    - 级别可自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别，只有当级别等于或高于指定级别才被记录
- 使用方式
    - 直接使用logging（封装了其他组件）
    - logging四大组件直接定制
    
    # 2.1 logging模块级别的日志
    - 使用以下几个函数
        - logging.debug(msg, *args, **kargs)一条严重级别为DEBUG的日志记录
        - logging.info(msg, *args, **kargs)一条严重级别为INFO的日志记录
        - logging.warning(msg, *args, **kargs)一条严重级别为WARNING的日志记录
        - logging.error(msg, *args, **kargs)一条严重级别为ERROR的日志记录
        - logging.critical(msg, *args, **kargs)一条严重级别为CIRITICAL的日志记录
        - logging.log(level, *args, **kargs)一条严重级别为level的日志记录
        - logging.basicConfig(**kargs) 对rootlogger进行一次性配置
            - 只在第一次调用的时候起作用
            - 不配置logger则使用默认值
                - 输出：sys.stderr
                - 级别：WARNING
                - 格式：level：log_name：content   
    - 举例：01_logging.py
    - format参数：省略
    
# 2.1 longging模块的处理流程
- 四大组件
    - 日志器（Logger）：产生日志的一个借口
    - 处理器（Handler）:把产生的日志发送到相应的目的地
    - 过滤器（Filter）：更精细的控制那些日子输出
    - 格式器（Formatter）：对输出信息进行格式化
- Logger
    - 产生一个日志
    - 操作：
            Logger.setLevel() 设置日至其将会处理的日志消息的最低严重级别
            logger.addHandler()  和logger.removeHandler()    为该logger对象添加和移除一个处理器
            logger.addFiler() 和 logger.removeFiler 为该logger对象添加和移除一个file文件
            logger.debug 产生一条debug级别的日志，同理info、error等
            logger.exception()  创建类似于logger.error日志消息
            logger.log()  获取一个明确的日志level参数类创建一个日志记录
    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()
- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter,removeFilter
    - 不需要直接使用，Handler是基类
        - logging.StreamHandler 将日志消息发送到输出到Stream.如std.out,std.err或者任何file
        - logging.FileHandler 将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
        - logging.handlers.RotatingFileHandler 将日志消息发送到磁盘文件并支持日志文件
        - logging.handlers.TimeRotatingFileHandler 将日志消息发给磁盘，并支持日志文件
        - logging.handlers.HTTPHandler 将日志消息以以GET或者POST的方式发送给一个HTTP服务器
        - logging.handlers..SMTPHandler 将日志消息发送给一个指定的Email地址
        - logging.NullHandler 该Handler实例会忽略error message     通常被想使用logging      
- Format
    - 直接实例化
    - 可以继承Fomat添加特殊内容
    - 三个参数
        - fmt：指定消息格式化字符串，如果不指定该参数则默认情况下使用message的原始值
        - datefmt：指定日期格式字符串，如果不能指定该参数则默认使用“%Y-%m-%d %H-%M-%S”
        - style：python3.2新增的参数，可取值为'%','{'和’$',如果不能指定参数则默认使用’%‘
        
- Filter类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息的具体内容
- 案列：02_四大组件使用.py  
                        
                 
        
                