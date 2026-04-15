class SingleTon(object):
    __instance = None
    def __new__(cls,*args,**kwargs):
        if not isinstance(cls.__instance,cls):
            cls.__instance = object.__new__(cls)
        return cls.__instance


class Foo(SingleTon):
    # def __new__(cls, *args,**kwargs):
    #     print('Static method')
    #     instance = super(Foo,cls).__new__(cls)
    #     return instance


    def __init__(self,value=None):
        print('Self constructor')
        self.value = value

test = Foo(123456)

test_2 = Foo(55449554)
print(id(test))
print(id(test_2))
print(id(test_2) == id(test))

