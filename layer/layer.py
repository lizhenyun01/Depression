from variable.variable import *


class Layer(object):
    def __init__(self, name: str =None):
        self.__name = name
    
    def name(self):
        return self.__name
    
    def forward(self, x):
        return x
    
    def backward(self, grad):
        return grad
    
    