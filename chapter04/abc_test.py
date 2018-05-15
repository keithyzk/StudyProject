class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["jack", "rose"])
print(hasattr(com, "__len__"))

from collections.abc import Sized
isinstance(com, Sized)

# abc 实现抽象基类
import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get(self, key):
            pass
    @abc.abstractclassmethod
    def set(self, key, value):
            pass


# # 抽象基类
# class CacheBase():
#     def get(self, key):
#         # raise NotImplementedError
#         pass
#     def set(self, key, value):
#         # raise NotImplementedError
#         pass
#
class RedisCache(CacheBase):
    def set(self, key, value):
        pass
    def get(self, key):
        pass

redis_cache = RedisCache()
# redis_cache.set("key","value")

