# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self, name="jingjing", age=21):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0},my age is {1}.".format(self.name,self.age))

def sayHello():
    print("Hi,wellcome to turlin")


# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print ("Winter is coming!")