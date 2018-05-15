#try except raise
def exe_try():
    try:
        print("code stared")
        raise KeyError
        return 1
    except KeyError as e:
        print ("key error")
        return 2
    else:
        print ("other error")
        return 3
    finally:
        print("retry")
        return 4

if __name__ == '__main__':
    result = exe_try()
    print(result)

# 上下文管理器
class Sample:
    def __enter__(self):
        print("open")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close")
    def do_somthing(self):
        print ("do somthing")

with Sample() as sample:
    sample.do_somthing()

# context 上下文管理器
import contextlib
@contextlib.contextmanager
def open_file(file_name):
    print ("open")
    yield {}
    print ("close")

with open_file("123.txt") as f_opend:
    print ("file processling")