from layer import Layer


class Block(Layer):
    def __init__(self, name: str =None):
        super.__init__(name)
        self.__layers= []
        
    def add(self, layer: Layer):
        self.__layers.append(layer)
        
    def forward(self, x):
        for layer in self.__layers:
            x = layer.forward(x)
        return x
        
    def backward(self, grad):
        for layer in reversed(self.__layers):
            grad = layer.backward(grad)
        return grad
    

        