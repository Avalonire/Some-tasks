from abc import ABC, abstractmethod


class MyOwn(ABC):

    @abstractmethod
    def some(self):
        pass


class MyOwn2(MyOwn):

    def some(self):
        print(1)


a = MyOwn2
print(a.__dict__)