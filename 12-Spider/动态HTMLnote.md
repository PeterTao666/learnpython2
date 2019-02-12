# 动态HTML
- 爬虫跟反爬虫

# 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从Javascript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面
    
# Selenium + PhantomJS
- Selenium：Web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install Selenium==2.48.0
    - 官网：http://selenium-python.readthedocs.io/index.html
- PhantomJS
    - 基于Webkit的无界面的浏览器        
    - 官网：http://phantomjs.org/download.html
- Selenium 库有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例：36_Selenium.py
- chrome + chromedriver
- 下载安装chrome:下载+安装
- 下载安装chromedriver：https://www.cnblogs.com/eternal1025/p/8880245.html
                        https://jingyan.baidu.com/article/b24f6c82cba6dc86bfe5da9f.html
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements-by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例：37_Selenium_UI.py       
    
# 验证码问题
- 验证码：防止机器人或者爬虫
- 分类：
    - 简单图片
    - 极验，官网：http://geetest.com
    - 12306,图片匹配
    - 电话
    - google验证     
- 验证码破解：
    - 通用方法：
        - 下载网页和验证码
        - 手动输入验证号码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证码破解网站，例：www.chaojiying.com
    - 极验，官网：http://geetest.com
        - 破解比较麻烦
        - 可以模拟鼠标移动
        - 一直在进化
    - 12306,图片匹配
    - 电话：语音识别
    - google验证    

# Tesseract
- 机器视觉领域的基础软件
- OCP:opticalChracterRecognition, 光学文字识别
- Tesseract: 一个ocr库，有google赞助
- 安装：
    - windows：https://jingyan.baidu.com/album/6181c3e0c731ba152ef153cf.html?picindex=1
    - MAac: brew install tesseract
    - Linux: apt-get install tesseract-ocr
    - 安装完成后需要设置环境变量
- 安装完后还需要pytesseract
    - pip install pytesseract
- 案例：38_数字识别.py  

# scrapy-爬虫框架
- 框架
- 爬虫框架
    - scrapy
    - pyspider
    - crawley
- scrapy框架介绍
    - https://doc.scray.prg/en/lateest/
    - http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
    
- 安装
    - 利用pip:                 

# scrapy概述
    -包含各个部件
        - ScrapyEngine：神经中枢，大脑，核心
        - Scheduler调度器，引擎发来的request请求，调度器需要处理，然后交换引擎
        - Downloader下载器：把引擎发来的request发出请求， 得到response
        - Spider爬虫：负责把下载器得到的网页/结果进行分解，分解成数据+链接
        - ItemPipeline管道：详细处理Item
        - DownloaderMiddleware下载中间件：自定义下载的功能组件
        - SpiderMiddleware爬虫中间件：对Spider进行功能扩展
    - 爬虫项目大概流程
        - 新建项目：scrapy startproject xxx
        - 明确需要目标/产出：编写item.py
        - 制作爬虫：地址 spider/xxspider.py
        - 存储内容：pipelines.py
- ItemPipeline
    - 爬虫提取出数据存入item后，item中保存的数据需要进一步处理，比如清洗，去重，存储等
    - pipeline需要处理process_item函数
        - 对应的是pipeline.py文件
        - process_item:
            - spider提取出来的item作为参数传入，同时传入的还有spider
            - 此方法必须实现
            - 必须返回一个Item对象，被丢弃的item不会不会被之后的pipeline处理
        - __init__:构造函数
            - 进行一些必要的参数初始化
        - open_spider(spider):
            -spider对象被开启的时候调用
        - close_spider(spider):
            - 当spider对象被关闭的时候调用            
- Spider
    - 对应的是文件夹spiders下的文件
    - __init__:初始化爬虫名称,start_urls列表
    - start_requests:生成Request对象交给Scrapy下载并返回response
    - parse:根据返回的response解析出相应的item自动进入pipeline；如果需要，解析出url，url交给requests模块，一直循环下去
    - start_request:此方法仅能被调用一次，读取start_urls内容并启动循环过程
    - name：设置爬虫名称
    - start_urls:设置开始第一批爬取的url
    - allow_domains：Spider允许爬取的域名列表
    - start_request(self):只能调用一次
    - parse
    - log：日志记录
