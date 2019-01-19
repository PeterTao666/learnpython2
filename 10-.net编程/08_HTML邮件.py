from email.mime.text import MIMEText

mail_content = """
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

msg = MIMEText(mail_content, "html", "utf-8")

# 构建发送者地址和登录信息
from_addr = "2720723762@qq.com"
from_pwd = "yvgpmynbsnsedfhi"

# 构建邮件接收者信息
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