from chapter04.class_var import Date

class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year

class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday


if __name__ == "__main__":
    user = User(Date(1970,2,12))
    student = Student(Date(2014,9,12))
    # print(user._User__birthday)
    print(user._User__birthday)
    print(student._Student__birthday)
    print(user.get_age())
    print(Student.__mro__)