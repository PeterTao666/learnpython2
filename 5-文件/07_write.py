# 可以直接写入行，用writelines
# writelines表示写入很多行，参数可以是list格式
# a代表追加方式打开
with open(r'test01.txt', 'a') as f:
    # 注意字符串内含有换行符
    f.writelines('生活不仅有眼前的苟且')
    f.writelines("还有远方的枸杞")

l = ["I","love","jingjing"]
# w代表写入，覆盖以前内容
with open(r'test02.txt', 'w') as f:
    # 注意字符串内含有换行符
    f.writelines(l)

