class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class MyClass(metaclass=Singleton):
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)  # True
