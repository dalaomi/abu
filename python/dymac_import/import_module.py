import importlib
import dymac_import.mock_g as g

def f1():
    """
    动态加载
    :return:
    """
    module_name = "module"
    module1 = __import__(module_name)
    h = module1.Hello()
    h.test()


def f2():
    """
        使用importlib
        importlib相比__import__()，操作更简单、灵活，支持reload()
    """
    module_name = "module"
    class_name = "Hello"
    test_module = importlib.import_module(module_name)
    test_class = getattr(test_module, class_name)
    test_obj = test_class()
    test_obj.test()

if __name__ == '__main__':
    f1()
    print("*****")
    f2()
    print(g.name)

