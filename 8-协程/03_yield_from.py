# yield from 举例
def gen():
    for c in 'AB':
        i = 1
        print(i)
        yield c
        i +=1

print(list(gen()))

# list 直接用生成器作为参数
def gen_new():
    yield from 'AB'

print(list(gen_new()))