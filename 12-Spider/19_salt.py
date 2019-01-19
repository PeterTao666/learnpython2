# 案例二：处理js加密代码
'''
通过查找，能找到js代码中操作代码
1、计算salt值：r = "" + (new Date).getTime(),
               i = r + parseInt(10 * Math.random(), 10)；
2、sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
   说明：md5一共需要四个参数，第一个和第四个都是固定值得字符串，第三个是所谓的salt，第二个是输入的要查找的单词
'''

def getSalt():
    '''
    salt公式是：r = "" + (new Date).getTime(),
               i = r + parseInt(10 * Math.random(), 10)；
    把他翻译成python代码
    :return:
    '''
    import time, random
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    # update需要一个bytes格式的参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return sign

def getSign(key, salt):
    sign = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    sign = getMD5(sign)
    return sign

from urllib import request, parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = getSalt()
    data = {
        "i": key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        "ts": "1547732328104",
        "bv": "ab57a166e6a56368c9f95952de6192b5",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    data = parse.urlencode(data).encode()

    headers = {
                  "Accept": "application/json, text/javascript, */*; q=0.01",
                  # "Accept-Encoding": "gzip, deflate",
                  "Accept-Language": "zh-CN,zh;q=0.9",
                  "Connection": "keep-alive",
                  "Content-Length": len(data),
                  "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                  "Cookie": "OUTFOX_SEARCH_USER_ID=1673339245@58.242.142.64;OUTFOX_SEARCH_USER_ID_NCOO=1560942349.7731295;JSESSIONID=aaaXiMsTcQy0EfKicbCHw;__guid = 204659719.3936192943466982000.1547732137377.3496;monitor_count=1;___rl__test__cookies = 1547732328091",
                  "Host": "fanyi.youdao.com",
                  "Origin": "http://fanyi.youdao.com",
                  "Referer": "http://fanyi.youdao.com/",
                  "User-Agent": "Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/63.0.3239.132 Safari/537.36",
                  "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)

if __name__ == '__main__':
    youdao("boy")