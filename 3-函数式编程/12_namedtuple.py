import collections
Point = collections.namedtuple("Point",['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])

Circle = collections.namedtuple("Circle",['x','y','r'])
c = Circle(100,150,50)
print(c)
print(type(c))

# 想检测一下nametuple到底属于谁的子类
isinstance(c,tuple)
