class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    #魔法方法
    def __getitem__(self, item):
        return self.employee[item]

company = Company(["Tom", "Jack", "Rose"])

# emploee = company.employee
for i in company:
    print (i)