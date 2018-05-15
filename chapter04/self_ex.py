# 自省是通过一定的机制查询到对象的内部结构
from chapter04.class_var import Date

class person:
    name = "User"

class Student(person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == '__main__':
    user = Student("慕课网")

    # 通过__dict__查询属性
    print(user.__dict__)
    print(user.school_name)
    print(person.name)
    user.__dict__["school_addr"]="beijing"
    print(user.school_addr)
    print(user.__dict__)