- 中间件（DownloaderMinddlewares)
    - 中间件是处于引擎和下载器中间的一层组件
    - 可以有很多个，被按顺序加载执行
    - 作用是对发出的请求和返回的结果进行预处理
    - 在middlewares文件中
    - 需要在settings中设置以便生效
    - 编写中间件十分简单，中间件必须是scrapy.contrib.downloadmiddleware.DownloaderMiddleware的子类
    - 一般一个中间件完成一项功能
    - 必须实现以下一个或者多个方法
        - process_request(self, request, spider)
            - 在request通过的时候被调用
            - 必须返回None或Response或Raise IgnoreRequest
            - None：Scrapy将继续处理该request
            - Request：scrapy会停止调用prosess_request并重新调度返回的request
            - Response：scrapy将不会调用其他的process_request或者process_exception,直接将该response作为结果，
               同时调用process_response函数
        - process_response(self, request, reponse, spider)                
            - 跟process_request大同小异
            - 每次返回结果的时候会自动调用
            - 可以有多个，按顺序调用
        - 案例代码
            - import random
            - import base64
            
            # 从settings设置文件中导入值
            from settings import POXIES
            from settings import USER_AGENTS
            
            # 随机的USER-AGENT
            class RandomUserAgent(Object):
                def process_request(self, request, spider):
                    useragent = random.choice(USER_AGENTS)
                    request.headers.setdefult("User-Agent", useragent)
                    
            class RandomProxy(object):
                def process_request(self, request, spider):
                    proxy = random.choice(PROXIES)
                    if proxy['user_passwd'] is None:
                    # 没有代理账户验证的代理使用方式
                        request.meta['proxy'] = "http://" +proxy['ip_port'] 
                    else：
                    # 对账户密码进行base64编码转换
                        base64_userpasswd = base64_b64encode(proxy['user_passwd'])
                    # 对应得到代理服务器的信令格式里
                        request.headers['Proxy-Authorization'] = 'Basic' + base64_userpasswd
                        request.meta['proxy'] = "http://" + proxy['ip_port]
        - 设置settings的相关代码
- 去重
    - 为了防止爬虫陷入死循环，需要去重
    - 即在spider中的parse函数中，返回Request的时候加上dont_filter=False参数
            
            myspider(scrapy.Spider):
                def parse(...,...):
                    ......
                    yield scrapy.Rquest(url=url, callback=self.parse, dont_filter=False)
- 如何在scrapy使用selenium
    - 可以放入中间件中的process_request函数中
    - 在函数中调用Selenium，完成爬取后返回Response
            
            class MyMiddleWare(object):
                def process_request(......):
                
                    driver = webdriver.Chrome()
                    html = driver.page_source
                    driver.quit()
                    
                    return HtmlResponse(url=request.url, encoding='utf-8', body=html, request=request)                                             
- 案例e14_scrapy_baidu
    - 利用最简单的爬虫
    - 爬取百度页面
    - 关闭配置机器人协议
    - scrapy startproject baidu 
    - scrapy crawl baidu
- 案例e15-meiju
    - 创建新项目
    - 分析网页，定义item
    - 编写pipeline，确定如何处理item
    - 编写Spider，确定如何提取item        

# scrapy-shell
- 资料：https://segmentfault.com/a/1190000013199636?utm_source=tag-newest
- 启动
    - linux：ctr+T， 打开终端，然后输入scrapy shell "url:xxx" 
    - wimdows:1.anaconda prompt:scrapy shell "url:xxx"
                                启动后自动下载指定url的网页
                                下载完成后，url的内容保存在Response的变量中，如果需要，我们需要调用reponse
        - reponse
            - 爬取到的被容保存在response中
            - response.body: 网页的代码
            - response.headers: 返回的http的头信息
            - response.xpath()允许使用xpath语法选择内容
            - response.css()：允许使用css语法选取内容
        - selector
            - 选择器，允许用户使用选择器来选择自己想要的内容
            - response.selector.xpath: response.xpath是selector.xpath的快捷方式
            - selector.extract：把节点的内容用unicode形式返回
            - selector.re: 允许用户通过正则选取内容                                          