# # 上下文管理器
#
# class Databases():
#     def __init__(self):
#         self.connected = False
#     def connect(self):
#         self.connected = True
#     def close(self):
#         self.connected = False
#     def query(self):
#         if self.connected:
#             return 'select data'
#         else:
#             raise ValueError("DB not connected")
#
# def handle_query():
#     db = Databases()
#     db.connect()
#     print("handle----"), db.query()
#     db.close()
#
# def main():
#     handle_query()
#
# if __name__ == '__main__':
#     main()

class Databases():
    def __init__(self):
        self.connected = False
    def __enter__(self):
        self.connected = True
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
    def query(self):
        if self.connected:
            print("select data")
        else:
            raise ValueError("DB not connected")

def hanndle_query():
    with Databases() as db:
        print("handle---"), db.query()

def main():
    hanndle_query()

if __name__ == '__main__':
    main()