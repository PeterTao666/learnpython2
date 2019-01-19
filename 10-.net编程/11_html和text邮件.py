from email.mime.text import MIMEText # 构建附件使用
from email.mime.multipart import MIMEBase, MIMEMultipart # 构建基础邮件使用

# 构建一个MIMEMultipart邮件
msg = MIMEMultipart("alternative")

# 构建一个HTML邮件内容
html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title<title>
        </head>
        <body>

        <h1> 这是一封HTML格式邮件</h1>

        <body>
        </html> 
        """
msg_html = MIMEText(html_content, "html", "utf-8")
msg.attach(msg_html)

msg_text = MIMEText("Hello,I am Superman!", "plain", "utf-8")
msg.attach(msg_text)

# 发送email地址，此处地址直接使用我的qq邮箱，密码一般需要临时输入，此处偷懒
from_addr = "2720723762@qq.com"
# 此处密码是经过申请设置后的授权码，不是qq邮箱密码
from_pwd = "yvgpmynbsnsedfhi"

# 收件人信息
# 此处使用qq邮箱，给自己发送
to_addr = "1471380269@qq.com"

smtp_srv = "smtp.qq.com"

try:
    import smtplib
    # SMTP两个参数
    # 1.第一个是服务器地址，但一定是bytes格式，所以需要编码
    # 2.第二个参数是服务器的接受访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口是25
    # 登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件三个参数
    # 1.发送地址
    # 2.接受地址，必须是List形式
    # 3.发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)