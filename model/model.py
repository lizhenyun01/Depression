
class Model(object):
    def __init__(self):
        self.__blocks = []
    
    def add(self, block):
        self.__blocks.append(block)
            
    def forward(self, x):
        for block in self.__blocks:
            x = block.forward(x)
        return x
    
    def backword(self, grad):
        for block in reversed(self.__blocks):
            grad = block.backward(grad)
        return grad
    
    def __call__(self,x):
        return self.forward(x)