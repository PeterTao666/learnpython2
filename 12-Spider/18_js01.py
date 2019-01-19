# 破解有道词典

from urllib import request, parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i":"girl",
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client": "fanyideskweb",
        "salt": "15477323281040",
        "sign": "5c2e2198d2767a3375c2843fe75132d3",
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
                  "Content-Length": "254",
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
    youdao("girl")