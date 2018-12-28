import threading
import dymac_import.mock_g as g

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()



def boll(x):
    return x*2

class Indicator(object):
    def __init__(self, name, func, freq, win_size):
        self.name = name
        self.func = func
        self.freq = freq
        self.win_size = win_size

c = Indicator('boll', boll, '1D', 200)

#g.indicator = c
g.reg_indicator('boll', boll, '1D', 200)
def test_hook():
    x = 2
    a = 10
    print("hook begin")
    if hasattr(g, "g_indicator") and g.g_indicator:
        for v in g.g_indicator.values():
            print(v)
            a = v.func(x)
    print("hook end")
    return a

print(test_hook())


dict_test = {'a':1, 'b':2}

print(dict_test.values())
print(dict_test)
for v in dict_test.values():
    print(v)



