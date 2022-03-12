import numpy as np
from tools.error import *


class Variable(object):
    '''
    args:

    
    '''
    def __init__(self, value, shape, dtype, name=None):
        self.__value = value
        self.__name = name
        self.__shape = shape
        self.__dtype = dtype
        

    #获取name
    def name(self):
        return self.__name
    
    def shape(self):
        return self.__shape

    def dtype(self):
        return self.__dtype

    def value(self):
        return self.__value
    
    def updata(self, value):
        self.__value = value

def variavle(value, name=None):
    if type(value) is np.ndarray:
        return Variable(value, value.shape, dtype=dtype(value), name=name)
    elif type(value) is list:
        return Variable(np.asarray(value, dtype), value.shape, dtype=dtype(value), name=name)
    
    else:
        error("Value must be numpy.ndarray or list !")

def zeros(shape, dtype=float, name=None):
    value = np.zeros(shape,dtype)
    return Variable(value, shape, dtype, name=name)

def ones(shape, dtype=float, name=None):
    value = np.ones(shape,dtype)
    return Variable(value, shape, dtype, name=name)


def random(shape, name=None, init=None):
    '''
    
    init:zero,one,random
    
    '''
    value = np.random.random(shape)
    return Variable(value, shape, float, name)
    