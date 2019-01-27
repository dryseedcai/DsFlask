import threading

t = threading.current_thread()
print(t.getName())


def worker():
    print("i am thread")
    t = threading.current_thread()
    print(t.getName())
    pass


# 启动线程
new_t = threading.Thread(target=worker, name='ds_thread')
new_t.start()
