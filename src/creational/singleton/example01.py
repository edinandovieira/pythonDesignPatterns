class Singleton():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class NoSingleton():
    a = None


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

obj3 = NoSingleton()
obj4 = NoSingleton()

print(obj3 is obj4)