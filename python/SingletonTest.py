def singleton(cls, *args, **kwargs):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student('jiang', 25)
print(student)
student = Student('jiang', 35)
print(student.age)