class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

from threading import Thread
class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)
        
if __name__ == '__main__':
    b = B()
    print(A.__mro__)
    print(b)