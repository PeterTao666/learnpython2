# 导入相关包
# poplib负责从MDA到MUA下载
import poplib

# 一下包负责相关邮件结构解析
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 得到邮件的原始内容
# 这个过程主要负责从MDA到MUA的下载并使用Parser粗略解析
def fetMsg():
    # 准备相应的信息
    email = "2720723762@qq.com"
    # 邮箱的授权码
    pwd = "yvgpmynbsnsedfhi"

    # pop3服务器地址
    pop3_srv = "pop.qq.com" # 端口995

    # ssl代表是安全通道
    srv = poplib.POP3_SSL(pop3_srv)

    # user代表email地址
    srv.user(email)
    # pass代表密码
    srv.pass(pwd)