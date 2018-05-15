#
# class BaseCache(object):
#     def get(self, key):
#         raise NotImplementedError
#     def set(self, key,value):
#         raise NotImplementedError
#
# class RedisCache(BaseCache):
#     def get(self, key):
#         value = self.__cache.get(key)
#         return value
#
#     def set(self, key, value, timeout = 60):
#         self.__cache.set(key, value, timeout)
#
# redis_cache = RedisCache()
# redis_cache.get()

# 使用 assert

class BaseCache(object):
    def action(self, foobar):
        assert False, 'wrong'

BaseCache.action('a')