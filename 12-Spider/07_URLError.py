# URLError的使用
# 运行无反馈，未解决

from urllib import request, error

if __name__ == '__main__ ':
    url = "http://www.baiduuuuu.com"

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))

    except Exception as e:
        print(e)

