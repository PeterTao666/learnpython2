# with 案例
with open(r'test01.txt','r') as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()

# with案列二
# list能用打开文件作为参数，把文件内每一行内容作为一个元素
with open(r'test01.txt','r') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)


