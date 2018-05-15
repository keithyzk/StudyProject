class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    #静态方法
    @staticmethod
    def parese_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    #类方法
    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year = self.year, month = self.month, day = self.day)

if __name__ == "__main__":
    new_day = Date(2018, 4, 22)
    print(new_day)

    # 静态方法完成初始化
    new_day = Date.parese_from_string(date_str="2018-12-32")
    print(new_day)

    # 类方法完成初始化
    date_str = "2018-12-33"
    new_day = Date.from_string(date_str)
    print(new_day)