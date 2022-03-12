class Name(object):
    def __init__(self, value):
        self.__value = value
    def value(self):
        return self.__value
    def update_value(self, value):
        self.__value = value
        
        
class Person(object):
    def __init__(self,name):
        self.__name = name
        
    def name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
        
    
    def update_name(self, value):
        self.__name.update_value(value)


a = Person(Name('1'))

b = Person(Name('2'))

m = a()
print(m)
