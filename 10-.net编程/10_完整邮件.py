from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello world!", "plain", "utf-8")
# 下面代码故意写错，说明，所谓的发送者的地址，只是从一个Header的第一个参数作为字符串构建
# 用utf-8编码是因为很可能内容包含非英文字符
header_from = Header("从图灵学院邮箱发出去的<TuLingXueYuan@qq.com", "utf-8")
msg['From'] = header_from

# 填写接受者信息
header_to = Header("去王小静的地方<wangxiaojing@sina.com>", "utf-8")
msg['To'] = header_to

header_sub = Header("图灵学院", "utf-8")
msg['Subject'] = header_sub

# 构建发送者地址和登录信息
from_addr = "2720723762@qq.com"
from_pwd = "yvgpmynbsnsedfhi"

# 构建邮件接受者信息
from_pwd = "yvgpmynbsnsedfhi"

to_addr = "1471380269@qq.com"

smtp_srv = "smtp.qq.com"


try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口是25

    srv.login(from_addr, from_pwd)

    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)