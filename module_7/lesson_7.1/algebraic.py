class Adder:
    def __add__(self, obj):
        raise NotImplemented
    

class ListAdder(Adder):
    def __init__(self,list_with_values=None):
        if list_with_values is None:
            self.list = list()
        else:
            self.list = list_with_values

    def __add__(self,obj):
        return sorted(self.list + obj.list)
    
class DictAdder(Adder):
    def __init__(self,dict_with_values=None):
        if dict_with_values is None:
            self.dict = dict()
        else:
            self.dict = dict_with_values

    def __add__(self,obj):
        return {**self.dict,**obj.dict}

    
# list_adder = ListAdder([2,5])
# list_adder_2 = ListAdder([8,9])
# print(list_adder + list_adder_2)

dict_adder = DictAdder({'1': 1, '2': 2})
dict_adder_2 = DictAdder({'3': 3, '4': 4})
print(dict_adder + dict_adder_2)
