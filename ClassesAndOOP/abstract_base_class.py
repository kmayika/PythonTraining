from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        raise NotImplementedError
    @abstractmethod
    def bar(self):
        raise NotImplementedError

class Concrete(Base):
    def foo(self):
        return 'foo called'

print(issubclass(Concrete, Base))
c = Concrete()
# print(c.foo())