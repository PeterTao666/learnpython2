# 利用cookie自动访问人人
# 流程：
# 1.打开登录页面后自动通过用户名密码登录
# 自动提取反馈回来的cookie
# 利用提取的cookie登录隐私页面

from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要用户名密码，用来获取登录cookie凭证
    :return:
    '''
    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登录from的两个对应input中提取name属性
    data = {
        "email":"18355329210",
        "password":"123456"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/965187997/profile"

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    # 执行完login之后，会得到授权之后的cookie
    # 我们尝试把cookie打印出来
    login()

    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)