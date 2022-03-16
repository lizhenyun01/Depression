from multiprocessing.sharedctypes import Value
import numpy as np
from variable.variable import *

'''
方法实现:输入variable/num
        输入合法性验证
        读取shape
        利用numpy做计算
        为结果创建新变量并输出
'''



@staticmethod
def mul(arg1, arg2):
# 元素乘法
    if isinstance(arg1, Variable):
        arg1 = arg1.value
    if isinstance(arg2, Variable):
        arg2 = arg2.value
    value = np.multiply(arg1,arg2)
    if not isinstance(value, np.ndarray):
        value = np.array(value)
    return variavle(value)

@staticmethod
def matmul(arg1, arg2):
# 矩阵乘法
    return

@staticmethod
def add(arg1, arg2):
# 加法，支持自动广播
    return

@staticmethod
def subtract(arg1, arg2):
# 减法，支持自动广播
    return

@staticmethod
def divide(arg1, arg2):
# 除法
    return

@staticmethod
def reciprocal(arg1):
# 取倒数
    return

@staticmethod
def exp(arg1):
# e为底的指数函数
    return

@staticmethod
def pow(arg1, arg2):
#幂函数
    return

@staticmethod
def tan(arg1):
    return

@staticmethod
def cos(arg1):
    return

@staticmethod
def sin(arg1):
    return

@staticmethod
def abs(arg1):
# 取绝对值
    return

@staticmethod
def around(arg1):
# 四舍五入
    return

@staticmethod
def floor(arg1):
# 向下取整
    return

@staticmethod
def ceil(arg1):
# 向上取整
    return

@staticmethod
def mod(arg1):
# 取模
    return