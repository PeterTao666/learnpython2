# 使用cookie登录
from urllib import request

if __name__ == '__main__':

    url = 'https://mail.163.com/js6/w?sid=vARbHhwsyFPrNFcpfissYRlMhrqUMurw&func=ntes:udproxy:getAttrs'

    headers = {
        "Cookie": "..."
    }
    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)