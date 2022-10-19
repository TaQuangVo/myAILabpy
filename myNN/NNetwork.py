from Layer import NNLayer 

class NNetwork:
    def __init__(self, layersDef):
        self._layers = []
        for i in range(len(layersDef)-1):
            nnl = NNLayer(layersDef[i], layersDef[i+1])
            self._layers.append(nnl)
    
    def guess(self, input):
        for i in range(len(self._layers)):
            input = self._layers[i].forward_prop(input, 0)
        return input

    def train(self, input, target, lr):
        guess = self.guess(input)

        err = target - guess
        for i in reversed(range(len(self._layers))):
            err = self._layers[i].backward_prop(err, lr, 0)
