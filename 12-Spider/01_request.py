# 使用urllib.request请求一个网页内容，并把内容打印出来
from urllib import request

if __name__ == '__main__':
    url = "https://nanjing.anjuke.com/?pi=navi-360-mz"
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))

    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode()

    print(html)