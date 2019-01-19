# 爬虫准备工作
- 参考资料
    - python网络数据采集，图灵工业出版
    - 精通Python爬虫框架Scrapy，人民邮电出版社
    - [Python3网络爬虫](http://blog.csdn.net/c406495762/article/detail/72858983)
    - [Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
- 前提知识
    - url
    - httl协议
    - web前端，html，css，js
    - ajax
    - re
    - xml
    
# 1.爬虫简介
- 爬虫定义：参考百度
- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载信息
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行以上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
- Python网络包简介
    - Python2.x: urllib, urllib2, urllib3, httplib, httplib2, requests
    - Python3.x: urllib, urllib3, httplib2, requests
    - python2: urllib和urllib2配合使用， 或者requests
    - Python3: urllib和requests
    
# 2.urllib
- 包含模块
    - urllib.request: 打开和读取urls
    - urllib.error: 包含urllib.request产生的常见的错误，使用try捕捉
    - urllib.parse: 包含解析url的方法
    - urllib.robotparse: 解析robots.txt文件
    - 案例：01_request.py
- 网页编码问题解决
    - chardet：可以自动检测页面文件的编码格式，但是可能有误
    - 需要安装，conda install chardet           
    - 案例：02_chardet.py
- urlopen 的返回对象
    - 案例：03_urlopen.py
    - geturl: 返回请求对象的url
    - info：请求反馈对象的meta信息
    - getcode：返回的http code
- reauest.date 的使用
    - 访问网络的两种方法
        - get：
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
            - 案例：04_get.py
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息，需要用到data参数
            - 使用post。意味着Http的请求头可能需要更改：
                - Content-Type：application/x-ww.form-urlencode
                - Content_Lenth: 数据长度
                - 简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案例：05_post.py       
            - 为了更多的设置请求信息，单纯的通过urlopen函数已经不太好用了
            - 需要利用request.Requst 类
            - 案例：06_post02.py
            
- urllib.error
    - URLError产生的原因
        - 没网
        - 粉武器链接失败
        - 指不到指定的服务器
        - 是OSError的子类
        - 案例：07_URLError.py
    - HTTPError, 是URLError的一个子类
        - 案例：08_HTTPError.py            
    - 两者区别：
        - HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上的，则引发HTTPError
        - URLError对应的一般是网络出现问题，包括url问题
        - 关系区别：OSError-URLError-HTTPError
        
- UserAgent
    - UserAgent: 用户代理，简称UA，数以heads的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值， 使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
        - 1.Android
            Mozilla/5.0(linux; Andriod 4.1.1; Nexus 7 BuildJROd03D) AppleWebkit/535(KHTML,)
            Mozilla/5.0(linux; U; Andriod 4.0.1; en-gb;) AppleWebkit/535(KHTML,)
            Mozilla/5.0(linux; U; Andriod 2.2;
            
          2.Firefox
            Mozilla/5.0
            Mozilla/5.0
            
          3.Google Chrome
            Mozilla/5.0
            Mozilla/5.0
            
          4.iOS
            Mozilla/5.0
            Mozilla/5.0
    
    - 设置UA可以通过两种方式：
        - heads
        - add_header
        - 案例：09_UA.py
        
# ProxyHandler处理（代理服务器）
    - 使用代理IP，是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许频繁访问某一要个固定网站，所以，代理一定要很多很多
    - 基本使用步骤：
        1.设置代理地址
        2.创建ProxyHandler
        3.创建Opener
        4.安装Opener
    - 案例：10_ProxyHandler.py
    
#　cookie & session
-  由于http协议的无记忆性，人们为了弥补这个缺憾，所以采用的一个补充协议
- cookie是发放给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息
- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上一定时间，会过期
    - 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
- session的存放位置
    - 存在服务器端
    - 一般情况，session是放在内存中或者数据库中
    - 案例：11_没有cookie登录.py
- 使用cookie登录
    - 直接把cookie复制下来，然后手动放入请求头
    - 案例：12_cookie登录.py
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar实例回收回来后cookie将消失
        - FileCookieJar(filename, delayload=None, policy=None)
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillarCookieJar(filename, delayload=None, policy=None)：
            - 创建与mocilla浏览器cookie.txt兼容的Filename实例
        - LwpCookieJar(filename, delayload=None, policy=None)：
            - 创建与libwww-perl标准兼容的Set-Cookies3格式的FileCookieJar实例
        - 他们的关系是：CookieJar-->FileCookieJar-->MozillaCookieJar&LwpCookieJar
    - 案例：利用cookiejar访问人人网，13_cookiejar.py
        - 自动使用cookie登录，大致流程是
        - 打开登录页面后自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登录隐私页面
    - handler是Handler的实例，常用来查看案例代码
        - 用来处理复杂请求
            # 创建cookiejar的实例
            cookie = cookiejar.CookieJar()
            # 生成cookie的管理器
            cookie_handler = request.HTTPCookieProcessor(cookie)
            # 创建http请求管理器
            http_handler = request.HTTPHandler()

    - 创立handler后，使用opener打开，打开后相应的业务由相应的handler处理
    - cookie作为一个变量，打印出来，案例：14_handler.py
        - cookie的属性
            - name：名称
            - value：值
            - domain：可以访问此cookie的域名
            - path：可以访问此cookie的页面路径
            - expires：过期时间
            - size：大小
            - Http字段
        - cookie的保存-FileCookieJar
            - 案例：15_filecookiejar.py
        - cookie的读取
            - 案例：16_cookie读取.py 
                                 
# SSL
    - SSL证书就是遵守SSL安全套阶层协议的服务器数字证书（SercureSocketLayer）
    - 美国网警公司开发
    - CA(CertifacateAuthority)是数字证书认证中心，是发放、管理、废除数字证书的授信人的第三方机构
    - 遇到不信任的SSL证书，需要单独处理，案例：17_SSL.py
    
# js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是取MD5值）
    - 经过加密，传输的就是密文，但是
    - 加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 过程参考案例：18_js01.py
                    19_salt.py                                      
          
                  
     
             