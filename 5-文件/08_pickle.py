# 序列化案列
'''
import pickle
age = 19
# 'wb'表示用二进制写入
with open(r'test03.txt', 'wb') as f:
    pickle.dump(age, f)
'''
# 反序列化案列

import pickle
with open(r'test03.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)

