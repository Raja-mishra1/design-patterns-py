
class Singleton:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
            cls.__instance.value = 0
        return cls.__instance

    def increment(self):
        self.value +=1

if __name__ == "__main__":
    Singleton1 = Singleton()
    Singleton2 = Singleton()

    Singleton1.increment()
    print(Singleton1.value)
    print(Singleton2.value)



