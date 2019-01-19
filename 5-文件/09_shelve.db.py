# 使用shelve创建文件并使用
import shelve
# 打开文件
# shv相当于一个字典
shv = shelve.open(r'shv.db')

shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

# 通过以上案列发现，shelve自动创建的不仅仅是一个shv.db文件，还包括其他文件

# shelve读取案列
shv  = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['three'])
except Exception as e:
    print("烦死了")
finally:
    shv.close()